import unittest
from flask import Flask
from projekt_2.app.decorators.pokemon_decorator import json_response


class TestJsonResponseDecorator(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)

    def test_json_response_with_dict(self):
        @json_response
        def sample_function():
            return {"key": "value"}

        with self.app.test_request_context():
            response = sample_function()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {"key": "value"})

    def test_json_response_with_list(self):
        @json_response
        def sample_function():
            return ["item1", "item2", "item3"]

        with self.app.test_request_context():
            response = sample_function()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, ["item1", "item2", "item3"])

    def test_json_response_with_error(self):
        @json_response
        def sample_function():
            return {"error": "Something went wrong"}

        with self.app.test_request_context():
            response = sample_function()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_json(), {"error": "Something went wrong"})

