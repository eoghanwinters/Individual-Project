from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
	return render_template('home.html', title="Home")

@app.route('/about')
def about():
	return render_template('about.html', title='About')