from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config 
from pathlib import Path

db = SQLAlchemy()
app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)


with app.app_context():
	if(Path(Path(__file__).parent/ 'app.db').exists() != True):
		from models import *
		db.create_all()



from routes import *




if __name__ == "__main__":
	# app.run()
	app.run(debug=True)
	print(Path(__file__))
