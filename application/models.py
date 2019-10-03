from application import db, login_manager
from flask_login import UserMixin

class Exercises(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	exercise_name = db.Column(db.String(50), nullable=False)
	sets = db.Column(db.Integer, nullable=False)
	reps = db.Column(db.Integer, nullable=False)
	muscle_group = db.Column(db.String(50), nullable=False)
	description = db.Column(db.String(100000), nullable=False)
	image = db.Column(db.String(20))
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


	def __repr__(self):
		return ''.join(['Exercise Name: ', self.exercise_name, '\r\n', 
						'Muscle Group: ', self.muscle_group, '\r\n',
						'Sets: ', self.sets, '\r\n',
						'Reps: ', self.reps, '\r\n',
						'Description: ', self.description, '\r\n'])


class Users(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(20), nullable=False)
	last_name = db.Column(db.String(20), nullable=False)
	email = db.Column(db.String(150), nullable=False, unique=True)
	password = db.Column(db.String(50), nullable=False)
	exercises = db.relationship('Exercises', backref='author', lazy=True)

	def __repr__(self):
		return ''.join(['User ID: ', str(self.id), '\r\n', 
			'Email: ', self.email, '\r\n',
			'Name: ', self.first_name, ' ', self.last_name])


@login_manager.user_loader
def load_user(id):
	return Users.query.get(int(id))

