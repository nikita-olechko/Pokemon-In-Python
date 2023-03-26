"""
Nikita Olechko
A01337397
"""


from unittest import TestCase
from unittest.mock import patch
import io
from simple_game import get_user_choice


class TestGetUserChoice(TestCase):
    @patch('builtins.input', side_effect=["1"])
    def test_valid_input_one(self, _):
        actual = get_user_choice()
        self.assertEqual(actual, "1")

    @patch('builtins.input', side_effect=["2"])
    def test_valid_input_two(self, _):
        actual = get_user_choice()
        self.assertEqual(actual, "2")

    @patch('builtins.input', side_effect=["3"])
    def test_valid_input_three(self, _):
        actual = get_user_choice()
        self.assertEqual(actual, "3")

    @patch('builtins.input', side_effect=["4"])
    def test_valid_input_four(self, _):
        actual = get_user_choice()
        self.assertEqual(actual, "4")

    @patch('builtins.input', side_effect=["up"])
    def test_valid_input_word_lowercase(self, _):
        actual = get_user_choice()
        self.assertEqual(actual, "up")

    @patch('builtins.input', side_effect=["UP"])
    def test_valid_input_word_uppercase(self, _):
        actual = get_user_choice()
        self.assertEqual(actual, "up")

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["Lemons", "up"])
    def test_invalid_input_printed_message(self, _, mock_stdout):
        get_user_choice()
        expected = "Please enter a valid direction\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
