import io
from unittest import TestCase
from unittest.mock import patch

from character.character import make_character
from character.shop import buy_items


class TestBuyItems(TestCase):
    @patch("builtins.input", side_effect=["1", "q"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_buy_pokeball_output(self, mock_output, _):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        buy_items(character)
        system_printed = mock_output.getvalue()
        expected_output = "You bought a Pokeball!" in system_printed
        self.assertEqual(expected_output, True)

    @patch("builtins.input", side_effect=["2", "q"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_buy_boat_output(self, mock_output, _):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        character["Gold"] = 150
        buy_items(character)
        system_printed = mock_output.getvalue()
        expected_output = "You bought a Boat!" in system_printed
        self.assertEqual(expected_output, True)

    @patch("builtins.input", side_effect=["2", "q"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_buy_boat_not_enough_gold(self, mock_output, _):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        character["Gold"] = 50
        buy_items(character)
        system_printed = mock_output.getvalue()
        expected_output = "You don't have enough gold for a Boat." in system_printed
        self.assertEqual(expected_output, True)

    @patch("builtins.input", side_effect=["1", "q"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_buy_pokeball_not_enough_gold(self, mock_output, _):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        character["Gold"] = 30
        buy_items(character)
        system_printed = mock_output.getvalue()
        expected_output = "You don't have enough gold" in system_printed
        self.assertEqual(expected_output, True)

    def test_TypeError(self):
        with self.assertRaises(TypeError):
            buy_items("character")

    def test_KeyError_no_Boat(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        del character["Boat"]
        with self.assertRaises(KeyError):
            buy_items(character)

    def test_KeyError_no_Gold(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        del character["Gold"]
        with self.assertRaises(KeyError):
            buy_items(character)

    def test_KeyError_no_Pokeballs(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        del character["Pokeballs"]
        with self.assertRaises(KeyError):
            buy_items(character)
