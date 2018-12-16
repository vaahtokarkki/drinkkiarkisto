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

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

# roles in login_required
from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()
          
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True
                
                if int(current_user.roles) is role:
                    unauthorized = False

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

from application.auth import role
from application.ingredients import models
from application.keywords import models
from application.drinks import models
from application.auth import models

# Luodaan tarvittavat tietokantataulut
db.create_all()

from application import views
from application.ingredients import views
from application.keywords import views
from application.search import views
from application.admin import views
from application.profile import views
from application.drinks import views
from application.auth import views

# kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
