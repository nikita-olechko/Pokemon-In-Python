"""
Nikita Olechko
A01337397
"""


from unittest import TestCase

from game import move_character


class TestMoveCharacter(TestCase):
    def test_move_down(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0}
        direct = "s"
        move_character(player, direct)
        self.assertEqual(player, {"X-coordinate": 0, "Y-coordinate": 1})

    def test_move_up(self):
        player = {"X-coordinate": 0, "Y-coordinate": 1}
        direct = "w"
        move_character(player, direct)
        self.assertEqual(player, {"X-coordinate": 0, "Y-coordinate": 0})

    def test_move_left(self):
        player = {"X-coordinate": 1, "Y-coordinate": 0}
        direct = "a"
        move_character(player, direct)
        self.assertEqual(player, {"X-coordinate": 0, "Y-coordinate": 0})

    def test_move_right(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0}
        direct = "d"
        move_character(player, direct)
        self.assertEqual(player, {"X-coordinate": 1, "Y-coordinate": 0})

    def test_TypeError_player(self):
        player_direction = "d"
        player = []
        with self.assertRaises(TypeError):
            move_character(player, player_direction)

    def test_TypeError_direction(self):
        player_direction = 1
        player = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 5}
        with self.assertRaises(TypeError):
            move_character(player, player_direction)
