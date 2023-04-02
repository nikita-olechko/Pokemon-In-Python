import random

from misc.misc import randomize_within_10_percent


from pokemon.pokemon import forest_pokemon, ocean_pokemon, mine_pokemon, volcano_pokemon


def get_a_pokemon(board, character, *args):
    current_biome = board[(character["X-coordinate"], character["Y-coordinate"])][:-1]
    if current_biome == 'Forest':
        return get_forest_pokemon(*args)
    if current_biome == 'Ocean':
        return get_ocean_pokemon(*args)
    if current_biome == 'Mine':
        return get_mine_pokemon(*args)
    if current_biome == 'Volcano':
        return get_volcano_pokemon(*args)


def get_pokemon_dict(character, board=None, search_parameter=None):
    if search_parameter is None:
        search_parameter = board[(character["X-coordinate"], character["Y-coordinate"])][:-1]
    if search_parameter == 'Forest':
        return forest_pokemon()
    if search_parameter == 'Ocean':
        return ocean_pokemon()
    if search_parameter == 'Mine':
        return mine_pokemon()
    if search_parameter == 'Volcano':
        return volcano_pokemon()


def get_ocean_pokemon(pokemon=None):
    while True:
        if pokemon is None:
            pokemon = random.choice(list(ocean_pokemon().keys()))
        pokemon = ocean_pokemon()[pokemon]
        pokemon["Current HP"] = randomize_within_10_percent(pokemon["Current HP"])
        if pokemon["Class"] == "Legendary":
            if one_in_n_odds(5):
                return pokemon
            else:
                continue
        return pokemon


def get_mine_pokemon(pokemon=None):
    while True:
        if pokemon is None:
            pokemon = random.choice(list(mine_pokemon().keys()))
        pokemon = mine_pokemon()[pokemon]
        pokemon["Current HP"] = randomize_within_10_percent(pokemon["Current HP"])
        if pokemon["Class"] == "Legendary":
            if one_in_n_odds(5):
                return pokemon
            else:
                continue
        return pokemon


def get_volcano_pokemon(pokemon=None):
    while True:
        if pokemon is None:
            pokemon = random.choice(list(volcano_pokemon().keys()))
        pokemon = volcano_pokemon()[pokemon]
        pokemon["Current HP"] = randomize_within_10_percent(pokemon["Current HP"])
        if pokemon["Class"] == "Legendary":
            if one_in_n_odds(5):
                return pokemon
            else:
                continue
        return pokemon


def get_forest_pokemon(pokemon: str = None) -> dict:
    while True:
        if pokemon is None:
            pokemon = {}
            pokemon_name = random.choice(list(forest_pokemon()))
            pokemon[pokemon_name] = forest_pokemon()[pokemon_name]
        else:
            pokemon = forest_pokemon()[pokemon]
            pokemon_name = list(pokemon.keys())[0]
        pokemon[pokemon_name]["Current HP"] = randomize_within_10_percent(pokemon[pokemon_name]["Current HP"])
        if pokemon[pokemon_name]["Class"] == "Legendary":
            if one_in_n_odds(5):
                return pokemon
            else:
                continue
        return pokemon


def one_in_n_odds(n):
    if random.randint(1, n) == 1:
        return True
    else:
        return False
