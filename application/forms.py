from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class EditForm(FlaskForm):
	exercise_name = StringField('Exercise: ',
		validators=[
			DataRequired(),
			Length(max=50)
		])
	muscle_group = StringField('Muscle Group: ',
		validators=[
			DataRequired(),
			Length(max=50)
		])
	description = StringField('Description: ',
		validators=[
			DataRequired(),
			Length(max=100000)
		])
	submit = SubmitField('Add Exercise')