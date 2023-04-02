from character.shop import enter_shop
from combat.combat import combat
from misc.misc import print_rolling_dialogue
from pokemon.finding_pokemon import get_pokemon_dict


def at_shop(character):
    if (character["X-coordinate"], character["Y-coordinate"]) == (1, 0):
        return True


def at_arceus(character):
    if (character["X-coordinate"], character["Y-coordinate"]) == (4, 4):
        return True
    else:
        return False


def at_hospital(character):
    if (character["X-coordinate"], character["Y-coordinate"]) == (0, 0):
        return True
    else:
        return False


# def at_ocean(character):
#     ocean_locations = ((2, 0), (2, 1), (2, 2), (2, 3), (2, 4))
#     if (character["X-coordinate"], character["Y-coordinate"]) in ocean_locations:
#         return True
#     else:
#         return False


def at_special_location(character):
    if at_shop(character) or at_arceus(character) or at_hospital(character):
        return True
    else:
        return False


def beat_the_game():
    print_rolling_dialogue("You Win.")


def reset_health(pokemon_inventory, board, character):
    for pokemon, stats in pokemon_inventory:
        location = stats["Location"]
        pokemon_dict = get_pokemon_dict(board, character, search_parameter=location)
        full_hp = pokemon_dict[pokemon.lower()]['Current HP']
        pokemon_inventory[pokemon]['Current HP'] = full_hp


def special_locations_sequence(character, board, pokemon_inventory):
    if at_shop(character):
        enter_shop(character)
        return
    elif at_arceus(character):
        if combat(character, board, pokemon_inventory, enemy_name='Arceus'):
            character['Victory'] = True
            beat_the_game()
        else:
            character['Current HP'] = 0
    else:
        reset_health(pokemon_inventory, board, character)
