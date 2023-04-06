"""
Nikita Olechko
A01337397
"""
import io
from unittest import TestCase
from unittest.mock import patch

from movement.movement import validate_move


class TestValidateMove(TestCase):
    def test_valid_input_number_y(self):
        game_board = {(0, 0): "Room", (0, 1): "Room", (1, 0): "Room", (1, 1): "Room"}
        player = {"X-coordinate": 0, "Y-coordinate": 0}
        direct = "2"
        actual = validate_move(game_board, player, direct)
        self.assertEqual(actual, True)

    def test_valid_input_letter_y(self):
        game_board = {(0, 0): "Room", (0, 1): "Room", (1, 0): "Room", (1, 1): "Room"}
        player = {"X-coordinate": 0, "Y-coordinate": 0}
        direct = "down"
        actual = validate_move(game_board, player, direct)
        self.assertEqual(actual, True)

    def test_invalid_input_number_y(self):
        game_board = {(0, 0): "Room", (0, 1): "Room", (1, 0): "Room", (1, 1): "Room"}
        player = {"X-coordinate": 0, "Y-coordinate": 0}
        direct = "1"
        actual = validate_move(game_board, player, direct)
        self.assertEqual(actual, False)

    def test_invalid_input_letter_y(self):
        game_board = {(0, 0): "Room", (0, 1): "Room", (1, 0): "Room", (1, 1): "Room"}
        player = {"X-coordinate": 0, "Y-coordinate": 0}
        direct = "up"
        actual = validate_move(game_board, player, direct)
        self.assertEqual(actual, False)

    def test_valid_input_number_x(self):
        game_board = {(0, 0): "Room", (0, 1): "Room", (1, 0): "Room", (1, 1): "Room"}
        player = {"X-coordinate": 0, "Y-coordinate": 0}
        direct = "4"
        actual = validate_move(game_board, player, direct)
        self.assertEqual(actual, True)

    def test_valid_input_letter_x(self):
        game_board = {(0, 0): "Room", (0, 1): "Room", (1, 0): "Room", (1, 1): "Room"}
        player = {"X-coordinate": 0, "Y-coordinate": 0}
        direct = "right"
        actual = validate_move(game_board, player, direct)
        self.assertEqual(actual, True)

    def test_invalid_input_number_x(self):
        game_board = {(0, 0): "Room", (0, 1): "Room", (1, 0): "Room", (1, 1): "Room"}
        player = {"X-coordinate": 0, "Y-coordinate": 0}
        direct = "3"
        actual = validate_move(game_board, player, direct)
        self.assertEqual(actual, False)

    def test_invalid_input_letter_x(self):
        game_board = {(0, 0): "Room", (0, 1): "Room", (1, 0): "Room", (1, 1): "Room"}
        player = {"X-coordinate": 0, "Y-coordinate": 0}
        direct = "left"
        actual = validate_move(game_board, player, direct)
        self.assertEqual(actual, False)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_input_printed_x_coordinate(self, mock_stout):
        game_board = {(0, 0): "Room", (0, 1): "Room", (1, 0): "Room", (1, 1): "Room"}
        player = {"X-coordinate": 0, "Y-coordinate": 0}
        direct = "left"
        validate_move(game_board, player, direct)
        self.assertEqual(mock_stout.getvalue(), "That is not a valid move\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_input_printed_y_coordinate(self, mock_stout):
        game_board = {(0, 0): "Room", (0, 1): "Room", (1, 0): "Room", (1, 1): "Room"}
        player = {"X-coordinate": 0, "Y-coordinate": 0}
        direct = "up"
        validate_move(game_board, player, direct)
        self.assertEqual(mock_stout.getvalue(), "That is not a valid move\n")
