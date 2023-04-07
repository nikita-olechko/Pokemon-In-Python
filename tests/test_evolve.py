from unittest import TestCase

from character.leveling import evolve


class TestEvolutionOne(TestCase):

    def test_TypeError(self):
        with self.assertRaises(TypeError):
            evolve("string")
