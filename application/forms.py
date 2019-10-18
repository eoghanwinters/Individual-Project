from flask_wtf import FlaskForm
from flask_login import current_user
from application.models import Users
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed

class EditForm(FlaskForm):
	
	exercise_name = StringField('Exercise: ',
		validators=[
			DataRequired(),
			Length(max=50)
		])
	
	muscle_group = SelectField('Muscle Group: ',
		choices=[
			('Legs', 'Legs'),
			('Chest', 'Chest'),
			('Back', 'Back'),
			('Shoulders', 'Shoulders'),
			('Arms', 'Arms'),
			('Core', 'Core')
		])
	
	sets = SelectField('Sets: ',
		choices=[
			('1', 1),
			('2', 2),
			('3', 3),
			('4', 4),
			('5', 5),
			('6', 6),
			('7', 7),
			('8', 8)
		])

	reps = SelectField('Reps: ',
		choices=[
			('1', 1),
			('2', 2),
			('3', 3),
			('4', 4),
			('5', 5),
			('6', 6),
			('7', 7),
			('8', 8),
			('9', 9),
			('10', 10),
			('11', 11),
			('12', 12),
			('13', 13),
			('14', 14),
			('15', 15)
		])
	description = StringField('Description: ',
		validators=[
			DataRequired(),
			Length(max=100000)
		])
	picture = FileField('Add picture',
		validators=[
			FileAllowed(['jpg','png'])
		])
	submit = SubmitField('Add Exercise')


class SearchForm(FlaskForm):
	muscle_group = SelectField('Muscle Group: ',
		choices=[
			('All', 'All'),
			('Legs', 'Legs'),
			('Chest', 'Chest'),
			('Back', 'Back'),
			('Shoulders', 'Shoulders'),
			('Arms', 'Arms'),
			('Core', 'Core')

		])
	submit = SubmitField('Search')

class UpdateExerciseForm(FlaskForm):
	sets = SelectField('Sets: ',
		choices=[
			('1', 1),
			('2', 2),
			('3', 3),
			('4', 4),
			('5', 5),
			('6', 6)
		])
	reps = SelectField('Reps: ',
		choices=[
			('1', 1),
			('2', 2),
			('3', 3),
			('4', 4),
			('5', 5),
			('6', 6),
			('7', 7),
			('8', 8),
			('9', 9),
			('10', 10),
			('11', 11),
			('12', 12),
			('13', 13),
			('14', 14),
			('15', 15)
		])
	description = StringField('Description: ',
		validators=[
			DataRequired(),
			Length(max=100000)
		])
	submit = SubmitField('Update')


class RegistrationForm(FlaskForm):
	first_name = StringField('First Name: ',
		validators=[
			DataRequired(),
			Length(max=30)
		])
	last_name = StringField('Last Name: ',
		validators=[
			DataRequired(),
			Length(max=30)
		])
	email = StringField('Email: ',
		validators=[
			DataRequired(),
			Email()
		])
	password = PasswordField('Password: ',
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


class LoginForm(FlaskForm):
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		])
	password = PasswordField('Password',
		validators=[
			DataRequired()
		])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
	first_name = StringField('First Name: ',
		validators=[
			DataRequired(),
			Length(max=30)
		])
	last_name = StringField('Last Name: ',
		validators=[
			DataRequired(),
			Length(max=30)
		])
	email = StringField('Email: ',
		validators=[
			DataRequired(),
			Email()
		])
	submit = SubmitField('Update')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = Users.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('Email already in use! Please choose another!')