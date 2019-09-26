from flask import render_template, redirect, url_for
from application import app, db
from application.models import Exercises
from application.forms import EditForm


@app.route('/home')
@app.route('/')
def home():
	return render_template('home.html', title="Home")


@app.route('/exercises')
def exercises():
	exerciseData = Exercises.query.all()
	return render_template('exercises.html', title='Exercises', exercises=exerciseData)


@app.route('/login')
def login():
	return render_template('login.html', title='Login')


@app.route('/register')
def register():
	return render_template('register.html', title='Register')


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