"""
Nikita Olechko
A01337397
"""


from unittest import TestCase
from unittest.mock import patch
import io
from movement.movement import describe_current_location


class TestDescribeCurrentLocation(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_start(self, mock_stdout):
        game_board = {(0, 0): "Room", (0, 1): "Room", (1, 0): "Room", (1, 1): "Room"}
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        describe_current_location(game_board, player)
        expected = "You are at (0, 0), Room.\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_end(self, mock_stdout):
        game_board = {(0, 0): "Room", (0, 1): "Room", (1, 0): "Room", (1, 1): "Room"}
        player = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        describe_current_location(game_board, player)
        expected = "You are at (1, 1), Room.\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_middle(self, mock_stdout):
        game_board = {(0, 0): "Room", (0, 1): "Room", (1, 0): "Room", (1, 1): "Room"}
        player = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        describe_current_location(game_board, player)
        expected = "You are at (0, 1), Room.\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_KeyError(self):
        game_board = {(0, 0): "Room", (0, 1): "Room", (1, 0): "Room", (1, 1): "Room"}
        player = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 5}
        with self.assertRaises(KeyError):
            describe_current_location(game_board, player)

    def test_TypeError_game_board(self):
        game_board = []
        player = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 5}
        with self.assertRaises(TypeError):
            describe_current_location(game_board, player)

    def test_TypeError_player(self):
        game_board = {(0, 0): "Room", (0, 1): "Room", (1, 0): "Room", (1, 1): "Room"}
        player = []
        with self.assertRaises(TypeError):
            describe_current_location(game_board, player)
