from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError 

class RegisterForm(FlaskForm):

	username=StringField("UserName:",validators=[DataRequired()])
	email=StringField("Email Id:",validators=[DataRequired(),Email()])
	password=PasswordField("Enter Password:",validators=[DataRequired(),EqualTo('confirm',message='Passwords must match!')])
	confirm=PasswordField("Confirm Password:",validators=[DataRequired()])
	submit=SubmitField('Register')

	def check_email(self,field):
		if Users.query.filter_by(email=field.data).first():
			raise ValidationError('Email already Registered!')

	def check_username(self,field):
		if Users.query.filter_by(username=field.data).first():
			raise ValidationError('UserName already exists!')