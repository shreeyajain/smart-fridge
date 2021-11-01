from flask import Flask, abort, render_template, request, session, redirect
from werkzeug.wrappers import UserAgentMixin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, current_user, UserMixin, login_user, logout_user, login_required
from datetime import timedelta

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/login"
login_manager.session_protection = "strong"

from app import views