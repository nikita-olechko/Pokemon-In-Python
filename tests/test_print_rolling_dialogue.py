import io
from unittest import TestCase
from unittest.mock import patch

from utilities.utilities import print_rolling_dialogue


class TestPrintRollingDialogue(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_output_new_line(self, mock_output):
        print_rolling_dialogue("Hello")
        system_printed = mock_output.getvalue()
        expected = "Hello\n\n"
        self.assertEqual(expected, system_printed)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_output_no_line(self, mock_output):
        print_rolling_dialogue("Hello", new_line=False)
        system_printed = mock_output.getvalue()
        expected = "Hello"
        self.assertEqual(expected, system_printed)

    def test_TypeError(self):
        with self.assertRaises(TypeError):
            print_rolling_dialogue(1)
