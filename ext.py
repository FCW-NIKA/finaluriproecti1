from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = ""
app.config["SQLALCHEMY_DATABASE_URI"] = ""

db = SQLAlchemy(app)
login_manager = LoginManager(app)

login_manager.login_view = "login"