from unittest import TestCase

from board.make_board import make_board
from character.character import make_character
from combat.combat import get_combat_details


class TestGetCombatDetails(TestCase):
    def test_get_combat_details_TypeError_character(self):
        character = ""
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
        with self.assertRaises(TypeError):
            get_combat_details(character, board, pokemon_inventory)

    def test_get_combat_details_TypeError_board(self):
        login_details = {"Username": "User", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        board = ""
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
        with self.assertRaises(TypeError):
            get_combat_details(character, board, pokemon_inventory)

    def test_get_combat_details_TypeError_pokemon_inventory(self):
        login_details = {"Username": "User", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        board = make_board(5, 5)
        pokemon_inventory = ""
        with self.assertRaises(TypeError):
            get_combat_details(character, board, pokemon_inventory)

    def test_get_combat_details_TypeError_enemy_name(self):
        login_details = {"Username": "User", "Password": "Password"}
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
        with self.assertRaises(TypeError):
            get_combat_details(character, board, pokemon_inventory, enemy_name=[])
