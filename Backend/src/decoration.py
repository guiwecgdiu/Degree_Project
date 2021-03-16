from flask import session, redirect, flash
import functools

def loginAuth(func):
    def inner(*args,**kwargs):
        if not session.get("USERNAME") is None:
            func(*args,**kwargs)
        else:
            flash("User needs to either login or sign up first")
            return redirect('login')
    return inner