from unittest import TestCase
from unittest.mock import patch

from utilities.utilities import one_in_number_odds


class TestOneInNumberOdds(TestCase):
    @patch("random.randint", side_effect=[5])
    def test_False(self, _):
        self.assertEqual(one_in_number_odds(7), False)

    @patch("random.randint", side_effect=[1])
    def test_True(self, _):
        self.assertEqual(one_in_number_odds(5), True)

    @patch("random.randint", side_effect=[1])
    def test_One(self, _):
        self.assertEqual(one_in_number_odds(1), True)

    def test_TypeError(self):
        with self.assertRaises(TypeError):
            one_in_number_odds("")
