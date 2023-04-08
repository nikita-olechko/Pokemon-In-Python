from unittest import TestCase
from unittest.mock import patch

from combat.combat import your_move


class TestYourMove(TestCase):
    @patch("builtins.input", side_effect=['1'])
    def test_your_move_proper(self, _):
        current_pokemon = 'arceus'
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
        self.assertEqual(your_move(current_pokemon, pokemon_inventory), 'judgment')

    @patch("builtins.input", side_effect=['1'])
    def test_TypeError_current_pokemon(self, _):
        current_pokemon = 1
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
            your_move(current_pokemon, pokemon_inventory)

    @patch("builtins.input", side_effect=['1'])
    def test_TypeError_pokemon_inventory(self, _):
        current_pokemon = "1"
        pokemon_inventory = "arceus"
        with self.assertRaises(TypeError):
            your_move(current_pokemon, pokemon_inventory)

    @patch("builtins.input", side_effect=['1'])
    def test_KeyError_pokemon_inventory(self, _):
        current_pokemon = "bob"
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
        with self.assertRaises(KeyError):
            your_move(current_pokemon, pokemon_inventory)
