import io
from unittest import TestCase
from unittest.mock import patch

from utilities.display import display_pokemon


class TestDisplayPokemon(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_dispaly_pokemon(self, mock_output):
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
        display_pokemon(pokemon_inventory)
        system_printed = mock_output.getvalue()
        expected_output = "\n\t| 1: Arceus, Current HP: 600 | \n\n"
        self.assertEqual(expected_output, system_printed)

    def test_TypeError(self):
        pokemon_inventory = []
        with self.assertRaises(TypeError):
            display_pokemon(pokemon_inventory)
