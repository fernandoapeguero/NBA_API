import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db

# constants
SUCCESS = 'success'
PLAYERS = 'players'
TEAMS = 'teams'
VENUES = 'venues'
EVENTS = 'events'

PLAYER = 'player'
TEAM = 'team'
VENUE = 'venue'
EVENT = 'event'

TOTAL_PLAYERS = 'total_players'
TOTAL_TEAMS = 'total_teams'
TOTAL_VENUES = 'total_venues'
TOTAL_EVENTS = 'total_events'

UPDATED_PLAYER = 'updated_player'
UPDATED_TEAM = 'updated_team'
UPDATED_VENUE = 'updated_venue'
UPDATED_EVENT = 'updated_event'

DELETED_PLAYER = 'deleted_player'
DELETED_TEAM = 'deleted_team'
DELETED_VENUE = 'deleted_venue'
DELETED_EVENT = 'deleted_event'

TEAM_MANAGEMENT_TOKEN = os.environ.get('Team_management')
VENUE_MANAGEMENT_TOKEN = os.environ.get('Venue_Management')
NBA_COMISSION_TOKEN = os.environ.get('NBA_Comission')

AUTHORIZATION = 'Authorization'


class NbaTestCase(unittest.TestCase):
    """This class represents the nba test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "nba_test"
        self.database_path = os.environ.get('LOCAL_DATABASE_URL')
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            # self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_players(self):
        res = self.client().get("/players")

        data = json.loads(res.data)

        self.assertEqual(res.status_code,  200)
        self.assertEqual(data[SUCCESS], True)
        self.assertTrue(data[PLAYERS])
        self.assertGreater(data[TOTAL_PLAYERS], 0)

    def test_get_player_by_id(self):

        res = self.client().get('/players/12')

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[SUCCESS], True)
        self.assertTrue(data[PLAYERS])

    def test_get_player_by_team_id(self):

        res = self.client().get('/players/1/teams')

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[SUCCESS], True)
        self.assertTrue(data[PLAYERS])
        self.assertGreater(data[TOTAL_PLAYERS], 0)

    def test_get_teams(self):
        res = self.client().get("/teams")

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[SUCCESS], True)
        self.assertTrue(len(data[TEAMS]))
        self.assertGreater(data[TOTAL_TEAMS], 0)

    def test_get_team_by_id(self):

        res = self.client().get('/teams/9')

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[SUCCESS], True)
        self.assertTrue(data[TEAM])

    def test_get_venues(self):
        res = self.client().get('/venues')

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[SUCCESS], True)
        self.assertTrue(len(data[VENUES]))
        self.assertGreater(data[TOTAL_VENUES], 0)

    def test_get_venue_by_id(self):

        res = self.client().get('/venues/3')

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[SUCCESS], True)
        self.assertTrue(data[VENUE])

    def test_get_events(self):
        res = self.client().get('/events')

        data = json.loads(res.data)

        self.assertTrue(res.status_code, 200)
        self.assertEqual(data[SUCCESS], True)
        self.assertTrue(len(data[EVENTS]))
        self.assertGreater(data[TOTAL_EVENTS], 0)

    def test_get_event_by_id(self):

        res = self.client().get('/events/18')

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[SUCCESS], True)
        self.assertTrue(data[EVENT])

    def test_post_player(self):

        player = {
            "first_name": "brick",
            "last_name": "wonders",
            "player_number": 18,
            "team": "Cavaliers",
            "mpg": 28.6,
            "ppg": 12.5,
            "rpg": 2.6,
            "apg": 4.9,
            "team_id": 16
        }

        res = self.client().post(
            '/players',
            json=player,
            headers={AUTHORIZATION: f'Bearer {TEAM_MANAGEMENT_TOKEN}'})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[SUCCESS], True)
        self.assertTrue(data[PLAYER])

    def test_post_team(self):

        team = {
            "name": "Space Jam",
            "home_city": "Hollywood",
            "losses": 5,
            "wins": 12,
            "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/5/5d/Oklahoma_City_Thunder.svg/1200px-Oklahoma_City_Thunder.svg.png"
        }

        res = self.client().post(
            '/teams',
            json=team,
            headers={AUTHORIZATION: f'Bearer {NBA_COMISSION_TOKEN}'})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[SUCCESS], True)

    def test_post_venue(self):

        venue = {
            "name": "Citi Bank Arena",
            "address": "40 Bay St, Toronto, ON M5J 2X2, Canada",
            "city": "Ontario",
            "zipcode": "33137",
            "is_available": False,
            "image": "https://upload.wikimedia.org/wikipedia/commons/5/57/Scotiabank_Arena_-_2018_%28cropped%29.jpg",
            "description": "Scotiabank Arena, formerly Air Canada Centre, is a multi-purpose arena located on Bay Street in the South Core district of Downtown Toronto, Ontario, Canada."
        }

        res = self.client().post(
            '/venues',
            json=venue,
            headers={
                AUTHORIZATION: f'Bearer {VENUE_MANAGEMENT_TOKEN}'
            })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[SUCCESS], True)

    def test_post_event(self):

        event = {
            "team_id": 19,
            "team_id_two": 18,
            "venue_id": 2,
            "start_time": "2021-12-05 20:30:00"

        }

        res = self.client().post(
            '/events',
            json=event,
            headers={
                AUTHORIZATION: f'Bearer {VENUE_MANAGEMENT_TOKEN}'
            })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[SUCCESS], True)

    def test_patch_player(self):

        updated_player_info = {
            "first_name": "richard"
        }

        res = self.client().patch(
            '/players/13',
            json=updated_player_info,
            headers={
                AUTHORIZATION: f'Bearer {TEAM_MANAGEMENT_TOKEN}'
            })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[SUCCESS], True)
        self.assertTrue(data[UPDATED_PLAYER])

    def test_patch_team(self):

        updated_team_info = {
            "name": "Free Agency"
        }

        res = self.client().patch(
            '/teams/44',
            json=updated_team_info,
            headers={
                AUTHORIZATION: f'Bearer {TEAM_MANAGEMENT_TOKEN}'
            })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[SUCCESS], True)
        self.assertTrue(data[UPDATED_TEAM])

    def test_patch_venue(self):

        updated_venue_info = {
            "name": "Chase Bank Center"
        }

        res = self.client().patch(
            '/venues/3',
            json=updated_venue_info,
            headers={
                AUTHORIZATION: f'Bearer {VENUE_MANAGEMENT_TOKEN}'
            })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[SUCCESS], True)
        self.assertTrue(data[UPDATED_VENUE])

    def test_patch_event(self):

        updated_event_info = {
            "team_id": 22,
            "team_one_score": 96

        }

        res = self.client().patch(
            '/events/18',
            json=updated_event_info,
            headers={
                AUTHORIZATION: f'Bearer {VENUE_MANAGEMENT_TOKEN}'
            })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[SUCCESS], True)
        self.assertTrue(data[UPDATED_EVENT])

    def test_delete_player(self):

        res = self.client().delete(
            '/players/16',
            headers={
                AUTHORIZATION: f'Bearer {TEAM_MANAGEMENT_TOKEN}'
            })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[SUCCESS], True)
        self.assertTrue(data[DELETED_PLAYER])

    def test_delete_team(self):

        res = self.client().delete(
            '/teams/45',
            headers={
                AUTHORIZATION: f'Bearer {NBA_COMISSION_TOKEN}'
            })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[SUCCESS], True)
        self.assertTrue(data[DELETED_TEAM])

    def test_delete_venue(self):

        res = self.client().delete(
            '/venues/1',
            headers={
                AUTHORIZATION: f'Bearer {VENUE_MANAGEMENT_TOKEN}'
            })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[SUCCESS], True)
        self.assertTrue(data[DELETED_VENUE])

    def test_delete_event(self):

        res = self.client().delete(
            '/events/17',
            headers={
                AUTHORIZATION: f'Bearer {VENUE_MANAGEMENT_TOKEN}'
            })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data[SUCCESS], True)
        self.assertTrue(data[DELETED_EVENT])


if __name__ == "__main__":
    unittest.main()
