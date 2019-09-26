from application import db

class Exercises(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	exercise_name = db.Column(db.String(50), nullable=False)
	muscle_group = db.Column(db.String(50), nullable=False)
	description = db.Column(db.String(100000), nullable=False)

	def __repr__(self):
		return ''.join(['Exercise Name: ', self.exercise_name, '\r\n', 
						'Muscle Group: ', self.muscle_group, '\r\n',
						'Description: ', self.description])