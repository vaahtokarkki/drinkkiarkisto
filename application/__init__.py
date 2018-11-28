from flask import Flask
import os
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///drinkarchive.db"    
    app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app,session_options={"autoflush": False}) #autoflush kanssa ongelmia kun monesta-moneen yhteyksiä

from application import views

from application.drinks import models
from application.drinks import views

from application.ingredients import models
from application.ingredients import views

from application.keywords import models
from application.keywords import views

from application.search import views

from application.profile import views

from application.auth import models
from application.auth import views

# kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Luodaan lopulta tarvittavat tietokantataulut
db.create_all()