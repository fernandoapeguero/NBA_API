import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db

team_manage_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im5YcFc4ZWRMbmR6aFFQOUZjTXNyOSJ9.eyJpc3MiOiJodHRwczovL2F1dGgwLWZzbmQudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmZmRkZTQ4MTMwOWUzMDA2OWM0MzRiNCIsImF1ZCI6Im5iYV9kYXRhX2FwaSIsImlhdCI6MTYxNDMxNjQ3MCwiZXhwIjoxNjE0MzIzNjcwLCJhenAiOiJmM0RLcWpxOEsySGhKZnI5dWJOU25ReFY2YVl4MjJaWiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnBsYXllcnMiLCJwYXRjaDpwbGF5ZXJzIiwicGF0Y2g6dGVhbXMiLCJwb3N0OnBsYXllcnMiXX0.KA4eopbhlFtFLuK9G8NfKFuAQkE-rEeg21NyG0Jb3Ht1fKIzSltqPvyjLZKglhWf4i1woMMZI6EeqAijuMSYO6dnxa_UBRKmTEsPHOoFCNPPW-uaRqco1l0bHZKeNExQR6qKnAdmt3jjWUOurok_CHkkuNk7wZIrDbDmus_Apt10iQgiodYZbDynoikF85luS_f3EeoN366WJYaa4f5tXeZCprtISgJ2R9CWMSsnUQOM3MutQmP9iNUZYSepSReubZ-67GR8MqXduQAd-mZqeQgy0d9OFT4fI2ahtpbuRLYIsz8sfuPLrxSse42CMNmaGG4UOvtiHVA-JgAf5MlwPQ'


class TriviaTestCase(unittest.TestCase):
    """This class represents the nba test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "nba_test"
        self.database_path = "postgresql://{}@{}/{}".format(
            'postgres:2225', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_players(self):
        res = self.client().get("/players")

        data = json.loads(res.data)

        self.assertEqual(res.status_code,  200)
        self.assertTrue(data['players'])
        self.assertGreater(data['total_players'], 0)

    def test_get_teams(self):
        res = self.client().get("/teams")

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['teams']))
        self.assertGreater(data['total_teams'], 0)

    def test_get_venues(self):
        res = self.client().get('/venues')

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['venues']))
        self.assertGreater(data['total_venues'], 0)

    def test_get_events(self):
        res = self.client().get('/events')

        data = json.loads(res.data)

        self.assertTrue(res.status_code, 200)
        self.assertTrue(len(data['events']))
        self.assertGreater(data['total_events'], 0)


if __name__ == "__main__":
    unittest.main()
