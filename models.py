from main import db
import datetime

class Note(db.Model):
	__tablename__ = 'Note'
	id = db.Column(db.Integer, primary_key = True, autoincrement=True)
	creation_date = db.Column(db.Date, default=datetime.date.today())
	change_date = db.Column(db.Date, default=datetime.date.today())
	content = db.Column(db.String(2048))

	def __init__(self, content, change_date):
	# def __init__(self, creation_date, content):
		self.change_date = change_date
		self.content = content

class User(db.Model):
	tablename__ = 'Users'

	id = db.Column(db.Integer, primary_key = True, autoincrement=True)
	login = db.Column(db.String(32))
	password = db.Column(db.String(32))

# class Session(db.Model):
# 	 user_id = 0
# 	 session_id = 0