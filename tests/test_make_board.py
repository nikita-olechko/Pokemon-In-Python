"""
Nikita Olechko
A01337397
"""

from unittest import TestCase

from board.make_board import make_board


class TestMakeBoard(TestCase):
    def test_5_by_5(self):
        actual = make_board(5, 5)
        self.assertEqual(actual, {(0, 0): 'Hospital  ',
                                  (0, 1): 'Forest ',
                                  (0, 2): 'Forest ',
                                  (0, 3): 'Mine   ',
                                  (0, 4): 'Mine   ',
                                  (1, 0): 'Shop   ',
                                  (1, 1): 'Forest ',
                                  (1, 2): 'Forest ',
                                  (1, 3): 'Mine   ',
                                  (1, 4): 'Mine   ',
                                  (2, 0): 'Ocean  ',
                                  (2, 1): 'Ocean  ',
                                  (2, 2): 'Ocean  ',
                                  (2, 3): 'Forest ',
                                  (2, 4): 'Forest ',
                                  (3, 0): 'Volcano',
                                  (3, 1): 'Volcano',
                                  (3, 2): 'Ocean  ',
                                  (3, 3): 'Plains ',
                                  (3, 4): 'Plains ',
                                  (4, 0): 'Volcano',
                                  (4, 1): 'Volcano',
                                  (4, 2): 'Ocean  ',
                                  (4, 3): 'Plains ',
                                  (4, 4): 'Plains '})

    def test_raises_ValueError_rows(self):
        with self.assertRaises(ValueError):
            make_board(2, 5)

    def test_raises_ValueError_columns(self):
        with self.assertRaises(ValueError):
            make_board(5, 2)

    def test_raises_TypeError_rows(self):
        with self.assertRaises(TypeError):
            make_board("5", 5)

    def test_raises_TypeError_columns(self):
        with self.assertRaises(TypeError):
            make_board(5, "5")
