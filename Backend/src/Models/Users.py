import jwt
from src.extension import db
from time import time
from src.Models.Pets import Pet
from src.Models.Reservations import Reservation
from flask import current_app
from datetime import datetime
from src.Models.Role import Role
from src.Models.Role import Permission
from flask_avatars import Identicon


class User(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=False)
    password_hash = db.Column(db.String(128))

    #user details
    name = db.Column(db.String(30))
    website = db.Column(db.String(255))
    bio = db.Column(db.String(120))
    location = db.Column(db.String)
    member_since = db.Column(db.DateTime, default=datetime.utcnow())
    confirmed = db.Column(db.Boolean, default=False)
    messages=db.relationship('Message',back_populates='user',cascade="all")

    #user avater
    avater_s=db.Column(db.String(64))
    avater_m=db.Column(db.String(64))
    avater_l=db.Column(db.String(64))






    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship('Role', back_populates='users')

    pets = db.relationship('Pet',
                           backref='user',
                           lazy='dynamic')
    reservations = db.relationship('Reservation', backref='user',
                                   lazy='dynamic')

    def __init__(self,**kwargs):
        super(User,self).__init__(**kwargs)
        self.set_role()
        self.generate_avatar()

    def set_role(self):
        if self.role is None:
            if self.email in current_app.config['ADMIN_EMAIL']:
                self.role = Role.query.filter_by(name='DOCTOR').first()
            else:
                self.role = Role.query.filter_by(name='USER').first()
            db.session.commit()

    def isAdmin(self):
        return self.role.name == "DOCTOR"

    def can(self,permission_name):
        permission=Permission.query.filter_by(name=permission_name).first()
        return permission is not None and self.role is not None and permission in self.role.permissions

    def generate_avatar(self):
        avatar = Identicon()
        filename=avatar.generate(text=self.username)
        self.avater_s=filename[0]
        self.avater_s = filename[1]
        self.avater_s = filename[2]

        db.session.commit()


    def authIn(self):
        self.confirmed=True

    def authOut(self):
        self.confirmed=False

    @staticmethod
    def get_user(id):
        user = User.query.filter(User.id == id).first()
        return user




    @staticmethod
    def read_all():
        return User.query.all()

    # add a new Pet
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.user_id = self.id
        else:
            raise Exception()
        db.session.add(pet)
        db.session.commit()

    def get_jwt_token(self, expires_in=6000):
        """get JWT token"""
        token = jwt.encode({'reset_password': self.id, 'exp': time() + expires_in},
                           current_app.config['SECRET_KEY'],
                           algorithm='HS256').decode('utf8')

        print(token)
        return token

    @staticmethod
    def verify_jwt_token(token):
        try:
            user_id = jwt.decode(token,
                                 current_app.config['SECRET_KEY'],
                                 algorithms='HS256')['reset_password']
        except Exception as e:
            print(e)
            return
        return User.query.get(user_id)


    def __repr__(self):
        return '{}'.format(self.username)


