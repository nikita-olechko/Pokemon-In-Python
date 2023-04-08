from unittest import TestCase
from unittest.mock import patch

from utilities.utilities import yes_or_no_input


class TestYesOrNoInput(TestCase):
    @patch("builtins.input", side_effect=["y"])
    def test_yes(self, _):
        self.assertEqual(yes_or_no_input(), True)

    @patch("builtins.input", side_effect=["n"])
    def test_no(self, _):
        self.assertEqual(yes_or_no_input(), False)
