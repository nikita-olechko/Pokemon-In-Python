import random

from pokemon.pokemon import forest_pokemon, ocean_pokemon, mine_pokemon, volcano_pokemon


def get_random_pokemon(board, character):
    current_biome = board[(character["X-coordinate"], character["Y-coordinate"])]
    if current_biome == "Forest":
        return get_forest_pokemon()
    if current_biome == "Ocean":
        return get_ocean_pokemon()
    if current_biome == "Mine":
        return get_mine_pokemon()
    if current_biome == "Volcano":
        return get_volcano_pokemon()


def get_ocean_pokemon():
    while True:
        pokemon = ocean_pokemon()
        if pokemon["Class"] == "Legendary":
            if legendary_check_odds():
                return pokemon
            else:
                continue
        return pokemon


def get_mine_pokemon():
    while True:
        pokemon = mine_pokemon()
        if pokemon["Class"] == "Legendary":
            if legendary_check_odds():
                return pokemon
            else:
                continue
        return pokemon


def get_volcano_pokemon():
    while True:
        pokemon = volcano_pokemon()
        if pokemon["Class"] == "Legendary":
            if legendary_check_odds():
                return pokemon
            else:
                continue
        return pokemon


def get_forest_pokemon():
    while True:
        pokemon = forest_pokemon()
        if pokemon["Class"] == "Legendary":
            if legendary_check_odds():
                return pokemon
            else:
                continue
        return pokemon


def legendary_check_odds():
    if random.randint(1, 5) == 1:
        return True
    else:
        return False
