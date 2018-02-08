import datetime
from flask import Flask, Response, render_template, request, redirect
# SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
#flask setup
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"

db = SQLAlchemy(app)
db.create_all()

class UserInfo(db.Model):

	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120))
	password = db.Column(db.String(120))
	email= db.Column(db.String(120))
 	
	def __init__(self,name,password,email):
		self.name=name
		self.password=password
		self.email=email


	def check_pass(self, psw):
		return psw==self.password

	def __repr__(self):
		return "<User(name='%s', email='%s', password='%s')>" % (
	                self.name, self.email, self.password)

class Recipe(db.Model):
	__tablename__ = 'Recipes'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120))
	content= db.Column(db.String(120))
	userId= db.Column(db.Integer)
	pic=db.Column(db.String)

	def __init__(self,name,content,userId,pic=None):
		self.name=name
		self.content=content
		self.userId=userId
		self.pic=pic


	def __repr__(self):
	    return "<User(name='%s', content='%s', userId='%i'), pic='%s'>" % (
	                       self.name, self.content, self.userId, self.pic)



db.create_all()

@app.route('/', methods=["GET", "POST"]) #this is the login page
def login():
	if (request.method == 'GET'):
		return render_template("login.html")
	username = request.form['uname']
	print(username)
	password = request.form['psw']
	user = db.session.query(UserInfo).filter_by(name= username).first()
	if user == None or user.password != password:
		print("if")
		return render_template('login.html', error = True)
	else:
		print("else")
		return render_template ("home.html") 


@app.route('/home')
def home():
	recipes = db.session.query(Recipe).all()
	return render_template("home.html", recipes=recipes)


@app.route('/recipepost',methods= ["POST","GET"])
def recipepost():
	if (request.method== 'GET'):
		return render_template("recipepost.html")
	else:
		postR=Recipe(name=request.form('Rname'),content=request.form('content'), pic=request.form('pic'))
		return render_template("home.html")

@app.route('/signin', methods=["POST", "GET"])
def signin():
	if (request.method== 'GET'):
		return render_template("signin.html")
	else:


		user=UserInfo(name=request.form['name'], password=request.form['psw'], email=request.form['email'])
		db.session.add(user)
		db.session.commit()
		return render_template("home.html")

@app.route('/quotes')
def quotes():
	return render_template("quotes.html")

if __name__ == '__main__':
	app.run(debug=True)

