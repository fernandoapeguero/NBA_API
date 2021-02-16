from sqlalchemy.sql.expression import false, true
from models import app, db, Venue, Team, Events, Player
from flask import jsonify, request
from auth import requires_auth
from flask import Flask, abort
from sqlalchemy import or_



@app.route('/')
def index():

    return f"Teams Api Home endpoint"

# update, Put, Delete, Post require Authentication 
# get does not 

# write api to get teams on the api does not require authentificaton 
# return a list of teams 10 per page you can change page number by adding page number to query 
# include a query parameter to paginated the pafes as well page size


# Get Endpoints group 

@app.route('/players')
def get_players():

    players = []
    error = False

    try:
        search_term = request.args.get('search_term')
        players_list = ''
        if search_term:
            players_list = Player.query.filter(or_(Player.first_name.ilike(f'%{search_term}%'),Player.last_name.ilike(f'%{search_term}%'))).all()
        else: 
            players_list = Player.query.all()

        if players_list:
            for player in players_list:
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
            'players': players,
            'number_of_players': len(players)
        })

@app.route('/players/<int:team_id>')
def get_all_players(team_id):

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
                'players': players,
                'number_of_players': len(players)
            })

@app.route('/teams')
def get_teams():

    teams = []
    error =  False
    try:
        search_term = request.args.get('search_term')
        team = ''
        if search_term:
            team = Team.query.filter(Team.name.ilike(f'%{search_term}%')).all()
            print(team)
        else:
            team = Team.query.all()

        print(search_term)


        for t in team:
            teams.append(t.get_team_info())

        return jsonify({
            'success': True,
            'teams': teams,
            'number_of_teams': len(teams)
        })
        
    except:
        error = True
        db.session.rollback()
    finally:
        db.session.close()

    if error:
        abort(404)

@app.route('/events/<int:event_id>')
def get_events(event_id):

    events = []
    error = False

    # {
    #     'events': 1,
    #     'team_one': 'bulls',
    #     'team_two': 'celtics',
    #     'event_date': '2021-05-18',
    #     'event_time': '20:30:00'
    # }
    try:
        print(event_id)
        event_list = ''
        if event_id > 0:

            event_list = Events.query.filter(Events.id == event_id).first()
        else:
            event_list = Events.query.all()

        if event_list:
            for event in event_list:
                events.append(event.)
        else:
            abort(404)


    except:
        db.session.rollback()
    finally:
        db.session.close()

    return 'Not implemented yet '


if __name__ == "__main__":
    app.run()