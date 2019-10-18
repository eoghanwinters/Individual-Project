from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Exercises, Users
from application.forms import EditForm, RegistrationForm, LoginForm, UpdateAccountForm, UpdateExerciseForm, SearchForm
from flask_login import login_user, current_user, logout_user, login_required, LoginManager
import os


@app.route('/home')
@app.route('/')
def home():
	return render_template('home.html', title="Home")


def save_picture(form_picture):
	picture_path = os.path.join(app.root_path, 'static/picture_uploads', form_picture.filename)
	picture = form_picture.filename
	form_picture.save(picture_path)
	return picture


@app.route('/exercises/<int:user_id>', methods=['POST', 'GET'])
@login_required
def exercises(user_id):
	exercises = Exercises.query.filter_by(user_id=user_id)
	if current_user.id != user_id:
		return redirect(url_for('home'))
	else:
		user = Users.query.get_or_404(user_id)
		exerciseData = Exercises.query.filter_by(user_id=user_id)
	form = SearchForm()
	if request.method == 'POST' and form.muscle_group.data == 'All':
		try:
			return redirect(url_for('exercises', user_id=current_user.id))
		except:
			return "This is not working!"
	elif request.method == 'POST':
		try:
			exerciseData = Exercises.query.filter_by(muscle_group=form.muscle_group.data, user_id=current_user.id).all()
		except:
			return "This is not working!"
	
	return render_template('exercises.html', title='Exercises', exercises=exerciseData, form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home', user_id=current_user.id))
	form = LoginForm()
	if form.validate_on_submit():
		user = Users.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user,remember=form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				return redirect(url_for('exercises', user_id=current_user.id))
	return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if current_user.is_authenticated:
		return redirect(url_for('login'))
	if form.validate_on_submit():
		hashed_pw = bcrypt.generate_password_hash(form.password.data)
		user = Users(
			first_name=form.first_name.data,
			last_name=form.last_name.data,
			email=form.email.data, 
			password=hashed_pw
			)
		db.session.add(user)
		db.session.commit()
		login_user(user)
		return redirect(url_for('exercises', user_id=current_user.id))
	return render_template('register.html', title='Register', form=form)


@app.route('/edits', methods=['GET','POST'])
@login_required
def edits():
	form = EditForm()
	image = url_for('static', filename='default.jpg')
	if form.validate_on_submit():
		if form.picture.data:
			picture_path = save_picture(form.picture.data)
			full_path = '/static/picture_uploads/' + picture_path
			editsData = Exercises(
					exercise_name=form.exercise_name.data,
					muscle_group=form.muscle_group.data,
					sets=form.sets.data,
					reps=form.reps.data,
					description=form.description.data,
					author=current_user,
					image=full_path
				)
			db.session.add(editsData)
			db.session.commit()
			image = url_for('static', filename=picture_path)
			return redirect(url_for('exercises', user_id=current_user.id))
		else:
			editsData = Exercises(
						exercise_name=form.exercise_name.data,
						muscle_group=form.muscle_group.data,
						sets=form.sets.data,
						reps=form.reps.data,
						description=form.description.data,
						author=current_user,
						image='/static/picture_uploads/default.jpg'
					)
			db.session.add(editsData)
			db.session.commit()
			return redirect(url_for('exercises', user_id=current_user.id))
	else:
		print(form.errors)
		
	return render_template('edits.html', title='Edits', form=form)


@app.route('/account', methods=['GET','POST'])
@login_required
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.email = form.email.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
		form.email.data = current_user.email
	return render_template('account.html', title='Account', form=form)


@app.route('/delete/<int:id>')
def delete(id):
	exercise_to_delete = Exercises.query.get_or_404(id)
	try:
		db.session.delete(exercise_to_delete)
		db.session.commit()
		return redirect(url_for('exercises', user_id=current_user.id))
	except:
		return 'There was a problem deleting that exercise!'


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
	form = UpdateExerciseForm()
	exercise = Exercises.query.get_or_404(id)
	if request.method == 'POST':
		exercise.sets = request.form['sets']
		exercise.reps = request.form['reps']
		exercise.description = request.form['description']
		try:
			db.session.commit()
			return redirect(url_for('exercises', user_id=current_user.id))
		except:
			return 'There was a problem updating that exercise!'
	else:
		return render_template('update.html', form=form, exercise=exercise)


@app.route('/user/delete/<int:user_id>', methods=['GET', 'POST'])
@login_required
def delete_user(user_id):
	user = Users.query.get_or_404(user_id)
	exercise = Exercises.query.filter_by(user_id=user_id).all()
	if user:
		db.session.delete(user)
		for i in exercise:
			db.session.delete(i)
		db.session.commit()
		return redirect(url_for('logout'))
	else:
		return 'Error!'

