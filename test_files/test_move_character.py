"""
Nikita Olechko
A01337397
"""


from unittest import TestCase

from game import move_character


class TestMoveCharacter(TestCase):
    def test_move_down(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0}
        direct = "2"
        move_character(player, direct)
        self.assertEqual(player, {"X-coordinate": 0, "Y-coordinate": 1})

    def test_move_up(self):
        player = {"X-coordinate": 0, "Y-coordinate": 1}
        direct = "1"
        move_character(player, direct)
        self.assertEqual(player, {"X-coordinate": 0, "Y-coordinate": 0})

    def test_move_left(self):
        player = {"X-coordinate": 1, "Y-coordinate": 0}
        direct = "3"
        move_character(player, direct)
        self.assertEqual(player, {"X-coordinate": 0, "Y-coordinate": 0})

    def test_move_right(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0}
        direct = "4"
        move_character(player, direct)
        self.assertEqual(player, {"X-coordinate": 1, "Y-coordinate": 0})
