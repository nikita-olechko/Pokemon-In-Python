"""
Nikita Olechko
A01337397
"""
from unittest import TestCase

from board.make_board import make_board
from movement.movement import validate_move


class TestValidateMove(TestCase):
    def test_valid_input_number_s(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0}
        game_board = make_board(5, 5)
        player_direction = "s"
        self.assertEqual(validate_move(game_board, player, player_direction), True)

    def test_valid_input_letter_w(self):
        player = {"X-coordinate": 0, "Y-coordinate": 1}
        game_board = make_board(5, 5)
        player_direction = "w"
        self.assertEqual(validate_move(game_board, player, player_direction), True)

    def test_valid_input_letter_a(self):
        player = {"X-coordinate": 1, "Y-coordinate": 1}
        game_board = make_board(5, 5)
        player_direction = "a"
        self.assertEqual(validate_move(game_board, player, player_direction), True)

    def test_valid_input_letter_d(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0}
        game_board = make_board(5, 5)
        player_direction = "d"
        self.assertEqual(validate_move(game_board, player, player_direction), True)

    def test_invalid_input_number_s(self):
        player = {"X-coordinate": 0, "Y-coordinate": 4}
        game_board = make_board(5, 5)
        player_direction = "s"
        self.assertEqual(validate_move(game_board, player, player_direction), False)

    def test_invalid_input_letter_w(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0}
        game_board = make_board(5, 5)
        player_direction = "w"
        self.assertEqual(validate_move(game_board, player, player_direction), False)

    def test_invalid_input_letter_a(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0}
        game_board = make_board(5, 5)
        player_direction = "a"
        self.assertEqual(validate_move(game_board, player, player_direction), False)

    def test_invalid_input_letter_d(self):
        player = {"X-coordinate": 4, "Y-coordinate": 4}
        game_board = make_board(5, 5)
        player_direction = "d"
        self.assertEqual(validate_move(game_board, player, player_direction), False)

    def test_TypeError_game_board(self):
        game_board = []
        player = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 5}
        player_direction = "d"
        with self.assertRaises(TypeError):
            validate_move(game_board, player, player_direction)

    def test_TypeError_player(self):
        game_board = {(0, 0): "Room", (0, 1): "Room", (1, 0): "Room", (1, 1): "Room"}
        player_direction = "d"
        player = []
        with self.assertRaises(TypeError):
            validate_move(game_board, player, player_direction)

    def test_TypeError_direction(self):
        game_board = {(0, 0): "Room", (0, 1): "Room", (1, 0): "Room", (1, 1): "Room"}
        player_direction = 1
        player = {"X-coordinate": 2, "Y-coordinate": 0, "Current HP": 5}
        with self.assertRaises(TypeError):
            validate_move(game_board, player, player_direction)
