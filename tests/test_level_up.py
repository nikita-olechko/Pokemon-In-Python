import io
from unittest import TestCase
from unittest.mock import patch

from character.character import make_character
from character.leveling import level_up


class TestLevelUp(TestCase):
    def test_no_level_up(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        self.assertEqual(False, level_up(character))

    def test_level_up(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        character["EXP"] = 150
        self.assertEqual(True, level_up(character))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_output(self, mock_output):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        character["EXP"] = 150
        level_up(character)
        function_printed_this = mock_output.getvalue()
        expected_output = "You have leveled up!\nCurrent Level: 2\n\n"
        self.assertEqual(expected_output, function_printed_this)

    def test_TypeError(self):
        with self.assertRaises(TypeError):
            level_up("character")

    def test_KeyError_no_EXP(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        del character["EXP"]
        with self.assertRaises(KeyError):
            level_up(character)

    def test_KeyError_no_Level(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        del character["Level"]
        with self.assertRaises(KeyError):
            level_up(character)
