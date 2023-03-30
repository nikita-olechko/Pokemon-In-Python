import random

from misc.misc import random_multiplier
from pokemon.pokemon import forest_pokemon, ocean_pokemon, mine_pokemon, volcano_pokemon


def get_random_pokemon(board, character):
    current_biome = board[(character["X-coordinate"], character["Y-coordinate"])][:-1]
    if current_biome == 'Forest':
        return get_forest_pokemon()
    if current_biome == 'Ocean':
        return get_ocean_pokemon()
    if current_biome == 'Mine':
        return get_mine_pokemon()
    if current_biome == 'Volcano':
        return get_volcano_pokemon()


def get_pokemon_list(board, character):
    current_biome = board[(character["X-coordinate"], character["Y-coordinate"])][:-1]
    if current_biome == 'Forest':
        return forest_pokemon()
    if current_biome == 'Ocean':
        return ocean_pokemon()
    if current_biome == 'Mine':
        return mine_pokemon()
    if current_biome == "'Volcano'":
        return volcano_pokemon()


def get_ocean_pokemon():
    while True:
        random_pokemon = random.choice(list(ocean_pokemon().keys()))
        pokemon = ocean_pokemon()[random_pokemon]
        pokemon["Current HP"] = random_multiplier(pokemon["Current HP"])
        if pokemon["Class"] == "Legendary":
            if legendary_check_odds():
                return pokemon
            else:
                continue
        return pokemon


def get_mine_pokemon():
    while True:
        random_pokemon = random.choice(list(mine_pokemon().keys()))
        pokemon = mine_pokemon()[random_pokemon]
        pokemon["Current HP"] = random_multiplier(pokemon["Current HP"])
        if pokemon["Class"] == "Legendary":
            if legendary_check_odds():
                return pokemon
            else:
                continue
        return pokemon


def get_volcano_pokemon():
    while True:
        random_pokemon = random.choice(list(volcano_pokemon().keys()))
        pokemon = volcano_pokemon()[random_pokemon]
        pokemon["Current HP"] = random_multiplier(pokemon["Current HP"])
        if pokemon["Class"] == "Legendary":
            if legendary_check_odds():
                return pokemon
            else:
                continue
        return pokemon


def get_forest_pokemon():
    while True:
        random_pokemon = random.choice(list(forest_pokemon().keys()))
        pokemon = forest_pokemon()[random_pokemon]
        pokemon["Current HP"] *= random_multiplier(pokemon["Current HP"])
        if pokemon["Class"] == "Legendary":
            if legendary_check_odds():
                return pokemon
            else:
                continue
        return random_pokemon


def legendary_check_odds():
    if random.randint(1, 5) == 1:
        return True
    else:
        return False
