from unittest import TestCase

from movement.special_locations import at_shop


class TestAtShop(TestCase):
    def test_at_shop_True(self):
        player = {"X-coordinate": 1, "Y-coordinate": 0}
        self.assertEqual(at_shop(player), True)

    def test_at_shop_None(self):
        player = {"X-coordinate": 2, "Y-coordinate": 0}
        self.assertEqual(at_shop(player), None)

    def test_TypeError(self):
        player = ""
        with self.assertRaises(TypeError):
            at_shop(player)
