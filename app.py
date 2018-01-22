# flask imports
from flask import Flask, Response, render_template, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
# from flask.ext.heroku import Heroku
app = Flask(__name__)
# heroku = Heroku(app)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test,db'

class UserInfo(db.Model):

	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120))
	password = db.Column(db.String(120))
	gender= db.Column(db.String(120))
 	
	def __init__(self,name,password,gender):
		self.name=name
		self.password=password
		self.gender=gender


	def check_pass(self, psw):
		return psw==self.password

	def __repr__(self):
		return "<User(name='%s', gender='%s', password='%s')>" % (
	                self.name, self.gender, self.password)

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

@app.route('/') #this is the login page
def login():
	return render_template("login.html")

@app.route ('/signin')
def signin():
	return render_template("signin.html")

@app.route('/home')
@app.route('/home')
def home():
	
	print("123")
	return render_template("home.html")


@app.route("/recipepost")
def recipepost():
	print("1234")
	return render_template("recipepost.html")


if __name__ == '__main__':
	app.run(debug=True)


@app.route('/profile/<name>')
def profile(name):
	return render_template("login.html",name=name)


# @app.route('/tuna',methods=["GET","POST"])
# def tuna():
# 	if request.method == "POST":
# 		return "you are using post"
# 	else:
# 		return "u r probablu usin get"

# @app.route("/profile/<username>")
# def profile(username):
# 	return "<h2>hey there %s</h2>" % username

# @app.route('/post/<int:post_id>')
# def post (post_id):
# 	return "<h2>post id is %s</h2>" % post_id




# '''@app.route('/home')
# # flask setup
# app = Flask(__name__)
# app.config["SECRET_KEY"] = "ITSASECRET"

# # flask-login imports
# from flask_login import login_required, current_user
# from login import login_manager, login_handler, logout_handler
# login_manager.init_app(app)

# # SQLAlchemy
# from model import Base, Recipe, User
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# engine = create_engine('sqlite:///project.db')
# Base.metadata.bind = engine
# DBSession = sessionmaker(bind=engine)
# session = DBSession()

# # we need this library for HTML-safe string operations
# import cgi


# @app.route('/')
# def test_login():
# 	return render_template('home.html')



# @app.route('/post/<int:post_id>')
# def post_recipe(post_id):
# 		recipe = session.query(Recipe).filter_by(id = post_id).first()
# 		return render_template('post.html', recipe = recipe)'''



# @app.route('/countries/<string:country>')
# def country_page(country):
# 	recipes = session.query(Recipe).filter_by(country=country).all()
# 	return render_template('country.html', recipes=recip

# @app.route('/signup')
# def signup_page():
# 	return render_template('signup.html')


# @app.route('/home/recipepost')
# 	return render_template('recipepost.html')

# @app.route("/home", method=['GET'])
# def home():
  
#     return render_template("home.html")

#     if __name__ == '__main__':
#        app.run()

# @app.route('/login',method=["GET"])
# 	def login:
