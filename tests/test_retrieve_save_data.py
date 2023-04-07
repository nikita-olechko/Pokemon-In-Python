from unittest import TestCase

from character.saving import retrieve_save_data


class TestCreateNewSave(TestCase):
    def test_TypeError(self):
        old_save_data = ["1", "2"]
        with self.assertRaises(TypeError):
            retrieve_save_data(old_save_data)

    def test_ValueError_username(self):
        old_save_data = {"Bob": "Username", "Password": "12343341"}
        with self.assertRaises(ValueError):
            retrieve_save_data(old_save_data)

    def test_ValueError_password(self):
        old_save_data = {"Username": "Username", "Bob": "12343341"}
        with self.assertRaises(ValueError):
            retrieve_save_data(old_save_data)
