from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError

class LoginForm(FlaskForm):

	username=StringField("UserName:",validators=[DataRequired()])
	password=PasswordField("Enter Password:",validators=[DataRequired()])
	submit=SubmitField('Login')