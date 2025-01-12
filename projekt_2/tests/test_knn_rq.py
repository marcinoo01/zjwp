import unittest
from unittest.mock import MagicMock
from projekt_2.app.model.knn_rq import KnnRq


class TestKnnRqFromRq(unittest.TestCase):

    def test_from_rq_with_valid_request(self):
        mock_request = MagicMock()
        mock_request.args.get.side_effect = lambda key, default=None: {
            'stat_x': 'attack',
            'stat_y': 'speed',
            'k': '5',
            'threshold': '90'
        }.get(key, default)

        knn_rq = KnnRq.from_rq(mock_request)

        self.assertEqual(knn_rq.stat_x, 'attack')
        self.assertEqual(knn_rq.stat_y, 'speed')
        self.assertEqual(knn_rq.k, 5)
        self.assertEqual(knn_rq.threshold, 90.0)

    def test_from_rq_with_missing_values(self):
        mock_request = MagicMock()
        mock_request.args.get.side_effect = lambda key, default=None: {
            'stat_x': 'defense',
            'stat_y': 'hp'
        }.get(key, default)

        knn_rq = KnnRq.from_rq(mock_request)

        self.assertEqual(knn_rq.stat_x, 'defense')
        self.assertEqual(knn_rq.stat_y, 'hp')
        self.assertEqual(knn_rq.k, 3)
        self.assertEqual(knn_rq.threshold, 80.0)

    def test_from_rq_with_invalid_k_and_threshold(self):
        mock_request = MagicMock()
        mock_request.args.get.side_effect = lambda key, default=None: {
            'stat_x': 'attack',
            'stat_y': 'speed',
            'k': 'invalid',
            'threshold': 'not_a_number'
        }.get(key, default)

        with self.assertRaises(ValueError):
            KnnRq.from_rq(mock_request)

    def test_from_rq_with_no_args(self):
        mock_request = MagicMock()
        mock_request.args.get.side_effect = lambda key, default=None: default

        knn_rq = KnnRq.from_rq(mock_request)

        self.assertEqual(knn_rq.stat_x, None)
        self.assertEqual(knn_rq.stat_y, None)
        self.assertEqual(knn_rq.k, 3)
        self.assertEqual(knn_rq.threshold, 80.0)


if __name__ == '__main__':
    unittest.main()
