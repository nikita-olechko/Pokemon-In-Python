import io
from unittest import TestCase
from unittest.mock import patch

from utilities.display import display_moves


class TestDisplayMoves(TestCase):
    @patch("builtins.input", side_effect=["1"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_choose_a_move(self, mock_output, _):
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
        combat_pokemon = 'arceus'
        display_moves(combat_pokemon, pokemon_inventory)
        system_printed = mock_output.getvalue()
        expected_output = "\n\tChoose a move:\n"
        self.assertEqual(expected_output, system_printed)

    def test_TypeError_combat_pokemon(self):
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
        combat_pokemon = 4
        with self.assertRaises(TypeError):
            display_moves(combat_pokemon, pokemon_inventory)

    def test_TypeError_inventory(self):
        pokemon_inventory = []
        combat_pokemon = ""
        with self.assertRaises(TypeError):
            display_moves(combat_pokemon, pokemon_inventory)
