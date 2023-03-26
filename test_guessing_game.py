"""
Nikita Olechko
A01337397
"""
import io
from unittest import TestCase
from unittest.mock import patch
from simple_game import guessing_game
from simple_game import make_character


class TestGuessingGame(TestCase):
    @patch('builtins.input', return_value="5")
    @patch('random.randint', return_value=5)
    @patch('random.choice', return_value=('Countess Coldblooded, the Cruel Crone', 'Cunning Crusader'))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_correct_number(self, mock_output, _, __, ___):
        character = make_character()
        guessing_game(character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "______________________________________________________________________________________" \
                          "__________\n" \
                          "Welcome Cunning Crusader. I am Countess Coldblooded, the Cruel Crone. " \
                          "Prepare to meet your doom!\n" \
                          "I have chosen a number between 1 and 5. You must guess what I picked or face my wrath!\n\n" \
                          "Damn, you survive another day. Begone from here!\n" \
                          "_________________________________________________\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', return_value="5")
    @patch('random.randint', return_value=3)
    @patch('random.choice', return_value=('Countess Coldblooded, the Cruel Crone', 'Cunning Crusader'))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_incorrect_number(self, mock_output, _, __, ___):
        character = make_character()
        guessing_game(character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "______________________________________________________________________________________" \
                          "__________\n" \
                          "Welcome Cunning Crusader. I am Countess Coldblooded, the Cruel Crone. " \
                          "Prepare to meet your doom!\n" \
                          "I have chosen a number between 1 and 5. You must guess what I picked or face my wrath!\n\n" \
                          "Fool! The number was obviously 3. Take this!\n" \
                          "Your HP has dropped to 4\n" \
                          "_________________________________________________\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', return_value="Lemon Pancakes")
    @patch('random.randint', return_value=3)
    @patch('random.choice', return_value=('Countess Coldblooded, the Cruel Crone', 'Cunning Crusader'))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_incorrect_input(self, mock_output, _, __, ___):
        character = make_character()
        guessing_game(character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "______________________________________________________________________________________" \
                          "__________\n" \
                          "Welcome Cunning Crusader. I am Countess Coldblooded, the Cruel Crone. " \
                          "Prepare to meet your doom!\n" \
                          "I have chosen a number between 1 and 5. You must guess what I picked or face my wrath!\n\n" \
                          "Fool! The number was obviously 3. Take this!\n" \
                          "Your HP has dropped to 4\n" \
                          "_________________________________________________\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', return_value="5")
    @patch('random.randint', return_value=3)
    @patch('random.choice', return_value=('Countess Coldblooded, the Cruel Crone', 'Cunning Crusader'))
    def test_hp_drain(self, _, __, ___):
        character = make_character()
        guessing_game(character)
        self.assertEqual(character, {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 4})
