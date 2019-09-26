from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Exercises, Users
from application.forms import EditForm, RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required



@app.route('/home')
@app.route('/')
def home():
	return render_template('home.html', title="Home")


@app.route('/exercises')
def exercises():
	exerciseData = Exercises.query.all()
	return render_template('exercises.html', title='Exercises', exercises=exerciseData)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = Users.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user,remember=form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				return redirect(url_for('home'))
	return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_pw = bcrypt.generate_password_hash(form.password.data)
		user = Users(email=form.email.data, password=hashed_pw)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('exercises'))
	return render_template('register.html', title='Register', form=form)


@app.route('/edits', methods=['GET','POST'])
def edits():
	form = EditForm()
	if form.validate_on_submit():
		editsData = Exercises(
				exercise_name=form.exercise_name.data,
				muscle_group=form.muscle_group.data,
				description=form.description.data
			)
		db.session.add(editsData)
		db.session.commit()
		return redirect(url_for('home'))
	else:
		print(form.errors)
	return render_template('edits.html', title='Edits', form=form)