"""
Nikita Olechko
A01337397
"""


import io
from unittest import TestCase
from unittest.mock import patch
from simple_game import win


class TestWin(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_win(self, mock_stout):
        win()
        expected = "Congratulations! You have mastered this technically, physically, and even " \
                   "philosophically challenging game.\nGo on, noble warrior, and rejoice in your victory. " \
                   "Full marks await you!\n"
        self.assertEqual(mock_stout.getvalue(), expected)
