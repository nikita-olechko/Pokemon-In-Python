import io
from unittest import TestCase
from unittest.mock import patch

from character.saving import prompt_load_old_save


class TestPromptLoadOldSave(TestCase):
    @patch('builtins.input', side_effect=["y"])
    def test_yes(self, _):
        self.assertEqual(True, prompt_load_old_save())

    @patch('builtins.input', side_effect=["n"])
    def test_no(self, _):
        self.assertEqual(False, prompt_load_old_save())

    @patch('builtins.input', side_effect=["y"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output(self, mock_output, _):
        prompt_load_old_save()
        output_is_this = mock_output.getvalue()
        expected_output = "Would you like to load a save file? "
        self.assertEqual(expected_output, output_is_this)
