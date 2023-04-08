from unittest import TestCase

from movement.special_locations import reset_health


class TestResetHealth(TestCase):
    def test_TypeError(self):
        pokemon_inventory = ""
        with self.assertRaises(TypeError):
            reset_health(pokemon_inventory)
