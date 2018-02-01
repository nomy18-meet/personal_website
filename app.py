import datetime
from flask import Flask, Response, render_template, request, redirect
# SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
# flask setup
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"

db = SQLAlchemy(app)
# class UserInfo(db.Model):

# 	__tablename__ = 'users'
# 	id = db.Column(db.Integer, primary_key=True)
# 	name = db.Column(db.String(120))
# 	password = db.Column(db.String(120))
# 	gender= db.Column(db.String(120))
 	
# 	def __init__(self,name,password,gender):
# 		self.name=name
# 		self.password=password
# 		self.gender=gender


# 	def check_pass(self, psw):
# 		return psw==self.password

# 	def __repr__(self):
# 		return "<User(name='%s', gender='%s', password='%s')>" % (
# 	                self.name, self.gender, self.password)

# class Recipe(db.Model):
# 	__tablename__ = 'Recipes'

# 	id = db.Column(db.Integer, primary_key=True)
# 	name = db.Column(db.String(120))
# 	content= db.Column(db.String(120))
# 	userId= db.Column(db.Integer)
# 	pic=db.Column(db.String)

# 	def __init__(self,name,content,userId,pic=None):
# 		self.name=name
# 		self.content=content
# 		self.userId=userId
# 		self.pic=pic


# 	def __repr__(self):
# 	    return "<User(name='%s', content='%s', userId='%i'), pic='%s'>" % (
# 	                       self.name, self.content, self.userId, self.pic)



# # db.create_all()


@app.route('/', methods=["GET"]) #this is the login page
def login():
	if (request.method == 'GET'):
		username = request.form['uname']
		password = request.form['psw']
		user = session.query(name).filter_by(name= uname).first()
		if user == None or user.password != password:
			return render_template('login.html', error = True)

	return render_template("login.html")

@app.route ('/signin')
def signin():
	return render_template("signin.html")

@app.route('/home')
def home():
	print("123")
	return render_template("home.html")


@app.route("/recipepost")
def recipepost():
	print("1234")
	return render_template("recipepost.html")



@app.route('/profile/<name>')
def profile(name):
	return render_template("login.html",name=name)

if __name__ == '__main__':
	app.run(debug=True)

