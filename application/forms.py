from flask_wtf import FlaskForm
from application.models import Users
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

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


class RegistrationForm(FlaskForm):
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		])
	password = PasswordField('Password',
		validators=[
			DataRequired()
		])
	confirm_password = PasswordField('Confirm Password',
		validators=[
			DataRequired(),
			EqualTo('password')
		])
	submit = SubmitField('Sign Up')

	def validate_email(self, email):
		user = Users.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email already in use!')