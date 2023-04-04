import random
import json

from utilities.utilities import randomize_within_10_percent


def read_json(file):
    with open(file) as json_file:
        poke_dict = json.load(json_file)
    return poke_dict


def get_a_pokemon_by_location(board, character, enemy_name=None):
    current_biome = board[(character["X-coordinate"], character["Y-coordinate"])].strip()
    return get_location_pokemon(current_biome, enemy_name)


def get_pokemon_dict(character=None, board=None, search_parameter=None):
    """
    Gets pokemon data from a json file.

    A function that retrieves pokemon stat data from a json file using an optional search_parameter.
    @param character: a dictionary containing character data
    @param board: a dictionary containing board data
    @param search_parameter: an optional search parameter
    @precondition: character must be a dictionary containing 'X-coordinate' and 'Y-coordinate' as keys
    @precondition: board must be a dictionary containing tuples of coordinates (0, 0) as keys
    @precondition: search_parameter must be the string 'legendary' or a valid location on the board
    @postcondition: gets pokemon data from the relevant json file
    @return: a dictionary containing all pokemon data by search parameter or current location
    """
    if search_parameter is None:
        search_parameter = board[(character["X-coordinate"], character["Y-coordinate"])].strip()
    if search_parameter == 'Legendary':
        return read_json("json_data/boss_pokemon.json")
    else:
        return read_json(f"json_data/{search_parameter.lower()}_pokemon.json")


def get_location_pokemon(current_biome, pokemon=None):
    """
    Retrieves the stats of a random or specified pokemon in a given biome
    @param current_biome: a biome in which pokemon exist
    @param pokemon: an optional specific pokemon to retrieve from the biome
    @precondition: biome must be a string
    @precondition: biome must be identifier of a json file that ends in _pokemon.json
    @precondition: pokemon must be a string
    @precondition: pokemon must be the name of a key in the specified json file
    @return: a dictionary containing the stats of a random or specified pokemon
    """
    all_pokemon = read_json(f"json_data/{current_biome}_pokemon.json")
    return retrieve_pokemon_from_json(all_pokemon, pokemon)


def retrieve_pokemon_from_json(all_pokemon, pokemon=None):
    """
    Retrieves a random or specified pokemon from a dictionary.
    @param all_pokemon: a dictionary containing pokemon names as keys and stats as values
    @param pokemon: an optional specific pokemon to retrieve from the dictionary
    @precondition: all_pokemon must be a dictionary containing pokemon names as keys and stats as values
    @precondition: pokemon must be a string
    @precondition: pokemon must be the name of a key in all_pokemon
    @return: a dictionary containing the stats of a random or specified pokemon
    """
    while True:
        if pokemon is None:
            pokemon_dict = {}
            pokemon_name = random.choice(list(all_pokemon.keys()))
            pokemon_dict[pokemon_name] = all_pokemon[pokemon_name]
        else:
            pokemon_dict = {}
            pokemon_name = pokemon
            pokemon_dict[pokemon_name] = all_pokemon[pokemon_name]
        pokemon_dict[pokemon_name]["Current HP"] = randomize_within_10_percent(pokemon_dict[pokemon_name]["Current HP"])
        if pokemon_dict[pokemon_name]["Class"] == "Legendary":
            if one_in_number_odds(5):
                return pokemon_dict
            else:
                continue
        return pokemon_dict


def one_in_number_odds(number):
    """
    Returns True with one in number probability.
    @param number: a positive integer >= 1
    @precondition: number be a positive integer >= 1
    @return: True with probability one in number, else False
    """
    if random.randint(1, number) == 1:
        return True
    else:
        return False
