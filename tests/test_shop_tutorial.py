import io
from unittest import TestCase
from unittest.mock import patch

from character.shop import shop_tutorial


class TestShopTutorial(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_shop_tutorial(self, mock_output):
        shop_tutorial()
        system_printed = mock_output.getvalue()
        expected_output = "⬛🟥🟥🟥🟥🟥⬛⬛🟥🟥🟥🟥🟥⬛" in system_printed
        self.assertEqual(expected_output, True)
