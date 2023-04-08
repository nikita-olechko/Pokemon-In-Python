from unittest import TestCase

from movement.special_locations import at_special_location


class TestAtSpecialLocation(TestCase):
    def test_at_special_location_True(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0}
        self.assertEqual(at_special_location(player), True)

    def test_at_special_location_False(self):
        player = {"X-coordinate": 2, "Y-coordinate": 0}
        self.assertEqual(at_special_location(player), False)

    def test_TypeError(self):
        player = ""
        with self.assertRaises(TypeError):
            at_special_location(player)
