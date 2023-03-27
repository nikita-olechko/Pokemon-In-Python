"""
Nikita Olechko
A01337397
"""
import io
from unittest import TestCase
from unittest.mock import patch

from game import death


class TestDeath(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_death(self, mock_stout):
        death()
        expected = "Welp, you've died. Wow, that's impressive, this really wasn't a hard game. Better luck next time!\n"
        self.assertEqual(mock_stout.getvalue(), expected)
