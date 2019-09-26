from flask import render_template
from application import app


@app.route('/home')
@app.route('/')
def home():
	return render_template('home.html', title="Home")

@app.route('/exercises')
def about():
	return render_template('exercises.html', title='Exercises')