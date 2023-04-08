from unittest import TestCase

from combat.combat import combat_loop


class TestCombatLoop(TestCase):
    def test_TypeError_combat_details(self):
        combat_details = []
        with self.assertRaises(TypeError):
            combat_loop(combat_details)

    def test_TypeError_defeat(self):
        combat_details = {"character": 0, "board": 0, "pokemon_inventory": 0,
                          "enemy_name": 0, "enemy_stats": 0, "current_pokemon": 0}
        with self.assertRaises(TypeError):
            combat_loop(combat_details, defeat="")

    def test_TypeError_victory(self):
        combat_details = {"character": 0, "board": 0, "pokemon_inventory": 0,
                          "enemy_name": 0, "enemy_stats": 0, "current_pokemon": 0}
        with self.assertRaises(TypeError):
            combat_loop(combat_details, victory="")
