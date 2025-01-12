import unittest
from unittest.mock import MagicMock
from projekt_2.app.model.sort_rq import SortRq

class TestSortRqFromRq(unittest.TestCase):

    def test_from_rq_with_valid_request(self):
        mock_request = MagicMock()
        mock_request.args.get.side_effect = lambda key, default=None: {
            'field': 'attack',
            'order': 'desc',
            'limit': '5',
            'to_display': 'name,attack'
        }.get(key, default)

        sort_rq = SortRq.from_rq(mock_request)

        self.assertEqual(sort_rq.field, 'attack')
        self.assertEqual(sort_rq.order, 'desc')
        self.assertEqual(sort_rq.limit, 5)
        self.assertEqual(sort_rq.to_display, 'name,attack')

    def test_from_rq_with_missing_values(self):
        mock_request = MagicMock()
        mock_request.args.get.side_effect = lambda key, default=None: {
            'field': 'defense'
        }.get(key, default)

        sort_rq = SortRq.from_rq(mock_request)

        self.assertEqual(sort_rq.field, 'defense')
        self.assertEqual(sort_rq.order, 'asc')
        self.assertEqual(sort_rq.limit, 10)
        self.assertIsNone(sort_rq.to_display)

    def test_from_rq_with_invalid_limit(self):
        mock_request = MagicMock()
        mock_request.args.get.side_effect = lambda key, default=None: {
            'field': 'speed',
            'order': 'asc',
            'limit': 'invalid',
        }.get(key, default)

        sort_rq = SortRq.from_rq(mock_request)

        self.assertEqual(sort_rq.field, 'speed')
        self.assertEqual(sort_rq.order, 'asc')
        self.assertEqual(sort_rq.limit, 10)

    def test_from_rq_with_no_args(self):
        mock_request = MagicMock()
        mock_request.args.get.side_effect = lambda key, default=None: default

        sort_rq = SortRq.from_rq(mock_request)

        self.assertEqual(sort_rq.field, 'name')
        self.assertEqual(sort_rq.order, 'asc')
        self.assertEqual(sort_rq.limit, 10)
        self.assertIsNone(sort_rq.to_display)

