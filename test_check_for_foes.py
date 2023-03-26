"""
Nikita Olechko
A01337397
"""

from unittest import TestCase
from unittest.mock import patch

from simple_game import check_for_foes


class TestCheckForFoes(TestCase):
    @patch('random.randint', side_effect=[4])
    def test_true(self, _):
        actual = check_for_foes()
        self.assertEqual(actual, True)

    @patch('random.randint', side_effect=[1])
    def test_false_1(self, _):
        actual = check_for_foes()
        self.assertEqual(actual, False)

    @patch('random.randint', side_effect=[2])
    def test_false_2(self, _):
        actual = check_for_foes()
        self.assertEqual(actual, False)

    @patch('random.randint', side_effect=[3])
    def test_false_3(self, _):
        actual = check_for_foes()
        self.assertEqual(actual, False)
