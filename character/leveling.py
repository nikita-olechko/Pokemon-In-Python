from playsound import playsound

from utilities.display import display_pokemon
from utilities.utilities import print_rolling_dialogue, randomize_within_10_percent
from pokemon.finding_pokemon import get_pokemon_dict


def print_evolution(pokemon, new_pokemon):
    """
    Prints evolution dialogue.
    :param pokemon: the old pokemon evolving
    :param new_pokemon: the pokemon being evolved into
    :precondition: pokemon must be a string
    :precondition: new_pokemon must be a string
    :raise: TypeError if pokemon or new_pokemon not a string
    """
    if type(pokemon) != str or type(new_pokemon) != str:
        raise TypeError("pokemon and new_pokemon must both be strings")
    print_rolling_dialogue(". . . ", delay=0.25)
    print_rolling_dialogue("What's this?? ", new_line=False)
    print_rolling_dialogue(". . . ", delay=0.10)
    print_rolling_dialogue(pokemon, delay=0.10, new_line=False)
    print_rolling_dialogue(" is evolving!", delay=0.10)
    print_rolling_dialogue(pokemon, delay=0.1, new_line=False)
    print_rolling_dialogue(" has evolved into ", delay=0.1, new_line=False)
    print_rolling_dialogue(new_pokemon, new_line=False)
    print_rolling_dialogue("!", delay=0.1)
    print_rolling_dialogue(new_pokemon, new_line=False)
    print_rolling_dialogue(" has more HP and new moves!")


def evolve(pokemon_inventory):
    """
    Evolves pokemon.

    A function that evolves all pokemon in pokemon_inventory that can be evolved into the next evolution.
    :param pokemon_inventory: a dictionary containing pokemon names as keys and stats as values
    :precondition: pokemon inventory must be a a dictionary containing pokemon names as keys and stats as values
    :postcondition: evolves all possible pokemon in pokemon_dictionary and updates their stats accordingly
    :raise: TypeError if pokemon_inventory is not a dictionary
    """
    if type(pokemon_inventory) != dict:
        raise TypeError("pokemon_inventory must be a dictionary")
    playsound('music/Evolution.wav', block=False)
    inventory_copy = pokemon_inventory.copy()
    for pokemon, value in inventory_copy.items():
        for key, stat_value in value.items():
            stat_value = str(stat_value).lower()
            if stat_value == pokemon.lower():
                current_evolution = key
                evolution_one(current_evolution, pokemon_inventory, pokemon, value)
                evolution_two(current_evolution, pokemon_inventory, pokemon, value)
    display_pokemon(pokemon_inventory)


def evolution_one(current_evolution, pokemon_inventory, pokemon, value):
    """
    Evolves first evolution.

    A function that evolves the first evolution of a pokemon into the next evolution, if possible.
    :param current_evolution: the current evolution of a pokemon
    :param pokemon_inventory: a dictionary containing pokemon names as keys and stats as values
    :param pokemon: the name of the pokemon being evolved
    :param value: a dictionary containing the stats of the pokemon being evolved
    :precondition: current_evolution must be a string containing the current evolution of a pokemon
    :precondition: pokemon inventory must be a a dictionary containing pokemon names as keys and stats as values
    :precondition: pokemon must be the name of the pokemon being evolved
    :precondition: value must be a dictionary containing the stats of the pokemon being evolved
    :postcondition: if possible, evolves the second evolution pokemon in
        pokemon_dictionary and updates their stats accordingly
    :raise: TypeError if current_evolution or pokemon not a string
    :raise: TypeError if pokemon_inventory or value not dictionaries
    """
    if type(pokemon_inventory) != dict or type(value) != dict:
        raise TypeError("pokemon_inventory and value must be dictionaries")
    if type(current_evolution) != str or type(pokemon) != str:
        raise TypeError("current_evolution and pokemon must be strings")
    if current_evolution == 'Evolution-One' and pokemon_inventory[pokemon]['Evolution-Two'].strip() != "":
        new_pokemon = pokemon_inventory[pokemon]['Evolution-Two'].lower()
        pokemon_inventory[new_pokemon] = get_pokemon_dict(search_parameter=value["Location"])[new_pokemon]
        pokemon_inventory.pop(pokemon)
        print_evolution(pokemon.title(), new_pokemon.title())


