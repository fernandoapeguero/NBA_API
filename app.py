from werkzeug import exceptions
from models import setup_db, Venue, Team, Events, Player
from flask import jsonify, request
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


    # @app.route('/events')
    # def get_events():
    #     pass

    #     # try:
    #     #     search_term = request.args.get('search_term')
    #     #     Events = []

    #     #     event_list = None
    #     #     if search_term:
    #     #         event_list = Events.query.filter()
    #     #     else:
                
    #     # except:
    #     #     abort(404)


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
            

    return app
