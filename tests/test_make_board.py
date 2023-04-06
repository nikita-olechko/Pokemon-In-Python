"""
Nikita Olechko
A01337397
"""

from unittest import TestCase

from board.make_board import make_board


class TestMakeBoard(TestCase):
    def test_two_by_two(self):
        actual = make_board(2, 2)
        self.assertEqual({(0, 0): 'Hospital  ', (0, 1): 'Ocean  ', (1, 0): 'Shop   ', (1, 1): 'Volcano'},
                         actual)

    def test_three_by_three(self):
        actual = make_board(3, 3)
        self.assertEqual({(0, 0): 'Hospital  ',
                          (0, 1): 'Volcano',
                          (0, 2): 'Forest ',
                          (1, 0): 'Shop   ',
                          (1, 1): 'Volcano',
                          (1, 2): 'Ocean  ',
                          (2, 0): 'Ocean  ',
                          (2, 1): 'Forest ',
                          (2, 2): 'Volcano'}, actual)

    def test_rectangle(self):
        actual = make_board(2, 3)
        self.assertEqual(actual, {(0, 0): 'Hospital  ',
                                  (0, 1): 'Ocean  ',
                                  (0, 2): 'Volcano',
                                  (1, 0): 'Shop   ',
                                  (1, 1): 'Volcano',
                                  (1, 2): 'Forest '})

    def test_ValueError_rows(self):
        with self.assertRaises(ValueError):
            make_board(1, 2)

    def test_ValueError_columns(self):
        with self.assertRaises(ValueError):
            make_board(2, 1)

    def test_ValueError_both(self):
        with self.assertRaises(ValueError):
            make_board(1, 1)
