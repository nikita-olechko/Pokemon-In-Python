from unittest import TestCase

from character.character import make_character, achieved_goal


class TestAchievedGoal(TestCase):
    def test_not_achieved_goal(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        self.assertEqual(achieved_goal(character), False)

    def test_achieved_goal(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        character["Victory"] = True
        self.assertEqual(achieved_goal(character), True)

    def test_TypeError(self):
        with self.assertRaises(TypeError):
            achieved_goal("String")

    def test_KeyError(self):
        login_details = {"Username": "Username", "Password": "Password"}
        tutorial_bool = False
        character = make_character(tutorial_bool, login_details)
        del character["Victory"]
        with self.assertRaises(KeyError):
            achieved_goal(character)
