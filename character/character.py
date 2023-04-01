from pokemon.pokemon import starter_pokemon_dict


def starter_pokemon():
    starters = ['bulbasaur', 'charmander', 'squirtle']
    while True:
        chosen_pokemon = input("Choose a starter Pokemon: ").lower()
        if chosen_pokemon not in starters:
            print("That's not one of the starter Pokemon! Pick again.")
            continue
        else:
            break
    return chosen_pokemon


def make_character(pokemon):
    """
    Make a character.

    A function that creates a new character at the starting coordinates (0, 0) with 5 HP.
    :postcondition: creates a character
    :return: dictionary with starting character values
    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    """
    character = {"Class": pokemon,
                 "X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5, "EXP": 0, "Level": 1, "Boat": False,
                 "Pokeballs": 0}
    return character


def get_starter_pokemon(pokemon):
    pokemon = {pokemon: starter_pokemon_dict()[pokemon]}
    return pokemon
