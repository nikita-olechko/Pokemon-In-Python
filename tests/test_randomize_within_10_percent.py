from unittest import TestCase
from unittest.mock import patch

from utilities.utilities import randomize_within_10_percent


class TestRandomizeWithin10Percent(TestCase):
    @patch("random.choice", side_effect=[1.0])
    def test_middle(self, _):
        self.assertEqual(randomize_within_10_percent(7), 7)

    @patch("random.choice", side_effect=[0.9])
    def test_lowest_end(self, _):
        self.assertEqual(randomize_within_10_percent(100), 90)

    @patch("random.choice", side_effect=[1.1])
    def test_high_end(self, _):
        self.assertEqual(randomize_within_10_percent(100), 110)

    def test_TypeError(self):
        with self.assertRaises(TypeError):
            randomize_within_10_percent("1")
