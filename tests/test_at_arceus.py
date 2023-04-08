from unittest import TestCase

from movement.special_locations import at_arceus


class TestAtArceus(TestCase):
    def test_at_arceus_True(self):
        player = {"X-coordinate": 4, "Y-coordinate": 0}
        self.assertEqual(at_arceus(player), True)

    def test_at_arceus_False(self):
        player = {"X-coordinate": 2, "Y-coordinate": 0}
        self.assertEqual(at_arceus(player), False)

    def test_TypeError(self):
        player = ""
        with self.assertRaises(TypeError):
            at_arceus(player)
