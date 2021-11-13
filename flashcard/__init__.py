from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '385c9dfa12c167b6c4bcb7be8004bba0'
db = SQLAlchemy(app)

from flashcard import routes
