import io
from unittest import TestCase
from unittest.mock import patch

from character.character import make_character
from character.shop import display_shop_items


class TestDisplayShopItems(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_boat(self, mock_output):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        display_shop_items(character)
        system_printed = mock_output.getvalue()
        expected_output = "\t| 1: Pokéball, 50 Gold | 2: Boat, 150 Gold |\n\n"
        self.assertEqual(expected_output, system_printed)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_no_boat(self, mock_output):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        character["Boat"] = True
        display_shop_items(character)
        system_printed = mock_output.getvalue()
        expected_output = "\t| 1: Pokéball, 50 Gold | \n\n"
        self.assertEqual(expected_output, system_printed)

    def test_TypeError(self):
        with self.assertRaises(TypeError):
            display_shop_items("character")

    def test_KeyError_no_Boat(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        del character["Boat"]
        with self.assertRaises(KeyError):
            display_shop_items(character)
