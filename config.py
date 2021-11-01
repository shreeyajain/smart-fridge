import os

from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
BASIC_AUTH_USERNAME="shbharad"
BASIC_AUTH_PASSWORD="thefireisnothot"
SECRET_KEY="columbiauniversityinthecityofnewyork"
REMEMBER_COOKIE_DURATION=timedelta(days=1)