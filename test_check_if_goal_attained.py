"""
Nikita Olechko
A01337397
"""

from unittest import TestCase

from simple_game import check_if_goal_attained


class TestCheckIfGoalAttained(TestCase):
    def test_true(self):
        game_board = {(0, 0): "Room", (0, 1): "Room", (1, 0): "Room", (1, 1): "Room"}
        player = {"X-coordinate": 1, "Y-coordinate": 1}
        actual = check_if_goal_attained(game_board, player)
        self.assertEqual(actual, True)

    def test_false(self):
        game_board = {(0, 0): "Room", (0, 1): "Room", (1, 0): "Room", (1, 1): "Room"}
        player = {"X-coordinate": 0, "Y-coordinate": 1}
        actual = check_if_goal_attained(game_board, player)
        self.assertEqual(actual, False)
