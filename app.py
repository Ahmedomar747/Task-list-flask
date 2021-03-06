from flask import Flask, render_template as render
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'abcd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)