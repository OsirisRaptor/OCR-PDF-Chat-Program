import unittest
from unittest.mock import patch
from src import app_interface

class TestAppInterface(unittest.TestCase):

    @patch('src.app_interface.run_app')
    def test_run_app(self, mock_run_app):
        # Test if the function is called when the app is run
        app_interface.run_app()
        mock_run_app.assert_called_once()

    @patch('src.app_interface.flask')
    def test_flask_app(self, mock_flask):
        # Test if the Flask app is correctly initialized
        app_interface.run_app()
        mock_flask.Flask.assert_called_once_with(__name__)

    @patch('src.app_interface.flask')
    def test_flask_run(self, mock_flask):
        # Test if the Flask app is run correctly
        app_interface.run_app()
        mock_flask.run.assert_called_once()

if __name__ == '__main__':
    unittest.main()