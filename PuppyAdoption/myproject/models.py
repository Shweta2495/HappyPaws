from myproject import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return Users.query.get(user_id)

class Puppy(db.Model):

	__tablename__='puppies'

	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.Text)
	owner=db.relationship('Owner',backref='puppy',uselist=False)

	def __init__(self,name):
		self.name=name 

	def __repr__(self):
		if self.owner:
			return f"Puppy name is {self.name} and id is {self.id} and owner is {self.owner.name}"
		else:
			return f"Puppy name is {self.name} and id is {self.id} and no owner is assigned yet!"


class Owner(db.Model):

	__tablename__='owners'
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.Text)
	puppy_id=db.Column(db.Integer,db.ForeignKey('puppies.id'))
	
	def __init__(self,name,puppy_id):
		self.name=name
		self.puppy_id=puppy_id
	def __repr__(self):
		return "Owner name:{self.name}"


class Users(db.Model,UserMixin):

	__tablename__='users'
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(64),unique=True,index=True)
	email=db.Column(db.String(64),unique=True,index=True)
	password_hash=db.Column(db.String(128))
	#confirm_password_hash=db.Column(db.String(128))

	def __init__(self,username,email,password):
		self.username=username
		self.email=email
		self.password_hash=generate_password_hash(password)
		#self.confirm=confirm

	def check_password(self,password):
		return check_password_hash(self.password_hash,password)

	def __repr__(self):
		return "Registered UserName:{self.username}"


class Login(db.Model):

	__tablename__='login'
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.Text)
	password=db.Column(db.Text)

	def __init__(self,username,password):
		self.username=username
		self.password=password

	def __repr__(self):
		return "Login UserName:{self.username}"
