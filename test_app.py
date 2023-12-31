from unittest import TestCase

from app import app, games

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with app.test_client() as client:
            response = client.get('/')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<table', html)
            # Change to table.
            # including an entire tag with an id/class makes it very brittle,
            # someone can come in and  change that down the road
            # Can even search for html comments. Specify its for testing
            # test that you're getting a template

    def test_api_new_game(self):
        """Test starting a new game."""

        with app.test_client() as client:
            # We are creating a fake browser at the endpoint /api/newgame
            # Retrieving the return value which is the response (json data about
            # the new game)
            # getting a response object
            response = client.post('/api/new-game')
            # breakpoint()

            # gameId = response.d
            # in order to get the json data, we have to use .get_json()
            gameData = response.get_json()
            new_game_json_data = response.get_data(as_text=True)

            self.assertEqual(response.is_json, True)
            self.assertEqual(response.status_code, 200)
            self.assertIn("gameId", new_game_json_data)
            self.assertTrue(gameData["gameId"] in games)
            # we want to determine if the game_id exist in the dictionary
            # write a test for this route


