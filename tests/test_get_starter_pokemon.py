from unittest import TestCase

from character.character import get_starter_pokemon


class TestGetStarterPokemon(TestCase):

    def test_TypeError(self):
        with self.assertRaises(TypeError):
            get_starter_pokemon(['squirtle'])

    def test_ValueError(self):
        with self.assertRaises(ValueError):
            get_starter_pokemon('charcuterie')
