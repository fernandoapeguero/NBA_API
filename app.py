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

    # if you pass in the value 0 for team it will give you all the players in every team 

    error = False 
    players = []
    try:
        player_list = None
        if team_id > 0:
            player_list = Player.query.filter(Player.team_id == team_id).all()
        else:
            # order by tema id later
            player_list = Player.query.all()

        if player_list:
            for player in player_list:
                players.append(player.get_player_info())
    except:
        error = True
        db.session.rollback()
    finally:
        db.session.close()

    if error:
        abort(404)
    else:
        return jsonify({
                'success': True,
                'players': players
            })

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