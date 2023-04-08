from unittest import TestCase

from utilities.utilities import read_json


class TestReadJson(TestCase):
    def test_TypeError(self):
        with self.assertRaises(TypeError):
            read_json(1)
