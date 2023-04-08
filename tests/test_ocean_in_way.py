from unittest import TestCase

from board.make_board import make_board
from movement.movement import ocean_in_way


class TestOceanInWay(TestCase):
    def test_ocean_in_way_False(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0}
        game_board = make_board(5, 5)
        player_direction = "d"
        self.assertEqual(ocean_in_way(game_board, player, player_direction), False)

    def test_ocean_in_way_True(self):
        player = {"X-coordinate": 2, "Y-coordinate": 2}
        game_board = make_board(5, 5)
        player_direction = "d"
        self.assertEqual(ocean_in_way(game_board, player, player_direction), True)

    def test_TypeError_game_board(self):
        player = {"X-coordinate": 0, "Y-coordinate": 1}
        game_board = "make_board(5, 5)"
        player_direction = "w"
        with self.assertRaises(TypeError):
            ocean_in_way(game_board, player, player_direction)

    def test_TypeError_player(self):
        player = []
        game_board = make_board(5, 5)
        player_direction = "w"
        with self.assertRaises(TypeError):
            ocean_in_way(game_board, player, player_direction)

    def test_TypeError_direction(self):
        player = {"X-coordinate": 0, "Y-coordinate": 1}
        game_board = make_board(5, 5)
        player_direction = 1
        with self.assertRaises(TypeError):
            ocean_in_way(game_board, player, player_direction)