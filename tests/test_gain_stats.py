from unittest import TestCase
from unittest.mock import patch

from character.character import make_character
from character.leveling import gain_stats


class TestGainStats(TestCase):
    @patch('random.choice', side_effect=[1.0, 1.0])
    def test_stat_gain(self, _):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        self.assertEqual(gain_stats(character), {"exp_gain": 50, "gold_gain": 50})

    @patch('random.choice', side_effect=[1.0, 1.0])
    def test_exp_gain_on_character(self, _):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        gain_stats(character)
        self.assertEqual(character["EXP"], 37)

    @patch('random.choice', side_effect=[1.0, 1.0])
    def test_gold_gain_on_character(self, _):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        gain_stats(character)
        self.assertEqual(character["Gold"], 150)

    def test_TypeError(self):
        with self.assertRaises(TypeError):
            gain_stats("character")

    def test_ValueError_no_Level(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        del character["Level"]
        with self.assertRaises(ValueError):
            gain_stats(character)

    def test_ValueError_no_EXP(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        del character["EXP"]
        with self.assertRaises(ValueError):
            gain_stats(character)

    def test_ValueError_no_Gold(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        del character["Gold"]
        with self.assertRaises(ValueError):
            gain_stats(character)
