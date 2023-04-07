import io
from unittest import TestCase
from unittest.mock import patch

from character.character import make_character
from character.shop import buy_pokeball


class TestBuyPokeball(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_buy_pokeball_output(self, mock_output):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        character["Gold"] = 50
        item = "1"
        buy_pokeball(character, item)
        system_printed = mock_output.getvalue()
        expected_output = "\n\tYou bought a Pokeball!\n\n"
        self.assertEqual(expected_output, system_printed)

    def test_buy_pokeball_pokeball_increase(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        character["Gold"] = 50
        item = "1"
        buy_pokeball(character, item)
        self.assertEqual(character["Pokeballs"], 3)

    def test_buy_pokeball_gold_decrease(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        character["Gold"] = 50
        item = "1"
        buy_pokeball(character, item)
        self.assertEqual(character["Gold"], 0)

    def test_TypeError_character(self):
        item = "1"
        with self.assertRaises(TypeError):
            buy_pokeball("character", item)

    def test_TypeError_item(self):
        item = 1
        with self.assertRaises(TypeError):
            buy_pokeball({}, item)

    def test_ValueError_character_no_pokeballs(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        del character["Pokeballs"]
        with self.assertRaises(ValueError):
            buy_pokeball(character, "1")

    def test_ValueError_character_no_gold(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        del character["Gold"]
        with self.assertRaises(ValueError):
            buy_pokeball(character, "1")
