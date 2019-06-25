from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddOwner(FlaskForm):

	name=StringField("Name of the Owner:")
	pup_id=IntegerField("Id of the puppy:")
	submit=SubmitField('AddOwner')