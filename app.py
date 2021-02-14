from models import app, db, Venue, Team, Events, Player
from flask import jsonify
from auth import requires_auth
from flask import Flask, abort


@app.route('/')
def index():

    return f"Teams Api Home endpoint"

# update, Put, Delete, Post require Authentication 
# get does not 

# write api to get teams on the api does not require authentificaton 
# return a list of teams 10 per page you can change page number by adding page number to query 
# include a query parameter to paginated the pafes as well page size

@app.route('/players/<int:team_id>')
def get_players(team_id):

    #use team id to get players 
    try:

        players = Player.query.filter(1 == Player.team_id).all()

        print(players.get_player_info())

        return jsonify({
            'success': True,
            'players': [],


        })
    except:
        db.session.rollback()
    finally:
        db.session.close()

@app.route('/teams')
def get_teams():

    teams = []
    try:

        team = Team.query.all()

        for t in team:
            teams.append(t.get_team_info())

        return jsonify({
            'success': True,
            'teams': teams,
            'number_of_teams': len(teams)
        })
        
    except:
        db.session.rollback()
    finally:
        db.session.close()




if __name__ == "__main__":
    app.run()