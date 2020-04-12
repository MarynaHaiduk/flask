from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'X\x18#L\xeb\xda\xe6nc\x19\xfdU_?\x02\xd4\xbf\xda\xd9\x8b0\x1e?\x8d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskAPP import routes

