import json
import random
import time


def randomize_within_10_percent(number_to_multiply):
    number = random.choice([0.90, 0.92, 0.94, 0.96, 0.98, 1.0, 1.02, 1.04, 1.06, 1.08, 1.1])
    rounded_number = int(round(number*number_to_multiply))
    return rounded_number


def print_dialogue(string, delay=0.03, new_line=True):
    dialogue = string.split(sep="\n")
    for index, line in enumerate(dialogue):
        if index == 0:
            print(line)
            continue
        line += "\n"
        time.sleep(1)
        for char in line:
            time.sleep(delay)
            print(char, end="")
    if new_line:
        print("")


def print_rolling_dialogue(string, delay=0.03, new_line=True):
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
    >>> all_prefixes("Pythonic")
    ['P', 'Py', 'Pyt', 'Pyth', 'Pytho', 'Python', 'Pythoni', 'Pythonic']
    >>> all_prefixes("")
    []
    >>> all_prefixes("a")
    ['a']
    """
    if len(string) == 0:
        return []
    prefixes = [string[0]]
    for prefix in all_prefixes(string[1:]):
        prefixes.append(string[0] + prefix)
    return prefixes


def read_and_write_json(file):
    with open(file) as json_file:
        poke_dict = json.load(json_file)
    for pokemon in poke_dict:
        poke_dict[pokemon]["Current HP"] *= 2.5
        poke_dict[pokemon]["Current HP"] = int(poke_dict[pokemon]["Current HP"])
    with open(file, "w") as json_file:
        json.dump(poke_dict, json_file)


def display_pokemon(pokemon_inventory):
    list_of_pokemon = "| "
    for index, pokemon in enumerate(pokemon_inventory):
        list_of_pokemon += f"{index + 1}: {pokemon.title()}, "
        list_of_pokemon += f"Current HP: {pokemon_inventory[pokemon]['Current HP']} | "
    print(f"\n\t{list_of_pokemon}\n")