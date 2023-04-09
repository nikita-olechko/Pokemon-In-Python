import io
from unittest import TestCase
from unittest.mock import patch

from character.character import make_character
from character.shop import enough_gold


class TestEnoughGold(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_not_enough_gold_boat_output(self, mock_output):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        character["Gold"] = 50
        item = "2"
        enough_gold(character, item)
        system_printed = mock_output.getvalue()
        expected_output = "\n\tYou don't have enough gold for a Boat.\n\n\n"
        self.assertEqual(expected_output, system_printed)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_not_enough_gold_pokeball_output(self, mock_output):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        character["Gold"] = 30
        item = "1"
        enough_gold(character, item)
        system_printed = mock_output.getvalue()
        expected_output = "\n\tYou don't have enough gold for a Pokeball.\n\n\n"
        self.assertEqual(expected_output, system_printed)

    def test_enough_gold_pokeball(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        character["Gold"] = 50
        item = "1"
        enough_gold(character, item)
        self.assertEqual(enough_gold(character, item), True)

    def test_enough_gold_boat(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        character["Gold"] = 150
        item = "2"
        enough_gold(character, item)
        self.assertEqual(enough_gold(character, item), True)

    def test_enough_gold_pokeball_all_prefixes(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        character["Gold"] = 50
        item = "pokeb"
        enough_gold(character, item)
        self.assertEqual(enough_gold(character, item), True)

    def test_enough_gold_boat_all_prefixes(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        character["Gold"] = 150
        item = "boa"
        enough_gold(character, item)
        self.assertEqual(enough_gold(character, item), True)

    def test_TypeError_character(self):
        item = "2"
        with self.assertRaises(TypeError):
            enough_gold("character", item)

    def test_TypeError_item(self):
        item = 1
        with self.assertRaises(TypeError):
            enough_gold({}, item)

    def test_KeyError_character_no_Boat(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        del character["Boat"]
        with self.assertRaises(KeyError):
            enough_gold(character, "2")

    def test_KeyError_character_no_gold(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        del character["Gold"]
        with self.assertRaises(KeyError):
            enough_gold(character, "2")

    def test_KeyError_character_no_pokeballs(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        del character["Pokeballs"]
        with self.assertRaises(KeyError):
            enough_gold(character, "2")

    def test_KeyError_item_not_correct(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        del character["Pokeballs"]
        with self.assertRaises(KeyError):
            enough_gold(character, "3")
