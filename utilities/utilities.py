import json
import random
import time


def randomize_within_10_percent(number_to_randomize):
    """
    Randomizes a number in a 10% margin.

    A function that randomizes a number +/- 10%
    :param number_to_randomize: a number to randomize
    :precondition: number_to_randomize must be a float or an int
    :postcondition: randomizes number_to_randomize +/- 10%
    :return: number_to_randomize randomized +/- 10% as an integer
    :raise: TypeError if number_to_randomize is not a number
    """
    if type(number_to_randomize) != int and type(number_to_randomize) != float:
        raise TypeError("number_to_randomize must be an integer or float")
    number = random.choice([0.90, 0.92, 0.94, 0.96, 0.98, 1.0, 1.02, 1.04, 1.06, 1.08, 1.1])
    rounded_number = int(round(number * number_to_randomize))
    return rounded_number


def print_rolling_dialogue(string, delay=0.03, new_line=True):
    """
    Prints a string with a specified delay per character, with the default delay at 0.03 seconds.
    :param string: a string
    :param delay: an optional number representing the delay (in seconds) between each character in string
    :param new_line: an optional boolean indicating whether a new line should be printed at the end of string
    :precondition: string must be a string
    :precondition: delay must be a number
    :precondition: new_line must be a boolean operator
    :postcondition: prints string character by character with the specified delay
    :raise: TypeError if string is not a string
    """
    if type(string) != str:
        raise TypeError("string must be a string")
    for char in string:
        time.sleep(delay)
        print(char, end="")
    if new_line:
        print("\n")


def all_prefixes(string: str) -> list:
    """
    Return all prefixes of string.

    A function that creates a list of all non-empty substrings in string that start with the first character.
    :param string: a string
    :precondition: string must be a string
    :postcondition: determines all non-empty substrings of string that start with the first character of string
    :return: an ordered list of strings containing all substrings that start with the first character in string
    :raise: TypeError if string is not a string
    >>> all_prefixes("Pythonic")
    ['P', 'Py', 'Pyt', 'Pyth', 'Pytho', 'Python', 'Pythoni', 'Pythonic']
    >>> all_prefixes("")
    []
    >>> all_prefixes("a")
    ['a']
    """
    if type(string) != str:
        raise TypeError("string must be a string")
    if len(string) == 0:
        return []
    prefixes = [string[0]]
    for prefix in all_prefixes(string[1:]):
        prefixes.append(string[0] + prefix)
    return prefixes


def yes_or_no_input():
    """
    Prompts the user yes or no (y/n).
    :postcondition: gets user input on something
    :return: True if yes (y), False if no (n)
    """
    while True:
        do_tutorial = input("(y/n): ").lower()
        if do_tutorial == 'y':
            return True
        elif do_tutorial == 'n':
            return False
        else:
            print("Invalid input")
            continue


def read_json(file):
    """
    Returns data from a json file.
    :param file: the name of a json file
    :precondition: file must be the name of a json pile
    :precondition: file name must start from the root of the working directory
    :return: data inside the json file as a dictionary
    :raise: TypeError if file not a string
    """
    if type(file) != str:
        raise TypeError("file must be a string")
    with open(file) as json_file:
        file_dict = json.load(json_file)
    return file_dict


def one_in_number_odds(number):
    """
    Returns True with one in number probability.
    :param number: a positive integer >= 1
    :precondition: number be a positive integer >= 1
    :postcondition: returns True with one in number odds
    :return: True with probability one in number, else False
    :raise: TypeError if number is not an integer
    """
    if type(number) != int:
        raise TypeError("number must be an integer")
    if random.randint(1, number) == 1:
        return True
    else:
        return False
