from unittest import TestCase

from board.make_board import make_board
from character.character import make_character
from pokemon.finding_pokemon import get_pokemon_dict


class TestGetAPokemonByLocation(TestCase):
    def test_TypeError_board(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        board = make_board(5, 5)
        with self.assertRaises(TypeError):
            get_pokemon_dict(board, character)

    def test_TypeError_character(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        board = make_board(5, 5)
        with self.assertRaises(TypeError):
            get_pokemon_dict(board, character)

    def test_TypeError_enemy_name(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        enemy_name = 1
        board = make_board(5, 5)
        with self.assertRaises(TypeError):
            get_pokemon_dict(board, character, enemy_name)
