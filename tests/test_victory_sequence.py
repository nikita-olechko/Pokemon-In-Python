from unittest import TestCase

from board.make_board import make_board
from character.character import make_character
from combat.combat import victory_sequence


class TestVictorySequence(TestCase):
    def test_TypeError_character(self):
        board = make_board(5, 5)
        enemy_name = 'nidoqueen'
        pokemon_inventory = {"arceus": {
            "Class": "Legendary",
            "Current HP": 600,
            "Evolution-One": "Arceus",
            "Location": "Volcano",
            "Move-Four": "Earthquake",
            "Move-One": "Judgment",
            "Move-Three": "Fissure",
            "Move-Two": "Hyper Beam"
        }}
        character = ""
        with self.assertRaises(TypeError):
            victory_sequence(pokemon_inventory, enemy_name, character, board)

    def test_TypeError_pokemon_inventory(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        board = make_board(5, 5)
        enemy_name = 'nidoqueen'
        pokemon_inventory = ""
        with self.assertRaises(TypeError):
            victory_sequence(pokemon_inventory, enemy_name, character, board)

    def test_TypeError_board(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        enemy_name = 'nidoran'
        pokemon_inventory = {"bob": {
            "Class": "Legendary",
            "Current HP": 600,
            "Evolution-One": "Arceus",
            "Location": "Volcano",
            "Move-Four": "Earthquake",
            "Move-One": "Judgment",
            "Move-Three": "Fissure",
            "Move-Two": "Hyper Beam"
        }}
        board = ""
        with self.assertRaises(TypeError):
            victory_sequence(pokemon_inventory, enemy_name, character, board)

    def test_TypeError_enemy_name(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        board = make_board(5, 5)
        pokemon_inventory = {"arceus": {
            "Class": "Legendary",
            "Current HP": 600,
            "Evolution-One": "Arceus",
            "Location": "Volcano",
            "Move-Four": "Earthquake",
            "Move-One": "Judgment",
            "Move-Three": "Fissure",
            "Move-Two": "Hyper Beam"
        }}
        enemy_name = {}
        with self.assertRaises(TypeError):
            victory_sequence(pokemon_inventory, enemy_name, character, board)
