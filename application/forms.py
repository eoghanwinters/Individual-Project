from flask_wtf import FlaskForm
from flask_login import current_user
from application.models import Users
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

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
			('6', 6)
		])

	numbers=[]
	for i in range(45):
		temp = [i+1, i+1]
		numbers.append(temp)


	reps = SelectField('Reps: ',
		choices=numbers)

	description = StringField('Description: ',
		validators=[
			DataRequired(),
			Length(max=100000)
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
	
	numbers=[]
	for i in range(45):
		temp = [i+1, i+1]
		numbers.append(temp)


	reps = SelectField('Reps: ',
		choices=numbers)

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