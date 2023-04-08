from unittest import TestCase

from movement.special_locations import at_hospital


class TestAtHospital(TestCase):
    def test_at_hospital_True(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0}
        self.assertEqual(at_hospital(player), True)

    def test_at_hospital_False(self):
        player = {"X-coordinate": 2, "Y-coordinate": 0}
        self.assertEqual(at_hospital(player), False)

    def test_TypeError(self):
        player = ""
        with self.assertRaises(TypeError):
            at_hospital(player)
