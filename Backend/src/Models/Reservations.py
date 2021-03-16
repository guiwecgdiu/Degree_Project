from src.extension import db
from datetime import datetime
from src.Utility import reservation_list


class Reservation(db.Model):
    __tablename__ = 'reservation'
    username = ""
    petname = ""
    create_time = ""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String, nullable=True)
    state = db.Column(db.String, nullable=True)
    place = db.Column(db.String, nullable=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    surgery_date = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'))

    @staticmethod
    def remove_res(id):
        res = Reservation.get_res(id)
        if res != None:
            db.session.delete(res)
            db.session.commit()
            print("remove reservation successfully")
            return res
        else:
            print("wrong reservation remove")
        # read method

    @staticmethod
    def add_res(user, pet, type, place, state):
        print("user:" + str(user))
        print("pet:" + str(pet))
        print("type:" + type)
        print("place:" + place)
        print("state:" + state)
        # print("save reservation: [username: %s, petname: %s, type: %s, state: %s, place: %s]" % (user.username, pet.petname, type, place, state))
        if type in ['emergency', 'standard'] and place in ['Beijing', 'Shanghai', 'Chengdu'] and state in [
            'surgery confirmed', 'completed', 'ready for release']:
            print("add reservation ready")
            reservation = Reservation(type=type, state=state, place=place, user_id=user.id, pet_id=pet.id)
            db.session.add(reservation)
            db.session.commit()
            reservation_list.add_list(reservation.id)
            print("add reservation successfully")
            return reservation
        else:
            return 'Invalid'

    @staticmethod
    def read_all(limit=None, order_by=None):
        query = Reservation.query
        # if limit is not None:
        #     query=query.limit(limit)
        # if order_by is not None:
        #     query=query.order_by()
        ress = query.order_by(Reservation.id.desc()).all()
        print("read all reservation successfully")
        return ress

    @staticmethod
    def read_all_unfinished(limit=None, order_by=None):
        query = Reservation.query
        # if limit is not None:
        #     query=query.limit(limit)
        # if order_by is not None:
        #     query=query.order_by()
        ress = query.filter(Reservation.state != "finished").order_by(Reservation.id.desc()).all()
        print("read all unfinished reservation successfully")
        return ress

    @staticmethod
    def get_res(id=None):
        id = int(id)
        if id is None:
            # res = Reservation.query.first()
            return None
        else:
            res = Reservation.query.filter(Reservation.id == id).first()
            # print("get reservation id: " + str(id))
            # print("reservation id: " + str(res.id))
            if res.id == id:
                # print("11")
                return res
            else:
                return None

    @staticmethod
    def get_user_res(id=None):
        id = int(id)
        if id is None:
            # res = Reservation.query.first()
            return None
        else:
            res = Reservation.query.filter(Reservation.user_id == id).order_by(Reservation.id.desc()).all()
            # print("11")
            return res

    @staticmethod
    def get_user_res_unfinished(id=None):
        id = int(id)
        if id is None:
            # res = Reservation.query.first()
            return None
        else:
            res = Reservation.query.filter(Reservation.state != 'finished', Reservation.user_id == id).order_by(
                Reservation.id.desc()).all()
            # print("11")
            return res

    @staticmethod
    def set_user_pet_name(reservation=None, user=None, pet=None):
        if reservation is not None:
            if user is not None:
                reservation.username = user.username
            if pet is not None:
                reservation.petname = pet.petname
        # print(reservation)
        return reservation

    @staticmethod
    def update_state(list=None):
        if list is None:
            return
        else:
            print("update state")
            print(list)

            res = Reservation.query.filter(Reservation.id == int(list[0])).first()
            res.state = list[1]
            if list[2]:
                # print(list)
                res.surgery_date = list[2]
            db.session.commit()

    @staticmethod
    def update_res(id=None, pet=None, type=None, place=None):
        if id is None:
            return
        else:
            print("update reservation")
            res = Reservation.query.filter(Reservation.id == id).first()
            res.pet_id = pet.id
            res.type = type
            res.place = place
            print(res)
            db.session.commit()

    @staticmethod
    def set_createTime(res=None):
        if res is not None:
            res.create_time = res.timestamp.strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def get_pet_res(pets):
        if pets is None:
            return None
        else:
            dicty = {}
            for pet in pets:
                dicty[pet] = (Reservation.query.filter(Reservation.pet_id == pet.id).first())
            print(dicty)
            return dicty

    @staticmethod
    def get_available_pet(pets):
        p = []
        for pet in pets:
            r = Reservation.query.filter(Reservation.pet_id == pet.id, Reservation.state != "finished").first()
            if not r:
                p.append(pet)
            elif r.state == 'ready for release':
                p.append(pet)
        return p

    @staticmethod
    def res_finish(id):
        r = Reservation.get_res(id)
        r.state = "finished"
        db.session.commit()

    def __repr__(self):
        return '<id: {},type: {},state: {},place: {},timestamp: {},user_id: {},pet_id: {}>'.format(self.id, self.type,
                                                                                                   self.state,
                                                                                                   self.place,
                                                                                                   self.timestamp,
                                                                                                   self.user_id,
                                                                                                   self.pet_id)
