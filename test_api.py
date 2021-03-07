import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db


class NbaTestCase(unittest.TestCase):
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
