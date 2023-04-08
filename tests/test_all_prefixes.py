"""
Nikita Olechko
A01337397
"""


from unittest import TestCase

from utilities.utilities import all_prefixes


class TestIsPalindrome(TestCase):
    def test_even_word(self):
        self.assertEqual(all_prefixes("Python"), ['P', 'Py', 'Pyt', 'Pyth', 'Pytho', 'Python'])

    def test_odd_character(self):
        self.assertEqual(all_prefixes("PyCharm"), ['P', 'Py', 'PyC', 'PyCh', 'PyCha', 'PyChar', 'PyCharm'])

    def test_two_words(self):
        self.assertEqual(all_prefixes("Bob cat"), ['B', 'Bo', 'Bob', 'Bob ', 'Bob c', 'Bob ca', 'Bob cat'])

    def test_special_characters(self):
        self.assertEqual(all_prefixes("Bob's cat!"),
                         ['B', 'Bo', 'Bob', 'Bob\'', 'Bob\'s',  'Bob\'s ', 'Bob\'s c', 'Bob\'s ca', 'Bob\'s cat',
                          'Bob\'s cat!'])

    def test_empty_string(self):
        self.assertEqual(all_prefixes(""), [])

    def test_single_character(self):
        self.assertEqual(all_prefixes("P"), ['P'])

    def test_TypeError(self):
        with self.assertRaises(TypeError):
            all_prefixes(1)
