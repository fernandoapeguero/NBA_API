from threading import Event
from sqlalchemy.sql.expression import asc, desc, null
from models import setup_db, Venue, Team, Events, Player
from flask import json, jsonify, request
from auth import requires_auth
from flask import Flask, abort
from sqlalchemy import or_
from flask_cors import CORS


def create_app(text_config=None):
    app = Flask(__name__)
    setup_db(app)

    cors = CORS(app, resources={r'/nba/*': {'origins': '*'}})

    @app.after_request
    def after_request(reponse):
        reponse.headers.add('Access-Control-Allow-Headers',
                            'Content-Type,Authorization,true')
        reponse.headers.add('Access-Control-Allow-Method',
                            'GET,PATCH ,POST, DELETE , OPTIONS')
        return reponse

    PAGINATiON_COUNT = 10

    def paginate(request, selection):
    
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * PAGINATiON_COUNT
        end = start + PAGINATiON_COUNT

        info = [information.format() for information in selection]

        formatted_info = info[start:end]

        return formatted_info

    def paginated_events(request, event_list):
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * PAGINATiON_COUNT
        end = start + PAGINATiON_COUNT

        events = []

        for event_data in event_list:
                    team = Team.query.get(event_data.team_id)
                    team_two = Team.query.get(event_data.team_id_two)
                    venue = Venue.query.get(event_data.venue_id)

                    events.append({
                        'id': event_data.id,
                        'venue': venue.name,
                        'team_one': team.name,
                        'team_two': team_two.name,
                        'start_time': event_data.start_time,
                    })

        paginated_events = events[start:end]

        return paginated_events


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

        try:
            players = []

            search_term = request.args.get('search_term')
            players_list = ''
            if search_term:
                players_list = Player.query.filter(or_(Player.first_name.ilike(f'%{search_term}%'),Player.last_name.ilike(f'%{search_term}%'))).all()
            else: 
                players_list = Player.query.all()

            if players_list:
                players = paginate(request, players_list)
            
            return jsonify({
                'success': True,
                'players': players,
                'number_of_players': len(players)
            }), 200
        except:
            abort(404)
        

    @app.route('/players/<int:player_id>')
    def get_players_by_id(player_id):

        # if you pass in the value 0 for team it will give you all the players in every team 
        try:
            
            player = Player.query.get(player_id)
            
            return jsonify({
                    'success': True,
                    'players': player.format()
            }), 200
        except:
            abort(404)

    @app.route('/teams')
    def get_teams():

        teams = []
        try:
            search_term = request.args.get('search_term')
            team_list = None
            if search_term:
                team_list = Team.query.filter(Team.name.ilike(f'%{search_term}%')).all()
            else:
                team_list = Team.query.all()

            if team_list:
                teams = paginate(request, team_list)

            return jsonify({
                'success': True,
                'teams': teams,
                'number_of_teams': len(teams)
            }), 200

        except:
            abort(404)

    @app.route('/teams/<int:team_id>')
    def get_team_by_id(team_id):
        
        try:
            team = Team.query.get(team_id)

            return {
                'success': True,
                'team': team.format()
            }
        except:
            abort(404)


    @app.route('/events')
    def get_events():

        try:
            events =  []

            event_list = Events.query.order_by(desc(Events.id)).all()

            if event_list:
                events = paginated_events(request, event_list)

            return jsonify({
                'success': True,
                'events': events,
                'total_events': len(event_list)
            })
        except:
            abort(404)


    @app.route('/events/<int:event_id>')
    def get_events_by_id(event_id):

        try:
            event = None

            event_data = Events.query.get(event_id)

            if event_data:
                team = Team.query.get(event_data.team_id)
                team_two = Team.query.get(event_data.team_id_two)
                venue = Venue.query.get(event_data.venue_id)

                event = {
                    'id': event_data.id,
                    'venue': venue.name,
                    'team_one': team.name,
                    'team_two': team_two.name,
                    'start_time': event_data.start_time,
                }

            return jsonify({
                'success': True,
                'events': event
            }), 200
        except:
            abort(404)


    # Post Endpoints Group

    @app.route('/players', methods=['POST'])
    def post_player():

        try:
            player_data = request.get_json()

            first_name = player_data.get('first_name')
            last_name = player_data.get('last_name')
            team = player_data.get('team')
            mpg = player_data.get('mpg')
            ppg = player_data.get('ppg')
            rpg = player_data.get('rpg')
            apg = player_data.get('apg')
            team_id = player_data.get('team_id')

            player = Player(
                first_name=first_name,
                last_name=last_name,
                team=team,
                mpg=mpg,
                ppg=ppg,
                rpg=rpg,
                apg=apg,
                team_id=team_id
            )
            
            player.insert()

            return jsonify({
                'success': True,
                'player': player.format()
            }), 200

        except:
            abort(400)
        
    @app.route('/teams', methods=['POST'])
    def post_team():
        try:
            team_data = request.get_json()

            name = team_data.get('name')
            home_state = team_data.get('home_state')
            losses = team_data.get('losses')
            wins = team_data.get('wins')
            logo = team_data.get('logo')

            team = Team(
                name=name,
                home_state=home_state,
                losses=losses,
                wins=wins,
                logo=logo
            )

            team.insert()

            return jsonify({
                'success': True,
                'team': team.format()
            }), 200
        except:
            abort(400)



    @app.route('/events' , methods=['POST'])
    def post_event():

        try:
            event_data = request.get_json()

            team_id_one = event_data.get('team_one_id')
            team_id_two =  event_data.get('team_two_id')
            venue_id = event_data.get('venue_id')
            start_time = event_data.get('start_time')
            team_one_score = event_data.get('team_one_score') or 0
            team_two_score = event_data.get('team_one_score') or 0

            event = Events(
                team_id = team_id_one,
                team_id_two = team_id_two,
                venue_id = venue_id,
                start_time = start_time,
                team_one_score = team_one_score,
                team_two_score = team_two_score
            )

            event.insert()

            formatted_event = paginated_events(request, [event])

            return jsonify({
                'success': True,
                'event': formatted_event[0]
            }), 200

        except: 
            abort(400)


    # Error Handling


    @app.errorhandler(400)
    def invalid_syntax(error):

        return jsonify({
            'success': False,
            'error': error.code,
            'message': 'Invalid syntax '
        }), error.code


    @app.errorhandler(404)
    def invalid_syntax(error):

        return jsonify({
            'success': False,
            'error': error.code,
            'message': 'Not Found '
        }), error.code

    @app.errorhandler(405)
    def invalid_syntax(error):

        return jsonify({
            'success': False,
            'error': error.code,
            'message': 'Method Not Allow'
        }), error.code

    @app.errorhandler(422)
    def invalid_syntax(error):

        return jsonify({
            'success': False,
            'error': error.code,
            'message': 'Unproccesable'
        }), error.code


    @app.errorhandler(500)
    def invalid_syntax(error):

        return jsonify({
            'success': False,
            'error': error.code,
            'message': 'Internal Error'
        }), error.code

    return app
