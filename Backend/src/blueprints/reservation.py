from flask import Blueprint, render_template, request
from src.Utility import reservation_list
from src.Models.Users import User
from src.Models.Pets import Pet
from src.forms import LoginForm, SignupForm, PetForm, ResetPasswordForm, ProfileForm, AddReservation, EditReservation, \
    AddReservationForm
from flask import session, render_template, redirect, request, flash, url_for
from src.extension import db
from src.Models.Reservations import Reservation
from datetime import datetime

reservation = Blueprint('reservation', __name__, template_folder="/template/reservation",
                        static_folder='static/example', url_prefix='/reservation')


@reservation.route('/index')
def index():
    return render_template('reservation/add.html')


# @reservation.route('/show', methods=['GET', 'POST'])
# def show():
#     state_list = []
#     if request.form.getlist("state_list[]") is not None and request.form.getlist("state_list[]") != []:
#         state_list = request.form.getlist("state_list[]")
#         print(state_list)
#         Reservation.update_state(state_list)
#     all_reservations = Reservation.read_all()
#     r = request.args.get("r")
#     if request.form.getlist("id_list[]") is not None and request.form.getlist("id_list[]") != []:
#         reservation_list.update_list(request.form.getlist("id_list[]"))
#     # print(reservation_list.get_list())
#     if r:
#         r = int(r)
#         for res in all_reservations:
#             if r == res.id:
#                 Reservation.remove_res(r)
#     all_reservations = Reservation.read_all_unfinished()
#     for res in all_reservations:
#         Reservation.set_user_pet_name(res, User.get_user(res.user_id), Pet.get_pet(res.pet_id))
#         Reservation.set_createTime(res)
#     # print(all_reservations)
#     # return render_template('reservation/show.html', reservations=all_reservations)
#     return render_template('reservation/show.html', reservations=all_reservations, list=reservation_list.get_list())


# else:
#     flash("User needs to either login or signup first")
#     return redirect(url_for('login'))
# lookup reservatiok


@reservation.route('/list', methods=['GET', 'POST'])
def list():
    if not session.get("USERNAME") is None:
        user_in_db = User.query.filter(User.username == session["USERNAME"]).first()
        all_reservations = Reservation.read_all()
        r = request.args.get("r")
        if r:
            r = int(r)
            for res in all_reservations:
                if r == res.id:
                    Reservation.remove_res(r)

        if request.form.getlist("res[]") is not None and request.form.getlist("res[]") != []:
            # print("GET")
            add_res = request.form.getlist("res[]")
            pet = Pet.query.filter(Pet.id == int(add_res[0])).first()
            print("add_res" + str(add_res))
            Reservation.add_res(user_in_db, pet, add_res[1], add_res[2], "surgery confirmed")
        if request.form.getlist("edit_res[]") is not None and request.form.getlist("edit_res[]") != []:
            edit_res = request.form.getlist("edit_res[]")
            pet = Pet.query.filter(Pet.id == int(edit_res[1])).first()
            print("edit_res: " + str(edit_res))
            Reservation.update_res(int(edit_res[0]), pet, edit_res[2], edit_res[3])
        if request.form.get('finish_id') is not None:
            finish_id=request.form.get('finish_id')
            print("finish_id: "+finish_id)
            Reservation.res_finish(int(finish_id))
            reservation_list.delete_res(finish_id)

        # print("username:"+str(user_in_db))
        reservation = Reservation.get_user_res_unfinished(user_in_db.id)
        print("reservation: " + str(reservation))
        pet = Reservation.get_available_pet(Pet.get_user_pet(user_in_db.id))
        # print("pet:"+str(pet))
        for res in reservation:
            Reservation.set_user_pet_name(res, User.get_user(res.user_id), Pet.get_pet(res.pet_id))
            Reservation.set_createTime(res)

        now = datetime.now().date()
        # print(now)
        daily_order = 0
        all = Reservation.read_all()
        order_number = all.__len__()
        pending = 0
        for rese in all:
            if rese.timestamp.date() == now:
                daily_order += 1
            if rese.state != 'finished':
                pending += 1
        animals = Pet.read_all().__len__()
        head_list = [daily_order, animals, order_number, pending]
        print(head_list)

        # today_res=

        return render_template('reservation/add.html', reservations=reservation, user=user_in_db, pets=pet,head_list=head_list)
    else:
        flash("User needs to either login or signup first")
        return redirect(url_for('login'))
