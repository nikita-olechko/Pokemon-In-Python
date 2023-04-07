from unittest import TestCase

from character.leveling import evolution_two


class TestEvolutionOne(TestCase):
    def test_TypeError_current_evolution(self):
        current_evolution = 1
        pokemon_inventory = {}
        pokemon = ""
        value = {}
        with self.assertRaises(TypeError):
            evolution_two(current_evolution, pokemon_inventory, pokemon, value)

    def test_TypeError_pokemon(self):
        current_evolution = ""
        pokemon_inventory = {}
        pokemon = 1
        value = {}
        with self.assertRaises(TypeError):
            evolution_two(current_evolution, pokemon_inventory, pokemon, value)

    def test_TypeError_pokemon_inventory(self):
        current_evolution = ""
        pokemon_inventory = 1
        pokemon = ""
        value = {}
        with self.assertRaises(TypeError):
            evolution_two(current_evolution, pokemon_inventory, pokemon, value)

    def test_TypeError_value(self):
        current_evolution = ""
        pokemon_inventory = {}
        pokemon = ""
        value = 1
        with self.assertRaises(TypeError):
            evolution_two(current_evolution, pokemon_inventory, pokemon, value)
