from unittest import TestCase

from character.character import get_starter_pokemon


class TestGetStarterPokemon(TestCase):

    def test_TypeError(self):
        with self.assertRaises(TypeError):
            get_starter_pokemon(['squirtle'])

    def test_KeyError(self):
        with self.assertRaises(KeyError):
            get_starter_pokemon('charcuterie')