def evolution_two(current_evolution, pokemon_inventory, pokemon, value):
    """
    Evolves second evolution.

    A function that evolves the second evolution of a pokemon into the next evolution, if possible.
    :param current_evolution: the current evolution of a pokemon
    :param pokemon_inventory: a dictionary containing pokemon names as keys and stats as values
    :param pokemon: the name of the pokemon being evolved
    :param value: a dictionary containing the stats of the pokemon being evolved
    :precondition: current_evolution must be a string containing the current evolution of a pokemon
    :precondition: pokemon inventory must be a a dictionary containing pokemon names as keys and stats as values
    :precondition: pokemon must be the name of the pokemon being evolved
    :precondition: a dictionary containing the stats of the pokemon being evolved
    :postcondition: if possible, evolves the second evolution pokemon in
        pokemon_dictionary and updates their stats accordingly
    :raise: TypeError if current_evolution or pokemon not a string
    :raise: TypeError if pokemon_inventory or value not dictionaries
    """
    if type(pokemon_inventory) != dict or type(value) != dict:
        raise TypeError("pokemon_inventory and value must be dictionaries")
    if type(current_evolution) != str or type(pokemon) != str:
        raise TypeError("current_evolution and pokemon must be strings")
    if current_evolution == 'Evolution-Two' and pokemon_inventory[pokemon]['Evolution-Three'].strip() != "":
        new_pokemon = pokemon_inventory[pokemon]['Evolution-Three'].lower()
        pokemon_inventory[new_pokemon] = get_pokemon_dict(search_parameter=value["Location"])[new_pokemon]
        pokemon_inventory.pop(pokemon)
        print_evolution(pokemon.title(), new_pokemon.title())


def level_up(character):
    """
    Levels up character.

    A function that levels up a character if they have enough EXP.
    :param character: a dictionary containing character stats
    :precondition: character must be a dictionary
    :precondition: character must contain "EXP" and "Level" as keys and integers as values
    :postcondition: levels up character if character has enough EXP
    :return: True if character levels up, else False
    :raise: TypeError if character is not a dictionary
    :raise: ValueError if "EXP" or "Level" are not keys in character
    >>> character_dict = {"EXP": 100, "Level": 1}
    >>> level_up(character_dict)
    You have leveled up!
    Current Level: 2
    True
    >>> character_dict = {"EXP": 200, "Level": 2}
    >>> level_up(character_dict)
    You have leveled up!
    Current Level: 3
    True
    >>> character_dict = {"EXP": 50, "Level": 1}
    >>> level_up(character_dict)
    False
    """
    if type(character) != dict:
        raise TypeError("character must be a dictionary")
    if "EXP" not in character.keys() or "Level" not in character.keys():
        raise ValueError("character must contain the keys 'EXP' and 'Level'")
    if character["EXP"] >= 100*character["Level"]:
        character["EXP"] -= 100*character["Level"]
        character["Level"] += 1
        print(f"You have leveled up!\nCurrent Level: {character['Level']}")
        return True
    return False


def gain_stats(character):
    """
    Increases character EXP and Gold.

    A function that increase character EXP and Gold by 50 each within a margin of 10%.
    :param character: a dictionary containing character stats
    :precondition: character must be a dictionary containing "EXP" and "Gold" as keys and integers as values
    :postcondition: increases character EXP and Gold values
    :return: dictionary with "exp_gain" and "gold_gain" as keys and their respective increases as values
    :raise: TypeError if character is not a dictionary
    :raise: ValueError if "EXP" or "Level" or "Gold" are not keys in character
    """
    if type(character) != dict:
        raise TypeError("character must be a dictionary")
    if "EXP" not in character.keys() or "Level" not in character.keys() or "Gold" not in character.keys():
        raise ValueError("character must contain the keys 'EXP', 'Level', and 'Gold'")
    stat_gain = {"exp_gain": randomize_within_10_percent(50), "gold_gain": randomize_within_10_percent(50)}
    character["EXP"] += int(stat_gain["exp_gain"] * (character["Level"] * 0.75))
    character["Gold"] += int(stat_gain["gold_gain"])
    return stat_gain


def main():
    """
    Drives the program.
    """


if __name__ == "__main__":
    main()
