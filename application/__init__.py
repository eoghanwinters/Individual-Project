from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '7218a9143c27c16610765205alb21cb7'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from application import routes
