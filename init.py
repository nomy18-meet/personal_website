from app import UserInfo, Recipe
import datetime
from flask import Flask, Response, render_template, request, redirect
# SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
#flask setup
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"

db = SQLAlchemy(app)




thisname="nomy"
thispassword="123"
thisgender="woman"

user= UserInfo(name=thisname,password=thispassword, email=thisgender)

db.session.add(user)
db.session.commit()

Rname="r"
Rcontent="content"
RuserId=session.query(UserInfo).first()
Rpic="tt"

ruser= Recipe(name=Rname,content=Rcontent, userid=ruserId, pic=Rpic)
db.session.add(user)
db.session.commit()