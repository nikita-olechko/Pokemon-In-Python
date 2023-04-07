"""
Nikita Olechko
A01337397
"""


from unittest import TestCase
from unittest.mock import patch
import io
from game import get_user_choice


class TestGetUserChoice(TestCase):
    @patch('builtins.input', side_effect=["w"])
    def test_valid_input_one(self, _):
        actual = get_user_choice()
        self.assertEqual(actual, "w")

    @patch('builtins.input', side_effect=["a"])
    def test_valid_input_two(self, _):
        actual = get_user_choice()
        self.assertEqual(actual, "a")

    @patch('builtins.input', side_effect=["s"])
    def test_valid_input_three(self, _):
        actual = get_user_choice()
        self.assertEqual(actual, "s")

    @patch('builtins.input', side_effect=["d"])
    def test_valid_input_four(self, _):
        actual = get_user_choice()
        self.assertEqual(actual, "d")

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["Lemons", "w"])
    def test_invalid_input_printed_message(self, _, mock_stdout):
        get_user_choice()
        expected = "Please enter a real direction\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
