"""
Nikita Olechko
A01337397
"""


from unittest import TestCase
from simple_game import make_character


class TestMakeCharacter(TestCase):
    def test_make_character(self):
        character = make_character()
        self.assertEqual(character, {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5})
