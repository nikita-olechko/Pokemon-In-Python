from unittest import TestCase

from character.saving import create_new_save


class TestCreateNewSave(TestCase):
    def test_TypeError_character(self):
        character = 1
        pokemon_inventory = {}
        with self.assertRaises(TypeError):
            create_new_save(character, pokemon_inventory)

    def test_TypeError_pokemon_inventory(self):
        character = {}
        pokemon_inventory = 1
        with self.assertRaises(TypeError):
            create_new_save(character, pokemon_inventory)

    def test_ValueError_pokemon_inventory(self):
        character = {"Test": "Not Real"}
        pokemon_inventory = {}
        with self.assertRaises(ValueError):
            create_new_save(character, pokemon_inventory)
