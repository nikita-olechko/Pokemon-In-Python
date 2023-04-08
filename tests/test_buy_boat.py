import io
from unittest import TestCase
from unittest.mock import patch

from character.character import make_character
from character.shop import buy_boat


class TestBuyBoat(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_buy_boat_output(self, mock_output):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        character["Gold"] = 150
        item = "2"
        buy_boat(character, item)
        system_printed = mock_output.getvalue()
        expected_output = "\n\tYou bought a Boat! You can now cross the ocean.\n\n"
        self.assertEqual(expected_output, system_printed)

    def test_buy_boat_Boat_increase(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        character["Gold"] = 150
        item = "2"
        buy_boat(character, item)
        self.assertEqual(character["Boat"], 1)

    def test_buy_boat_gold_decrease(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        character["Gold"] = 150
        item = "2"
        buy_boat(character, item)
        self.assertEqual(character["Gold"], 0)

    def test_TypeError_character(self):
        item = "2"
        with self.assertRaises(TypeError):
            buy_boat("character", item)

    def test_TypeError_item(self):
        item = 1
        with self.assertRaises(TypeError):
            buy_boat({}, item)

    def test_KeyError_character_no_Boat(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        del character["Boat"]
        with self.assertRaises(KeyError):
            buy_boat(character, "2")

    def test_KeyError_character_no_gold(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        del character["Gold"]
        with self.assertRaises(KeyError):
            buy_boat(character, "2")

    def test_ValueError_not_2(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        with self.assertRaises(ValueError):
            buy_boat(character, "3")
