from src.Models.Users import User
from flask import session

def current_user():
    user =None
    user=User.query.filter_by(username=session["USERNAME"]).first()
    return user

