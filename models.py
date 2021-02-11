from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)


# set up models for api 
# i was thinking about doing a dealership models or something else 
# maybe 


# nba theme models team model - venue model - events model 

class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    championship_wins = db.Column(db.Integer)


class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(150))
    city = db.Column(db.String(50))
    zipcode = db.Column(db.string(10))
    is_available = db.Column(db.Boolean(), nullable=False)


class Events(db.Model):
    __tablename__ = 'events'
    pass


