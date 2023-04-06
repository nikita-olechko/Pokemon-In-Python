"""
Nikita Olechko
A01337397
"""

from unittest import TestCase
from game import make_character


class TestMakeCharacter(TestCase):
    def test_make_character_tutorial_false(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        self.assertEqual({'Boat': False,
                          'Current HP': 5,
                          'EXP': 0,
                          'Gold': 100,
                          'Level': 1,
                          'Password': 'Password',
                          'Pokeballs': 2,
                          'Tutorial': False,
                          'Username': 'Username',
                          'Victory': False,
                          'X-coordinate': 0,
                          'Y-coordinate': 0}, character)

    def test_make_character_tutorial_true(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = True
        character = make_character(tutorial_bool, login_details)
        self.assertEqual({'Boat': False,
                          'Current HP': 5,
                          'EXP': 0,
                          'Gold': 100,
                          'Level': 1,
                          'Password': 'Password',
                          'Pokeballs': 2,
                          'Tutorial': True,
                          'Username': 'Username',
                          'Victory': False,
                          'X-coordinate': 0,
                          'Y-coordinate': 0}, character)
