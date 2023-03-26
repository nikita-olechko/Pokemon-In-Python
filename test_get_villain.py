"""
Nikita Olechko
A01337397
"""


from unittest import TestCase
from unittest.mock import patch

from simple_game import get_villain


class TestGetVillain(TestCase):
    @patch('random.choice', return_value=[('Baroness Bonecrusher, the Brutal Buccaneer', 'Brutal Buccaneer')])
    def test_first(self, _):
        actual = get_villain()
        self.assertEqual(actual, ('Baroness Bonecrusher, the Brutal Buccaneer', 'Brutal Buccaneer'))

    @patch('random.choice', return_value=[('Zany Zephyr, the Zesty Zealot', 'Zany Zorro')])
    def test_last(self, _):
        actual = get_villain()
        self.assertEqual(actual, ('Zany Zephyr, the Zesty Zealot', 'Zany Zorro'))

    @patch('random.choice', return_value=[('Inquisitor Ironheart, the Insidious Inquisitor', 'Intrepid Investigator')])
    def test_middle(self, _):
        actual = get_villain()
        self.assertEqual(actual, ('Inquisitor Ironheart, the Insidious Inquisitor', 'Intrepid Investigator'))
