from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db?charset=utf8"
    app.config["SQLALCHEMY_ECHO"] = True


db = SQLAlchemy(app)

# Login functionality
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

# roles in login_required
from functools import wraps

def login_required(_func=None, *, role="ANY"):
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not (current_user and current_user.is_authenticated):
                return login_manager.unauthorized()

            acceptable_roles = set(("ANY", *current_user.roles()))

            if role not in acceptable_roles:
                return login_manager.unauthorized()

            return func(*args, **kwargs)
        return decorated_view
    return wrapper if _func is None else wrapper(_func)

# Load app content

from application import views

from application.auth.models import User
from application.bets.models import Bet
from application.races.models import Race
from application.races.models import Connector
from application.horses.models import Horse

from application.auth import views
from application.bets import views
from application.races import views
from application.horses import views


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

try:
    db.create_all()
except:
    pass