from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
import os 

database_path =  os.environ['DATABASE_URL']
db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    # uncomment if not using flask migration 
    # db.create_all()
class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    logo = db.Column(db.String(500))
    wins = db.Column(db.String(10), default=0)
    losses = db.Column(db.String(10), default=0)
    home_city = db.Column(db.String(), nullable=False)

    def __init__(self, name, logo, wins, losses,home_city):
        
        self.name = name
        self.logo = logo
        self.wins = wins
        self.losses = losses
        self.home_city = home_city

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):

        return {
            "id": self.id,
            "name": self.name,
            "logo": self.logo,
            "wins": self.wins,
            "losses": self.losses,
            "home_city": self.home_city
        }

class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(500))
    address = db.Column(db.String(150))
    city = db.Column(db.String(50))
    zipcode = db.Column(db.String(10))
    description = db.Column(db.String())
    is_available = db.Column(db.Boolean(), nullable=False)

    def __init__(self, name, image, address, city, zipcode, description, is_available):
        self.name = name
        self.image = image
        self.address = address 
        self.city = city 
        self.zipcode = zipcode 
        self.description = description
        self.is_available = is_available

    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):

        return {
            'id': self.id,
            'venue_name': self.name,
            'venue_image': self.image,
            'venue_address': self.address,
            'venue_city': self.city,
            'venue_zipcode': self.zipcode,
            'venue_description': self.description,
            'venue_is_available': self.is_available
        }


class Events(db.Model):
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime())

    team_one_score = db.Column(db.Integer(), nullable=True, default=0)
    team_two_score = db.Column(db.Integer(), nullable=True, default=0)

    team_id = db.Column(db.Integer(), db.ForeignKey('teams.id', ondelete='cascade'), nullable=False)
    team_id_two = db.Column(db.Integer(), db.ForeignKey('teams.id', ondelete='cascade'), nullable=False)
    venue_id = db.Column(db.Integer(), db.ForeignKey('venues.id', ondelete='cascade'), nullable=False)

    team = db.relationship(Team, backref=db.backref('events', cascade='all,delete'), foreign_keys=[team_id])
    team_two = db.relationship(Team, backref=db.backref('team_events', cascade='all,delete'), foreign_keys=[team_id_two])
    venue = db.relationship(Venue, backref=db.backref('events', cascade='all,delete'))
    

    def __init__(self, team_id, team_id_two, venue_id, start_time, team_one_score = 0, team_two_score = 0):
        
        self.team_id = team_id
        self.team_id_two = team_id_two
        self.venue_id = venue_id
        self.start_time = start_time
        self.team_one_score = team_one_score
        self.team_two_score = team_two_score


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
class Player(db.Model):

    __tablename__ = 'players'

    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    team = db.Column(db.String(50), nullable=False)
    player_number = db.Column(db.Integer(), unique=True)
    # Minutes per game
    mpg = db.Column(db.Float())
    # Points per Game
    ppg = db.Column(db.Float())
    # Rebound per game
    rpg = db.Column(db.Float())
    #assistance per game 
    apg = db.Column(db.Float())

    team_id = db.Column(db.Integer(), db.ForeignKey('teams.id'), default=0, nullable=True)

    def __init__(self, first_name, last_name, team, mpg, ppg, rpg, apg, team_id):
        self.first_name = first_name
        self.last_name = last_name
        self.team = team
        self.mpg = mpg 
        self.ppg = ppg
        self.rpg = rpg
        self.apg = apg
        self.team_id = team_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):

        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "team": self.team,
            "minutes_per_game": self.mpg,
            "points_per_game": self.ppg,
            "rebounds_per_game": self.rpg,
            "assistance_per_game": self.apg
        }

