from unittest import TestCase
from unittest.mock import patch

from combat.combat import enemy_move


class TestEnemyMove(TestCase):
    @patch("random.choice", side_effect=['judgment'])
    def test_enemy_move_proper(self, _):
        pokemon_name = 'arceus'
        combat_pokemon_stats = {"arceus": {
            "Class": "Legendary",
            "Current HP": 600,
            "Evolution-One": "Arceus",
            "Location": "Volcano",
            "Move-Four": "Earthquake",
            "Move-One": "Judgment",
            "Move-Three": "Fissure",
            "Move-Two": "Hyper Beam"
        }}
        self.assertEqual(enemy_move(combat_pokemon_stats, pokemon_name), 'judgment')

    def test_TypeError_pokemon_name(self):
        pokemon_name = 1
        combat_pokemon_stats = {"arceus": {
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
            enemy_move(combat_pokemon_stats, pokemon_name)

    def test_TypeError_combat_pokemon_stats(self):
        pokemon_name = "arceus"
        combat_pokemon_stats = 'arceus stats'
        with self.assertRaises(TypeError):
            enemy_move(combat_pokemon_stats, pokemon_name)

    def test_ValueError(self):
        pokemon_name = 'giratina'
        combat_pokemon_stats = {"arceus": {
            "Class": "Legendary",
            "Current HP": 600,
            "Evolution-One": "Arceus",
            "Location": "Volcano",
            "Move-Four": "Earthquake",
            "Move-One": "Judgment",
            "Move-Three": "Fissure",
            "Move-Two": "Hyper Beam"
        }}
        with self.assertRaises(ValueError):
            enemy_move(combat_pokemon_stats, pokemon_name)
