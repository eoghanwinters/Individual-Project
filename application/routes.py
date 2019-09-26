from flask import render_template
from application import app


@app.route('/home')
@app.route('/')
def home():
	return render_template('home.html', title="Home")

@app.route('/exercises')
def exercises():
	return render_template('exercises.html', title='Exercises')

@app.route('/login')
def login():
	return render_template('login.html', title='Login')

@app.route('/register')
def register():
	return render_template('register.html', title='Register')