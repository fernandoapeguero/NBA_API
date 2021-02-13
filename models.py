from operator import truediv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    wins = db.Column(db.String(10), nullable=True, default=0)
    losses = db.Column(db.String(10), nullable=True, default=0)
    home_state = db.Column(db.String(), nullable=False)


class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(500), nullable=True)
    address = db.Column(db.String(150))
    city = db.Column(db.String(50))
    zipcode = db.Column(db.String(10))
    is_available = db.Column(db.Boolean(), nullable=False)


class Events(db.Model):
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime())
    
    team_id = db.Column(db.Integer(), db.ForeignKey('teams.id'))
    venue_id = db.Column(db.Integer(), db.ForeignKey('venues.id'))

    team = db.relationship(Team, backref=db.backref('events', cascade='all,delete'))
    venue = db.relationship(Venue, backref=db.backref('events', cascade='all,delete'))
    


