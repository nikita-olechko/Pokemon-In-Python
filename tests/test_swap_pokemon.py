from unittest import TestCase

from board.make_board import make_board
from character.character import make_character
from pokemon.capturing_pokemon import swap_pokemon


class TestSwapPokemon(TestCase):
    def test_TypeError_pokemon_inventory(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        pokemon_inventory = "bob"
        enemy_name = 'arceus'
        board = make_board(5, 5)
        with self.assertRaises(TypeError):
            swap_pokemon(pokemon_inventory, enemy_name, board, character)

    def test_TypeError_enemy_name(self):
        login_details = dict(Username='Username', Password="Password")
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
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
        enemy_name = 4
        board = make_board(5, 5)
        with self.assertRaises(TypeError):
            swap_pokemon(pokemon_inventory, enemy_name, board, character)

    def test_TypeError_board(self):
        login_details = {'Username': 'Username', 'Password': "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
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
        enemy_name = 'arceus'
        board = ""
        with self.assertRaises(TypeError):
            swap_pokemon(pokemon_inventory, enemy_name, board, character)

    def test_TypeError_character(self):
        character = []
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
        enemy_name = 'arceus'
        board = make_board(5, 5)
        with self.assertRaises(TypeError):
            swap_pokemon(pokemon_inventory, enemy_name, board, character)
