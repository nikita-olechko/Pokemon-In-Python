from unittest import TestCase

from movement.movement import can_cross_ocean


class TestCanCrossOcean(TestCase):
    def test_can_cross_ocean_False(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Boat": False}
        self.assertEqual(can_cross_ocean(player), False)

    def test_can_cross_ocean_True(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Boat": True}
        self.assertEqual(can_cross_ocean(player), True)

    def test_TypeError(self):
        player = '{"X-coordinate": 0, "Y-coordinate": 0, "Boat": True}'
        with self.assertRaises(TypeError):
            can_cross_ocean(player)
