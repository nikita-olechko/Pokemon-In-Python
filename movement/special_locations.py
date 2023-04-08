import time

from playsound import playsound

from utilities.display import display_pokemon
from utilities.utilities import print_rolling_dialogue
from pokemon.finding_pokemon import get_pokemon_dict


def at_shop(character: dict) -> bool:
    """
    Checks whether character is at the shop.
    :param character: a dictionary containing character stats
    :precondition: character must be a dictionary containing "X-coordinate" and "Y-coordinate"
    :return: True if at shop, else False
    :raise: TypeError if character not a dictionary
    >>> player = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> at_shop(player)
    False
    >>> player = {"X-coordinate": 1, "Y-coordinate": 0}
    >>> at_shop(player)
    True
    """
    if type(character) != dict:
        raise TypeError("character must be a dictionary")
    if (character["X-coordinate"], character["Y-coordinate"]) == (1, 0):
        return True
    else:
        return False


def at_arceus(character: dict) -> bool:
    """
    Checks whether character is at Arceus.
    :param character: a dictionary containing character stats
    :precondition: character must be a dictionary containing "X-coordinate" and "Y-coordinate"
    :return: True if at Arceus, else False
    :raise: TypeError if character not a dictionary
    >>> player = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> at_arceus(player)
    False
    >>> player = {"X-coordinate": 4, "Y-coordinate": 0}
    >>> at_arceus(player)
    True
    """
    if type(character) != dict:
        raise TypeError("character must be a dictionary")
    if (character["X-coordinate"], character["Y-coordinate"]) == (4, 0):
        return True
    else:
        return False


def at_hospital(character: dict) -> bool:
    """
    Checks whether character is at the hospital.
    :param character: a dictionary containing character stats
    :precondition: character must be a dictionary containing "X-coordinate" and "Y-coordinate"
    :return: True if at hospital, else False
    :raise: TypeError if character not a dictionary
    >>> player = {"X-coordinate": 2, "Y-coordinate": 0}
    >>> at_hospital(player)
    False
    >>> player = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> at_hospital(player)
    True
    """
    if type(character) != dict:
        raise TypeError("character must be a dictionary")
    if (character["X-coordinate"], character["Y-coordinate"]) == (0, 0):
        return True
    else:
        return False


def at_special_location(character: dict) -> bool:
    """
    Checks whether character is at a special location.
    :param character: a dictionary containing character stats
    :precondition: character must be a dictionary containing "X-coordinate" and "Y-coordinate"
    :return: True if at special location, else False
    :raise: TypeError if character not a dictionary
    >>> player = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> at_special_location(player)
    True
    >>> player = {"X-coordinate": 1, "Y-coordinate": 0}
    >>> at_special_location(player)
    True
    >>> player = {"X-coordinate": 2, "Y-coordinate": 0}
    >>> at_special_location(player)
    False
    """
    if type(character) != dict:
        raise TypeError("character must be a dictionary")
    if at_shop(character) or at_arceus(character) or at_hospital(character):
        return True
    else:
        return False


def beat_the_game():
    """
    Prints beating the game lore after you beat the game.
    :postcondition: prints beating the game lore and plays music
    """
    playsound("music\\Beat-The-Game.wav", block=False)
    time.sleep(3)
    print_rolling_dialogue(". . . \n", delay=1)
    time.sleep(2)
    print_rolling_dialogue("(you hear a voice inside your head)\n")
    print_rolling_dialogue("You have done well, Mortal. A God is not so easily defeated.\n", delay=0.10)
    print_rolling_dialogue(". . . ", delay=1)
    print_rolling_dialogue("But the world must always have a God\n", delay=0.10)
    print_rolling_dialogue(". . . \n", delay=1)
    print_rolling_dialogue("and so that must be you.\n", delay=0.10)
    print_rolling_dialogue(". . . \n", delay=1)
    print_rolling_dialogue("You shall take my place atop this Volcano, and watch over all.", delay=0.10)
    print_rolling_dialogue("and I . . . ", delay=0.5, new_line=False)
    print_rolling_dialogue("I shall rest in peace.", delay=0.2, new_line=False)
    time.sleep(50)


def reset_health(pokemon_inventory: dict) -> None:
    """
    Resets the health of all pokemon in pokemon_inventory.
    :param pokemon_inventory: a dictionary containing pokemon names as keys and stats as values
    :precondition: pokemon inventory must be a dictionary containing pokemon names as keys and stats as values
    :postcondition: resets the HP of all pokemon in pokemon_inventory
    :raise: TypeError if pokemon_inventory not a dictionary
    """
    if type(pokemon_inventory) != dict:
        raise TypeError("pokemon_inventory must be a dictionary")
    playsound("music/Pokemon Recovery.wav", block=False)
    for pokemon in pokemon_inventory:
        location = pokemon_inventory[pokemon]["Location"]
        pokemon_dict = get_pokemon_dict(search_parameter=location)
        full_hp = pokemon_dict[pokemon.lower()]['Current HP']
        pokemon_inventory[pokemon]['Current HP'] = full_hp
    print_rolling_dialogue("\nYour Pokémon have been healed!\n")
    display_pokemon(pokemon_inventory)


def main():
    """
    Drives the program.
    """


if __name__ == "__main__":
    main()
