from unittest import TestCase

from character.saving import save_game


class TestCreateNewSave(TestCase):
    def test_TypeError_character(self):
        character = 1
        pokemon_inventory = {}
        with self.assertRaises(TypeError):
            save_game(character, pokemon_inventory)

    def test_TypeError_pokemon_inventory(self):
        character = {}
        pokemon_inventory = 1
        with self.assertRaises(TypeError):
            save_game(character, pokemon_inventory)

    def test_KeyError_pokemon_inventory(self):
        character = {"Test": "Not Real"}
        pokemon_inventory = {}
        with self.assertRaises(KeyError):
            save_game(character, pokemon_inventory)
