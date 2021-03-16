from flask import Blueprint, render_template, session, flash, redirect,request,url_for
from src.Utility import reservation_list
from src.Models.Users import User
from src.Models.Reservations import Reservation
from src import Pet
from src.Utility.utilize import current_user

admin=Blueprint('admin',__name__)


@admin.route("/petcenter", methods=['GET', 'POST'])
def index():
    if not session.get("USERNAME") is None:
        if not current_user().isAdmin():
            return redirect(url_for('auth.index'))
        user =current_user()
        # reservations=Reservation.read_all()
        # return render_template("admin/index.html",reservations=reservations,user=user)
        state_list = []
        if request.form.getlist("state_list[]") is not None and request.form.getlist("state_list[]") != []:
            state_list = request.form.getlist("state_list[]")
            print(state_list)
            Reservation.update_state(state_list)
        all_reservations = Reservation.read_all()
        r = request.args.get("r")
        if request.form.getlist("id_list[]") is not None and request.form.getlist("id_list[]") != []:
            reservation_list.update_list(request.form.getlist("id_list[]"))
        # print(reservation_list.get_list())
        if r:
            r = int(r)
            for res in all_reservations:
                if r == res.id:
                    Reservation.remove_res(r)
        all_reservations = Reservation.read_all_unfinished()
        for res in all_reservations:
            Reservation.set_user_pet_name(res, User.get_user(res.user_id), Pet.get_pet(res.pet_id))
            Reservation.set_createTime(res)
        # print(all_reservations)
        # return render_template('reservation/show.html', reservations=all_reservations)
        # return render_template('admin/index.html', reservations=all_reservations, list=reservation_list.get_list())
        return render_template('admin/index.html', reservations=all_reservations, list=reservation_list.get_list(),user = user)
    else:
        flash("User needs to either login or sign up first")
        return redirect(url_for('auth.login'))

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
#     all_reservations = Reservation.read_all()
#     for res in all_reservations:
#         Reservation.set_user_pet_name(res, User.get_user(res.user_id), Pet.get_pet(res.pet_id))
#         Reservation.set_createTime(res)
#     # print(all_reservations)
#     # return render_template('reservation/show.html', reservations=all_reservations)
#     return render_template('reservation/show.html', reservations=all_reservations, list=reservation_list.get_list())
