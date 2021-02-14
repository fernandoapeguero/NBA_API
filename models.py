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
    logo = db.Column(db.String(500))
    wins = db.Column(db.String(10), default=0)
    losses = db.Column(db.String(10), default=0)
    home_state = db.Column(db.String(), nullable=False)

    def __init__(self, name, logo, wins, losses,home_state):
        
        self.name = name
        self.logo = logo
        self.wins = wins
        self.losses = losses
        self.home_state = home_state


    def get_team_info(self):

        return {
            "name": self.name,
            "logo": self.logo,
            "wins": self.wins,
            "losses": self.losses,
            "home_state": self.home_state 
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


class Events(db.Model):
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime())

    team_id = db.Column(db.Integer(), db.ForeignKey('teams.id'))
    venue_id = db.Column(db.Integer(), db.ForeignKey('venues.id'))

    team = db.relationship(Team, backref=db.backref('events', cascade='all,delete'))
    venue = db.relationship(Venue, backref=db.backref('events', cascade='all,delete'))
    


class Player(db.Model):

    __tablename__ = 'players'

    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    team = db.Column(db.String(50), nullable=False)
    # Minutes per game
    mpg = db.Column(db.Float())
    # Points per Game
    ppg = db.Column(db.Float())
    # Rebound per game
    rpg = db.Column(db.Float())
    #assistance per game 
    apg = db.Column(db.Float())

    team_id = db.Column(db.Integer(), db.ForeignKey('teams.id'))

    def __init__(self, first_name, last_name, team, mpg, ppg, rpg, apg):
        self.first_name = first_name
        self.last_name = last_name
        self.team = team
        self.mpg = mpg 
        self.ppg = ppg
        self.rpg = rpg
        self.apg = apg

    

    def get_player_info(self):

        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "team": self.team,
            "minutes_per_game": self.ppg,
            "points_per_game": self.ppg,
            "rebounds_per_game": self.rpg,
            "assistance_per_game": self.apg
        }