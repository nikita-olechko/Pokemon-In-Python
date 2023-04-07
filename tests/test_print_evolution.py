from unittest import TestCase

from character.leveling import print_evolution


class TestPrintEvolution(TestCase):
    def test_TypeError_pokemon(self):
        with self.assertRaises(TypeError):
            print_evolution([], 'new_pokemon')

    def test_TypeError_new_pokemon(self):
        with self.assertRaises(TypeError):
            print_evolution('pokemon', {})
