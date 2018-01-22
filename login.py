from flask import redirect, url_for, render_template
from flask_login import LoginManager, login_user, logout_user

import sys

import cgitb

cgitb.enable();

from model import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

login_manager = LoginManager()

@app.route()
@login_manager.user_loader
def load_user(user_id):
    user = session.query(UserInfo).filter_by(id=user_id)
    if user.count() == 0:
        return
    return user.first()


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'


def login_handler(request):
    if request.method == 'GET':
        return render_template('login.html')

    name = request.form.get('uname')
    psw    = request.form.get('psw')
    user  = session.query(UserInfo).filter_by(name=name) 

    for u in user:
        if u.check_pass(u, psw):
            user=u
            login_user(user)
            return redirect(url_for("protected"))
        return "wrong password!"

    redirect('fuck.html')
    return "bad login"

def logout_handler():
    logout_user()
    return 'Logged out'