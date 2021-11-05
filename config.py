import os

from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:thefireisnothot@localhost:5432/smartfridge'
BASIC_AUTH_USERNAME="shbharad"
BASIC_AUTH_PASSWORD="thefireisnothot"
SECRET_KEY="columbiauniversityinthecityofnewyork"
REMEMBER_COOKIE_DURATION=timedelta(days=1)
SQLALCHEMY_TRACK_MODIFICATIONS=False 
