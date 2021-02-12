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
    home_state = db.Column(db.String(), nullable=False)


class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(150))
    city = db.Column(db.String(50))
    zipcode = db.Column(db.String(10))
    is_available = db.Column(db.Boolean(), nullable=False)


class Events(db.Model):
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer(), db.ForeignKey('teams.id'))
    venue_id = db.Column(db.Integer(), db.ForeignKey('venues.id'))

    team = db.relationship(Team, backref=db.backref('events', cascade='all,delete'))
    venue = db.relationship(Venue, backref=db.backref('events', cascade='all,delete'))
    


