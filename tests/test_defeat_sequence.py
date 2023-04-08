import io
from unittest import TestCase
from unittest.mock import patch

from character.character import make_character
from combat.combat import defeat_sequence


class TestDefeatSequence(TestCase):
    @patch("builtins.input", side_effect=['q'])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_stdout(self, mock_output, _):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        enemy_name = 'arceus'
        defeat_sequence(character, enemy_name)
        system_printed = mock_output.getvalue()
        expected_output = f"All your Pokémon are unconscious. With no one to defend you, you were " \
                          f"eaten by {enemy_name.title()}.\n\n"
        self.assertEqual(expected_output, system_printed)

    def test_TypeError_character(self):
        enemy_name = 'nidoqueen'
        character = ""
        with self.assertRaises(TypeError):
            defeat_sequence(character, enemy_name)

    def test_TypeError_enemy_name(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        enemy_name = {}
        with self.assertRaises(TypeError):
            defeat_sequence(character, enemy_name)
