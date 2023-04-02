from combat.combat import display_pokemon
from pokemon.pokemon import starter_pokemon_dict


def choose_starter_pokemon():
    starters_evolution_1 = ['bulbasaur', 'charmander', 'squirtle']
    starter_dict = {}
    for pokemon in starters_evolution_1:
        starter_dict[pokemon] = starter_pokemon_dict()[pokemon]
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
    pokemon = {pokemon: starter_pokemon_dict()[pokemon]}
    return pokemon


def achieved_goal(character):
    if character['Victory']:
        return True
    else:
        return False
