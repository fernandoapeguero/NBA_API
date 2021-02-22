from threading import Event
from models import setup_db, Venue, Team, Events, Player
from flask import json, jsonify, request
from auth import requires_auth, AuthError
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


    # GET Endpoints group 

    @app.route('/players')
    def get_players():

        try:
            players = []

            search_term = request.args.get('search_term')
            players_list = ''
            if search_term:
                players_list = Player.query.filter(or_(Player.first_name.ilike(f'%{search_term}%'),Player.last_name.ilike(f'%{search_term}%'))).order_by('id').all()
            else: 
                players_list = Player.query.order_by('id').all()

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
                team_list = Team.query.filter(Team.name.ilike(f'%{search_term}%')).order_by('id').all()
            else:
                team_list = Team.query.order_by('id').all()

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

    @app.route('/venues')
    def get_venues():


        try:

            search_term = request.args.get('search_term')

            venues = None
            if search_term:
                venues = Venue.query.filter(Venue.name.ilike(f'%{search_term}%')).order_by('id').all()
            else:
                venues = Venue.query.order_by('id').all()


            formatted_venues = paginate(request, venues)

            return {
                'success': True,
                'venues': formatted_venues,
                'total_venues': len(venues)
            }
        except:
            abort(404)

    @app.route('/venues/<int:venue_id>')
    def get_venue_by_id(venue_id):

        try:
            venue = Venue.query.get(venue_id)

            return jsonify({
                'success': True,
                'venue': venue.format()
            })
        except:
            abort(404)

    @app.route('/events')
    def get_events():

        try:
            events =  []

            event_list = Events.query.order_by('id').all()

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


    # POST Endpoints Group

    @app.route('/players', methods=['POST'])
    @requires_auth('post:players')
    def post_player(jwt):

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
    @requires_auth('post:teams')
    def post_team(jwt):
        try:
            team_data = request.get_json()

            name = team_data.get('name')
            home_state = team_data.get('home_state')
            losses = team_data.get('losses') or 0
            wins = team_data.get('wins') or 0
            logo = team_data.get('logo') or ''

            team = Team(
                name = name,
                home_state = home_state,
                losses = losses,
                wins = wins,
                logo = logo
            )

            team.insert()
            print('de verdad ')
            return jsonify({
                'success': True,
                'team': team.format()
            }), 200
        except:
            abort(400)

    @app.route('/venues', methods=['POST'])
    @requires_auth('post:venues')
    def post_venue(jwt):

        try:
            venue_data = request.get_json()

            name = venue_data.get('name')
            address = venue_data.get('address')
            city = venue_data.get('city')
            zipcode = venue_data.get('zipcode')
            venue_image = venue_data.get('image')
            description = venue_data.get('description')
            is_available = venue_data.get('is_available')

            venue = Venue(
                name = name,
                address = address,
                city = city,
                zipcode = zipcode,
                is_available = is_available,
                image = venue_image,
                description = description
            )

            venue.insert()


            return jsonify({
                'success': True,
                'venue': venue.format()
            })
        except:
            abort(404)

    @app.route('/events' , methods=['POST'])
    @requires_auth('post:events')
    def post_event(jwt):

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

    # PATH Endpoints Group

    @app.route('/players/<int:player_id>', methods=['PATCH'])
    @requires_auth('patch:players')
    def patch_player(jwt, player_id):

        try:
            player = Player.query.get(player_id)
            player_data = request.get_json()

            player.first_name = player_data.get('first_name') or player.first_name
            player.last_name = player_data.get('last_name') or player.last_name
            player.team = player_data.get('team') or player.team
            player.mpg = player_data.get('mpg') or player.mpg
            player.ppg = player_data.get('ppg') or player.ppg
            player.rpg = player_data.get('rpg') or player.rpg
            player.apg = player_data.get('apg') or player.apg
            player.team_id = player_data.get('team_id') or player.team_id
            
            player.update()

            return jsonify({
                'success': True,
                'updated_player': player.format()
            }), 200

        except:
            abort(422)

    
    @app.route('/teams/<int:team_id>', methods=['PATCH'])
    @requires_auth('patch:teams')
    def patch_team(jwt, team_id):

        try: 
            team = Team.query.get(team_id)
            team_data = request.get_json()

            team.name = team_data.get('name') or team.name
            team.home_state = team_data.get('home_state') or team.home_state
            team.losses = team_data.get('losses') or team.losses
            team.wins = team_data.get('wins') or team.wins
            team.logo = team_data.get('logo') or team.logo

            team.update()

            return jsonify({
                'success': True,
                'updated_team': team.format()
            }), 200
        except:
            abort(422)

    
    @app.route('/venues/<int:venue_id>', methods=['PATCH'])
    @requires_auth('patch:venues')
    def patch_venue(jwt, venue_id):

        try:
            venue = Venue.query.get(venue_id)
            venue_data  = request.get_json()

            venue.name = venue_data.get('name') or venue.name
            venue.address = venue_data.get('address') or venue.address
            venue.city = venue_data.get('city') or venue.city
            venue.zipcode = venue_data.get('zipcode') or venue.zipcode
            venue.is_available = venue_data.get('is_available') or venue.is_available
            venue.image = venue_data.get('image') or venue.image

            venue.update()

            return jsonify({
                'success': True,
                'updated_venue': venue.format()
            }), 200
        except:
            abort(422)


    @app.route('/events/<int:event_id>' , methods=['PATCH'])
    @requires_auth('patch:events')
    def patch_events(jwt, event_id):

        try:
            event = Events.query.get(event_id)
            event_data = request.get_json()

            event.team_id = event_data.get('team_one_id') or event.team_id
            event.team_id_two = event_data.get('team_id_two') or event.team_id_two
            event.venue_id = event_data.get('venue_id') or event.venue_id
            event.team_one_score = event_data.get('team_one_score') or event.team_one_score
            event.team_two_score = event_data.get('team_two_score') or event.team_two_score

            event.update()

            formatted_event = paginated_events(request, [event])

            return jsonify({
                'success': True,
                'updated_event': formatted_event[0]
            }), 200
        
        except:
            abort(422)

    # DELETE Endpoint Group



    @app.route('/players/<int:player_id>' , methods={'DELETE'})
    @requires_auth('delete:players')
    def delete_player(jwt, player_id):

        try:
            player = Player.query.get(player_id)

            player.delete()

            return jsonify({
                'success': True,
                'deleted_player': player.format()
            }), 200
        except:
            abort(422)

    @app.route('/teams/<int:team_id>', methods=['DELETE'])
    @requires_auth('delete:teams')
    def delete_team(jwt, team_id):

        try:
            team = Team.query.get(team_id)

            team.delete()

            return jsonify({
                'success': True,
                'deleted_team': team.format()
            }), 200
        except:
            abort(422)

    @app.route('/venues/<int:venue_id>', methods=['DELETE'])
    @requires_auth('delete:venues')
    def delete_venue(jwt, venue_id):

        try:
            venue = Venue.query.get(venue_id)

            venue.delete()

            return jsonify({
                'success': True,
                'deleted_venue': venue.format()
            }), 200
        except:
            abort(422)
        
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

    @app.errorhandler(AuthError)
    def auth_error(error):

        return jsonify({
            'success': False,
            'error': error.status_code,
            'message': error.error
        }), error.status_code

    return app
