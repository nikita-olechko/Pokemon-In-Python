import random

from pokemon.pokemon import forest_pokemon


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
    pass


def get_mine_pokemon():
    pass


def get_volcano_pokemon():
    pass


def get_forest_pokemon():
    while True:
        pokemon = forest_pokemon()
        if pokemon["Class"] == "Legendary":
            if legendary_check_odds(pokemon):
                return pokemon
            else:
                continue
        return pokemon


def legendary_check_odds(pokemon):
    if random.randint(1, 5) == 1:
        return True
    else:
        return False
