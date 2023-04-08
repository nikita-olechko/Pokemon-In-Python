from unittest import TestCase
from unittest.mock import patch

from pokemon.finding_pokemon import retrieve_pokemon_from_json


class TestRetrievePokemonFromJson(TestCase):
    def test_TypeError_all_pokemon(self):
        all_pokemon = []
        with self.assertRaises(TypeError):
            retrieve_pokemon_from_json(all_pokemon)

    def test_TypeError_pokemon(self):
        all_pokemon = {"Username": "Username", "Password": "Password"}
        pokemon = 1
        with self.assertRaises(TypeError):
            retrieve_pokemon_from_json(all_pokemon, pokemon)

    @patch("random.choice", side_effect=["nidoqueen", 1.0])
    def test_retrieve_pokemon(self, _):
        all_pokemon = {"nidoqueen": {"Current HP": 10, "Class": "Forest"}}
        self.assertEqual(retrieve_pokemon_from_json(all_pokemon), {'nidoqueen': {'Class': 'Forest', 'Current HP': 10}})
