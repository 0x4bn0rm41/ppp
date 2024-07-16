from main import app, db
from flask import render_template, make_response, request, url_for, session, g
from models import Note
import datetime
# from functools import wraps, update_wrapper
from decorators import nocache

@app.route("/", methods=['POST', 'GET', "DELETE"])
@nocache
def index():
	notes = Note.query.all() 
	
	if request.method == "POST":
		json_data = request.json
		print(json_data)
		if(json_data['id'] is None):
			n = Note(json_data['content'], datetime.date.today())
			db.session.add(n)
			print(f'\033[32m added | {len(notes)}  \033[0m')
			db.session.commit()
			# return render_template('index.html', Notes = notes if len(notes) > 0 else None)
		else:
			n = Note.query.filter_by(id = json_data['id']).first()
			n.content = json_data['content']
			# n.change = datetime.today().date()
			db.session.commit() 

	if request.method == "DELETE":
		json_data = request.json
		print(json_data)
		n = Note.query.filter_by(id=json_data['id']).first()
		db.session.delete(n)
		db.session.commit()


	return render_template('index.html', Notes = notes if len(notes) > 0 else None, count = len(notes))