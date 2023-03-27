"""
Nikita Olechko
A01337397
"""


from unittest import TestCase
from unittest.mock import patch

from game import make_board


class TestMakeBoard(TestCase):
    @patch('random.choice', side_effect=["Game Room", "Game Room", "Game Room", "Game Room"])
    def test_two_by_two(self, _):
        actual = make_board(2, 2)
        self.assertEqual(actual, {(0, 0): 'Game Room', (0, 1): 'Game Room', (1, 0): 'Game Room', (1, 1): 'Game Room'})

    @patch('random.choice', return_value="Game Room")
    def test_three_by_three(self, _):
        actual = make_board(3, 3)
        self.assertEqual(actual, {(0, 0): 'Game Room', (0, 1): 'Game Room', (0, 2): 'Game Room', (1, 0): 'Game Room',
                                  (1, 1): 'Game Room', (1, 2): 'Game Room', (2, 0): 'Game Room', (2, 1): 'Game Room',
                                  (2, 2): 'Game Room'})

    @patch('random.choice', side_effect=["Game Room", "Game Room", "Game Room", "Game Room", "Game Room", "Game Room"])
    def test_rectangle(self, _):
        actual = make_board(2, 3)
        self.assertEqual(actual, {(0, 0): 'Game Room', (0, 1): 'Game Room', (0, 2): 'Game Room',
                                  (1, 0): 'Game Room', (1, 1): 'Game Room', (1, 2): 'Game Room'})

    def test_ValueError_rows(self):
        with self.assertRaises(ValueError):
            make_board(1, 2)

    def test_ValueError_columns(self):
        with self.assertRaises(ValueError):
            make_board(2, 1)

    def test_ValueError_both(self):
        with self.assertRaises(ValueError):
            make_board(1, 1)
