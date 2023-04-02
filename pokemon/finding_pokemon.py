import random
import json

from utilities.utilities import randomize_within_10_percent


def open_json(file):
    with open(file) as json_file:
        poke_dict = json.load(json_file)
    return poke_dict


def get_a_random_pokemon_by_location(board, character, enemy_name=None):
    current_biome = board[(character["X-coordinate"], character["Y-coordinate"])].strip()
    if current_biome == 'Forest':
        return get_forest_pokemon(enemy_name)
    if current_biome == 'Ocean':
        return get_ocean_pokemon(enemy_name)
    if current_biome == 'Mine':
        return get_mine_pokemon(enemy_name)
    if current_biome == 'Volcano':
        return get_volcano_pokemon(enemy_name)
    if current_biome == 'Plains':
        return get_plains_pokemon(enemy_name)


def get_pokemon_dict(character=None, board=None, search_parameter=None):
    if search_parameter is None:
        search_parameter = board[(character["X-coordinate"], character["Y-coordinate"])].strip()
    if search_parameter == 'Forest':
        return open_json("json_data/forest_pokemon.json")
    if search_parameter == 'Ocean':
        return open_json("json_data/ocean_pokemon.json")
    if search_parameter == 'Mine':
        return open_json("json_data/mine_pokemon.json")
    if search_parameter == 'Volcano':
        return open_json("json_data/volcano_pokemon.json")
    if search_parameter == 'Plains':
        return open_json("json_data/plains_pokemon.json")
    if search_parameter == 'Legendary':
        return open_json("json_data/boss_pokemon.json")
    else:
        return open_json("json_data/starter_pokemon.json")


def get_ocean_pokemon(pokemon=None):
    all_pokemon = open_json("json_data/ocean_pokemon.json")
    return retrieve_pokemon_from_json(all_pokemon, pokemon)


def get_mine_pokemon(pokemon=None):
    all_pokemon = open_json("json_data/mine_pokemon.json")
    return retrieve_pokemon_from_json(all_pokemon, pokemon)


def get_volcano_pokemon(pokemon=None):
    all_pokemon = open_json("json_data/volcano_pokemon.json")
    return retrieve_pokemon_from_json(all_pokemon, pokemon)


def get_plains_pokemon(pokemon: str = None) -> dict:
    all_pokemon = open_json("json_data/plains_pokemon.json")
    return retrieve_pokemon_from_json(all_pokemon, pokemon)


def get_forest_pokemon(pokemon: str = None) -> dict:
    all_pokemon = open_json("json_data/forest_pokemon.json")
    return retrieve_pokemon_from_json(all_pokemon, pokemon)


def retrieve_pokemon_from_json(all_pokemon, pokemon):
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
            if one_in_n_odds(5):
                return pokemon_dict
            else:
                continue
        return pokemon_dict


def one_in_n_odds(n):
    if random.randint(1, n) == 1:
        return True
    else:
        return False
