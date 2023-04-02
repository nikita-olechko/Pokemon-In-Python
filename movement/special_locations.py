from playsound import playsound

from character.shop import enter_shop
from combat.combat import get_combat_details, combat_loop
from utilities.utilities import print_rolling_dialogue
from pokemon.finding_pokemon import get_pokemon_dict


def at_shop(character):
    if (character["X-coordinate"], character["Y-coordinate"]) == (1, 0):
        return True


def at_arceus(character):
    if (character["X-coordinate"], character["Y-coordinate"]) == (4, 0):
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
    playsound("music/beat-the-game.wav", block=False)
    print_rolling_dialogue("You Win.")


def reset_health(pokemon_inventory, board, character):
    for pokemon in pokemon_inventory:
        location = pokemon_inventory[pokemon]["Location"]
        pokemon_dict = get_pokemon_dict(board, character, search_parameter=location)
        full_hp = pokemon_dict[pokemon.lower()]['Current HP']
        pokemon_inventory[pokemon]['Current HP'] = full_hp
    print_rolling_dialogue("\nYour Pokémon have been healed!\n")


def special_locations_sequence(character, board, pokemon_inventory):
    if at_shop(character):
        enter_shop(character)
        return
    elif at_arceus(character):
        combat_details = get_combat_details(character, board, pokemon_inventory, enemy_name='arceus')
        if combat_loop(combat_details["character"], combat_details["board"],
                       combat_details["pokemon_inventory"], combat_details["enemy_name"],
                       combat_details["enemy_stats"], combat_details["current_pokemon"]):
            character['Victory'] = True
            beat_the_game()
        else:
            character['Current HP'] = 0
    else:
        reset_health(pokemon_inventory, board, character)
