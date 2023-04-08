from unittest import TestCase
from combat.combat import enemy_turn


class TestEnemyTurn(TestCase):
    def test_TypeError_moves(self):
        combat_details = {"character": 0, "board": 0, "pokemon_inventory": 0,
                          "enemy_name": 0, "enemy_stats": 0, "current_pokemon": 0}
        moves = 0
        with self.assertRaises(TypeError):
            enemy_turn(combat_details, moves)

    def test_TypeError_combat_details(self):
        combat_details = []
        moves = {}
        with self.assertRaises(TypeError):
            enemy_turn(combat_details, moves)

    def test_TypeError_defeat(self):
        combat_details = {}
        moves = {}
        with self.assertRaises(TypeError):
            enemy_turn(combat_details, moves, defeat="")

    def test_KeyError_moves_no_character(self):
        combat_details = {"bob": 0, "board": 0, "pokemon_inventory": 0,
                          "enemy_name": 0, "enemy_stats": 0, "current_pokemon": 0}
        moves = {}
        with self.assertRaises(KeyError):
            enemy_turn(combat_details, moves)

    def test_KeyError_moves_no_board(self):
        combat_details = {"character": 0, "bob": 0, "pokemon_inventory": 0,
                          "enemy_name": 0, "enemy_stats": 0, "current_pokemon": 0}
        moves = {}
        with self.assertRaises(KeyError):
            enemy_turn(combat_details, moves)

    def test_KeyError_moves_no_pokemon_inventory(self):
        combat_details = {"character": 0, "board": 0, "bob": 0,
                          "enemy_name": 0, "enemy_stats": 0, "current_pokemon": 0}
        moves = {}
        with self.assertRaises(KeyError):
            enemy_turn(combat_details, moves)

    def test_KeyError_moves_no_enemy_name(self):
        combat_details = {"character": 0, "board": 0, "pokemon_inventory": 0,
                          "bob": 0, "enemy_stats": 0, "current_pokemon": 0}
        moves = {}
        with self.assertRaises(KeyError):
            enemy_turn(combat_details, moves)

    def test_KeyError_moves_no_enemy_stats(self):
        combat_details = {"character": 0, "board": 0, "pokemon_inventory": 0,
                          "enemy_name": 0, "bob": 0, "current_pokemon": 0}
        moves = {}
        with self.assertRaises(KeyError):
            enemy_turn(combat_details, moves)

    def test_KeyError_moves_no_enemy_current_pokemon(self):
        combat_details = {"character": 0, "board": 0, "pokemon_inventory": 0,
                          "enemy_name": 0, "enemy_stats": 0, "bob": 0}
        moves = {}
        with self.assertRaises(KeyError):
            enemy_turn(combat_details, moves)
