from pokemon.finding_pokemon import read_json
from utilities.display import display_pokemon


def choose_starter_pokemon():
    """
    Choose starter pokemon

    A function that asks the user to choose a starter pokemon.
    :postcondition: gets a starter pokemon from the user
    :return: name of a starter pokemon as a string
    """
    starters_evolution_1 = ['bulbasaur', 'charmander', 'squirtle']
    starter_dict = {}
    for pokemon in starters_evolution_1:
        starter_dict[pokemon] = read_json("json_data/starter_pokemon.json")[pokemon]
    display_pokemon(starter_dict)
    while True:
        chosen_pokemon = input("Choose a starter Pokemon: ").lower()
        if chosen_pokemon not in starters_evolution_1 and chosen_pokemon not in ["1", "2", "3"]:
            print("That's not one of the starter Pokemon! Pick again.")
            continue
        elif chosen_pokemon in starters_evolution_1:
            return chosen_pokemon
        else:
            return starters_evolution_1[int(chosen_pokemon)-1]


def make_character(tutorial_bool):
    """
    Make a character.

    A function that creates a new character at the starting coordinates (0, 0) with 5 HP.
    :postcondition: creates a character
    :return: dictionary with starting character values
    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    """
    character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5, "EXP": 0, "Level": 1, "Boat": False,
                 "Pokeballs": 2, "Gold": 100, "Tutorial": False, "Victory": False}
    if tutorial_bool:
        character['Tutorial'] = True
    return character


def get_starter_pokemon(pokemon):
    """
    Retrieve data of a given starter pokemon.
    :param: the name of a pokemon as a string
    :precondition: pokemon must be a string
    :precondition: pokemon must a key in json_data/starter_pokemon.json
    :return: dictionary of specified starter pokemon stats
    >>> get_starter_pokemon('charmander')

    """
    pokemon = {pokemon: read_json("json_data/starter_pokemon.json")[pokemon]}
    return pokemon


def achieved_goal(character):
    if character['Victory']:
        return True
    else:
        return False
