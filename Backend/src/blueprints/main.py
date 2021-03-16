from flask import Blueprint, session, render_template, flash, redirect, url_for, request, jsonify, send_from_directory
from src.forms import SignupForm, LoginForm, ResetPasswordForm, ResetPasswordRequestForm, PetForm,EditProfileForm
from flask_dropzone import random_filename
from src.Models.Users import Pet, Reservation
from src.extension import db
import os
from flask import current_app
from src.Utility.utilize import current_user,resize_image
main=Blueprint('main',__name__,url_prefix="/main")




@main.route('/upload', methods=['POST', 'GET'])
def upload():

    if not session.get("USERNAME") is None:
        global filename
        global filename_m
        global isPictured
        filename=None
        filename=None
        isPictured =False
        if request.method == 'POST' and 'file' in request.files:

            f = request.files.get('file')
            print("NO1")
            filename = random_filename(f.filename)
            f.save(os.path.join(current_app.config['PET_UPLOAD_PATH'], filename))
            filename_m=resize_image(f,filename,current_app.config['PHOTO_SIZE']['medium'])
            isPictured=True

        if request.form.getlist("pet[]") is not None and request.form.getlist("pet[]") != []:
            pet=request.form.getlist("pet[]")
            type = pet[0]
            if filename_m is None:
                print()
                if pet[0] == 'cat':
                    filename_m='cat'
                else:
                    filename_m = 'dog'
            Pet.add_pet(pet[1],pet[2],pet[0],current_user(),filename_m)
            filename_m = None
            filename =None
            return redirect(url_for('.index'))
        return render_template('main/treatPet.html', title='TreatPet')
    else:
        flash("User needs to either login or sign up first")
        return redirect(url_for('auth.login'))

@main.route("/")
@main.route("/index")
def index():
    if not session.get("USERNAME") is None:
        current = current_user()
        pets = Pet.get_user_pet(current.id)
        dicty = Reservation.get_pet_res(pets)
        return render_template("main/mypets.html", user=current, pets=pets, dicts=dicty)
    else:
        flash("User needs to either login or sign up first")
        return redirect(url_for('auth.login'))

@main.route('/EditInfo',methods=['POST','GET'])
def edit_form():
    form = EditProfileForm()
    if not session.get("USERNAME") is None:
        if form.validate_on_submit():
            user = current_user()
            user.bio=form.bio.data
            user.name=form.name.data
            user.location=form.location.data
            db.session.commit()
            print("hello")
            return redirect(url_for('main.index'))
        return render_template('main/edit_user.html',form=form)
    else:
        flash("User needs to either login or sign up first")
        return redirect(url_for('auth.login'))


@main.route('/avatars/<filename>')
def get_avatar(filename):
    return send_from_directory(current_app.config['AVATARS_SAVE_PATH'],filename)

@main.route('/pet/<filename>')
def get_pet_image(filename):
    if filename == 'dog':
        return send_from_directory(current_app.config['PET_DEFAULT_PATH'],filename+'.jpg')
    elif filename == 'cat':
        return send_from_directory(current_app.config['PET_DEFAULT_PATH'],filename+'.jpg')
    else:
        return send_from_directory(current_app.config['PET_UPLOAD_PATH'],filename)
#
# def get_default_image():
#     return current_app.config['PET_DEFAULT_PATH'],"dog.jpg"
#


