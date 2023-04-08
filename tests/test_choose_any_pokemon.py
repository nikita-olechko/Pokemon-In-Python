import io
from unittest import TestCase
from unittest.mock import patch

from utilities.display import choose_any_pokemon


class TestChooseAnyPokemon(TestCase):
    @patch("builtins.input", side_effect=["1"])
    def test_choose_pokemon(self, _):
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
        self.assertEqual(choose_any_pokemon(pokemon_inventory), 'arceus')

    @patch("builtins.input", side_effect=["2", "1"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_choose_incorrect_pokemon(self, mock_output, _):
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
        choose_any_pokemon(pokemon_inventory)
        system_printed = mock_output.getvalue()
        expected_output = "\n\t| 1: Arceus, Current HP: 600 | \n\nThat's not of you" \
                          "r Pokémon\n\n\t| 1: Arceus, Current HP: 600 | \n\n"
        self.assertEqual(expected_output, system_printed)

    def test_TypeError(self):
        pokemon_inventory = []
        with self.assertRaises(TypeError):
            choose_any_pokemon(pokemon_inventory)
