from src.Models.Users import User
from flask import session,current_app
import os
from PIL import Image

def current_user():
    user =None
    user=User.query.filter_by(username=session["USERNAME"]).first()
    return user



def resize_image(image, filname, base_width):
    filname, ext=os.path.splitext(filname)
    img=Image.open(image)
    if img.size[0] <= base_width:
        return filname + ext
    w_percent =(base_width/float(img.size[0]))
    h_size=int((float(img.size[1]))*float(w_percent))
    img=img.resize((base_width,h_size),Image.ANTIALIAS)

    filname += current_app.config["PHOTO_SUFFIX"][base_width]+ext
    img.save(os.path.join(current_app.config['PET_UPLOAD_PATH'],filname),optimize=True,quality=85)
    return filname

def registeredAdmin():
    admins = User.query.all()
    count =0
    for admin in admins:
        if admin.isAdmin:
            count +=1
    return count
