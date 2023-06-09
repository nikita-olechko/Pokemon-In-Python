import random

from character.leveling import gain_stats
from pokemon.capturing_pokemon import capture_pokemon
from utilities.display import display_pokemon, display_moves, choose_a_conscious_pokemon
from utilities.utilities import randomize_within_10_percent, read_json
from pokemon.finding_pokemon import get_a_pokemon_by_location, get_pokemon_dict


def your_move(current_pokemon: str, pokemon_inventory: dict) -> str:
    """
    Gets a move associated with a pokemon from the user.
    :param current_pokemon: a pokemon in pokemon_inventory
    :param pokemon_inventory: a dictionary containing pokemon names as keys and stats as values
    :precondition: pokemon must be a string
    :precondition: pokemon must be a key in pokemon_inventory
    :precondition: pokemon inventory must be a a dictionary containing pokemon names as keys and stats as values
    :postcondition: gets a valid move from the user
    :return: a valid move associated with current_pokemon as a string
    :raise: TypeError if pokemon_inventory not a dictionary
    :raise: TypeError if current_pokemon not a string
    :raise: KeyError if current_pokemon not in pokemon_inventory keys
    """
    if type(pokemon_inventory) != dict:
        raise TypeError("pokemon_inventory must be a dictionary")
    if type(current_pokemon) != str:
        raise TypeError("pokemon_name must be a string")
    if current_pokemon not in pokemon_inventory.keys():
        raise KeyError("pokemon_name must be a key in combat_pokemon_stats")
    move = display_moves(current_pokemon, pokemon_inventory)
    return move


def enemy_move(combat_pokemon_stats: dict, pokemon_name: str) -> str:
    """
    Picks a random enemy move.
    :param combat_pokemon_stats: stats associated with an enemy pokemon
    :param pokemon_name: the name of a pokemon
    :precondition: combat_pokemon_stats must be a dictionary containing at least one move ('Move-One')
    :precondition: pokemon_name must be a string
    :postcondition: gets a valid enemy move
    :return: an enemy move as a string
    :raise: TypeError if combat_pokemon_stats not a dictionary
    :raise: TypeError if pokemon_name not a string
    :raise: KeyError if pokemon_name not in combat_pokemon_stats keys
    """
    if type(combat_pokemon_stats) != dict:
        raise TypeError("pokemon_inventory must be a dictionary")
    if type(pokemon_name) != str:
        raise TypeError("pokemon_name must be a string")
    if pokemon_name not in combat_pokemon_stats.keys():
        raise KeyError("pokemon_name must be a key in combat_pokemon_stats")
    moves = [combat_pokemon_stats[pokemon_name]['Move-One'], combat_pokemon_stats[pokemon_name]['Move-Two'],
             combat_pokemon_stats[pokemon_name]['Move-Three'], combat_pokemon_stats[pokemon_name]['Move-Four']]
    while True:
        move = random.choice(moves).lower()
        if move.strip() == "":
            continue
        else:
            return move


def has_conscious_pokemon(pokemon_inventory: dict) -> bool:
    """
    Checks whether an inventory has any conscious pokemon.
    :param pokemon_inventory: a dictionary containing pokemon names as keys and stats as values
    :precondition: pokemon_inventory must be a a dictionary containing pokemon names as keys and stats as values
    :return: True if has conscious pokemon, else False
    :raise: TypeError if pokemon_inventory not a dictionary
    >>> inventory = {"squirtle": {"Current HP": 50}}
    >>> has_conscious_pokemon(inventory)
    True
    >>> inventory = {"squirtle": {"Current HP": 0}}
    >>> has_conscious_pokemon(inventory)
    False
    """
    if type(pokemon_inventory) != dict:
        raise TypeError("pokemon_inventory must be a dictionary")
    for pokemon in pokemon_inventory:
        if pokemon_inventory[pokemon]["Current HP"] > 0:
            return True
        else:
            continue
    return False


def victory_sequence(pokemon_inventory: dict, enemy_name: str, character: dict, board: dict) -> None:
    """
    Displays combat victory sequence.
    :param pokemon_inventory: a dictionary containing pokemon names as keys and stats as values
    :param enemy_name: the name of a pokemon
    :param character: a dictionary containing 'pokeballs' as a key and an integer as a value
    :param board: a dictionary containing coordinates as keys and descriptions as values
    :precondition: pokemon_inventory must be a dictionary containing pokemon names as keys and stats as values
    :precondition: enemy_name must be a the name of a pokemon
    :precondition: character must be  a dictionary containing 'pokeballs' as a key and an integer as a value
    :precondition: board must be a dictionary containing coordinates as keys and descriptions as values
    :postcondition: displays combat victory sequence
    :raise: TypeError if pokemon_inventory or character or board not a dictionary
    :raise: TypeError if enemy_name not a string
    """
    if type(pokemon_inventory) != dict or type(board) != dict or type(character) != dict:
        raise TypeError("pokemon_inventory, character, and board must be dictionaries")
    if type(enemy_name) != str:
        raise TypeError("enemy_name must be a string")
    stat_gain = gain_stats(character)
    print(f"{enemy_name.title()} has been defeated. You have gained {stat_gain['exp_gain']} EXP and "
          f"{stat_gain['gold_gain']} Gold!")
    if enemy_name != "arceus":
        capture_pokemon(character, board, pokemon_inventory, enemy_name)


def defeat_sequence(character: dict, enemy_name: str) -> None:
    """
    Displays combat defeat sequence.
    :param enemy_name: the name of a pokemon
    :param character: a dictionary containing 'Current HP' as a key and an integer as a value
    :precondition: enemy_name must be a the name of a pokemon
    :precondition: character must be a dictionary containing 'Current HP' as a key and an integer as a value
    :postcondition: displays combat defeat sequence
    :raise: TypeError if pokemon_inventory or character or board not a dictionary
    :raise: TypeError if enemy_name not a string
    """
    if type(character) != dict:
        raise TypeError("character must be a dictionary")
    if type(enemy_name) != str:
        raise TypeError("enemy_name must be a string")
    character["Current HP"] = 0
    print(f"All your Pokémon are unconscious. With no one to defend you, you were eaten by {enemy_name.title()}.\n")
    input("Press any button to quit the game. Loser.")


def your_turn(combat_details: dict, moves: dict, victory: str = False) -> bool:
    """
    Plays the user's turn.
    :param combat_details: a dictionary containing "character", "board", "pokemon_inventory", "enemy_name",
        "enemy_stats", and "current_pokemon" as keys
    :param moves: a dictionary containing move names as keys and stats as values
    :param victory: a default parameter representing whether the character has won the battle
    :precondition: combat_details must be a dictionary containing "character", "board", "pokemon_inventory",
        "enemy_name", "enemy_stats", and "current_pokemon" as keys
    :precondition: moves must be a dictionary containing move names as keys and stats as values
    :precondition: victory must be a boolean value
    :return: True if victory, else False
    :raise: TypeError if combat_details or moves not a dictionary
    :raise: TypeError if victory not a boolean
    :raise: KeyError if all specified keys not in combat_details
    """
    if type(combat_details) != dict or type(moves) != dict:
        raise TypeError("combat_details and moves must be a dictionaries")
    if type(victory) != bool:
        raise TypeError("victory must be a boolean")
    for key in ["character", "board", "pokemon_inventory", "enemy_name", "enemy_stats", "current_pokemon"]:
        if key not in combat_details.keys():
            raise KeyError("combat_details must contain all specified keys")
    display_pokemon(combat_details["pokemon_inventory"])
    move = your_move(combat_details["current_pokemon"], combat_details["pokemon_inventory"])
    damage = randomize_within_10_percent(moves[move]["Damage"])
    combat_details["enemy_stats"][combat_details["enemy_name"]]["Current HP"] -= damage
    if combat_details["enemy_stats"][combat_details["enemy_name"]]["Current HP"] <= 0:
        combat_details["enemy_stats"][combat_details["enemy_name"]]["Current HP"] = 0
        victory = True
    print(f"\t{combat_details['current_pokemon'].title()} used {move.title()}! "
          f"{combat_details['enemy_name'].title()} took "
          f"{damage} damage.")
    display_pokemon(combat_details["enemy_stats"])
    return victory


def enemy_turn(combat_details: dict, moves: dict, defeat: str = False) -> bool:
    """
    Plays the user's turn.
    :param combat_details: a dictionary containing "character", "board", "pokemon_inventory", "enemy_name",
        "enemy_stats", and "current_pokemon" as keys
    :param moves: a dictionary containing move names as keys and stats as values
    :param defeat: a default parameter representing whether the character has lost the battle
    :precondition: combat_details must be a dictionary containing "character", "board", "pokemon_inventory",
        "enemy_name", "enemy_stats", and "current_pokemon" as keys
    :precondition: moves must be a dictionary containing move names as keys and stats as values
    :precondition: defeat must be a boolean value
    :return: True if defeat, else False
    :raise: TypeError if combat_details or moves not a dictionary
    :raise: TypeError if defeat not a boolean
    :raise: KeyError if all specified keys not in combat_details
    """
    if type(combat_details) != dict or type(moves) != dict:
        raise TypeError("combat_details and moves must be a dictionaries")
    if type(defeat) != bool:
        raise TypeError("defeat must be a boolean")
    for key in ["character", "board", "pokemon_inventory", "enemy_name", "enemy_stats", "current_pokemon"]:
        if key not in combat_details.keys():
            raise KeyError("combat_details must contain all specified keys")
    move = enemy_move(combat_details['enemy_stats'], combat_details["enemy_name"]).lower()
    damage = randomize_within_10_percent(moves[move]["Damage"])
    print(f"\t{combat_details['enemy_name'].title()} used {move.title()}! It did {damage} damage.")
    combat_details["pokemon_inventory"][combat_details["current_pokemon"]][
        "Current HP"] -= damage
    if combat_details["pokemon_inventory"][combat_details["current_pokemon"]]["Current HP"] <= 0:
        print(f"\n\t{combat_details['current_pokemon'].title()} was defeated!\n")
        combat_details["pokemon_inventory"][combat_details["current_pokemon"]]["Current HP"] = 0
        defeat = True
    return defeat


def combat_loop(combat_details: dict, defeat: str = False, victory: str = False) -> bool:
    """
    Runs combat loop.
    :param combat_details: a dictionary containing "character", "board", "pokemon_inventory", "enemy_name",
        "enemy_stats", and "current_pokemon" as keys
    :param defeat: a default value representing character defeat
    :param victory: a default value representing character defeat
    :precondition: combat_details must be a dictionary containing "character", "board", "pokemon_inventory",
        "enemy_name", "enemy_stats", and "current_pokemon" as keys
    :precondition: defeat must be a boolean value
    :precondition: victory must be a boolean value
    :return: victory as a boolean operator
    :raise: TypeError if combat_details not a dictionary
    :raise: TypeError if defeat or victory not a boolean
    """
    if type(combat_details) != dict:
        raise TypeError("combat_details must be a dictionary")
    if type(defeat) != bool or type(victory) != bool:
        raise TypeError("defeat and victory must be booleans")
    turn = random.randint(0, 1)
    while not victory and not defeat:
        if turn:
            victory = your_turn(combat_details, read_json("json_data/moves.json"))
            turn -= 1
        else:
            defeat = enemy_turn(combat_details, read_json("json_data/moves.json"))
            if defeat and has_conscious_pokemon(combat_details["pokemon_inventory"]):
                combat_details['current_pokemon'] = choose_a_conscious_pokemon(combat_details["pokemon_inventory"])
                turn = random.randint(0, 1)
                defeat = False
            else:
                turn += 1
    return victory


def get_combat_details(character: dict, board: dict, pokemon_inventory: dict, enemy_name: str = None) -> dict:
    """
    Gets combat details.

    A function that generates combat details according to player location.
    :param character: a dictionary containing 'pokeballs' as a key and an integer as a value
    :param board: a dictionary containing coordinates as keys and descriptions as values
    :param pokemon_inventory: a dictionary containing pokemon names as keys and stats as values
    :param enemy_name: the name of a pokemon
    :precondition: character must be  a dictionary containing 'pokeballs' as a key and an integer as a value
    :precondition: board must be a dictionary containing coordinates as keys and descriptions as values
    :precondition: pokemon_inventory must be a dictionary containing pokemon names as keys and stats as values
    :precondition: enemy_name must be a the name of a pokemon
    :postcondition: generates combat details
    :return: a dictionary containing combat details
    :raise: TypeError if character, board, or pokemon_inventory not a dictionary
    :raise: TypeError if enemy_name is not a string or None
    """
    if type(character) != dict or type(pokemon_inventory) != dict or type(board) != dict:
        raise TypeError("character, pokemon_inventory, and board must be dictionaries")
    if enemy_name is not None and type(enemy_name) != str:
        raise TypeError("enemy_name must be a string or NoneType")
    if enemy_name is None:
        enemy_stats = get_a_pokemon_by_location(board, character)
        enemy_name = list(enemy_stats.keys())[0]
        print(f"\n\tYou encounter a wild {enemy_name.title()}!")
    else:
        enemy_dict = get_pokemon_dict(character, board=board, search_parameter="Legendary")[enemy_name.lower()]
        enemy_stats = {enemy_name: enemy_dict}
    current_pokemon = choose_a_conscious_pokemon(pokemon_inventory)
    combat_details = {"character": character, "board": board, "pokemon_inventory": pokemon_inventory,
                      "enemy_name": enemy_name, "enemy_stats": enemy_stats, "current_pokemon": current_pokemon}
    return combat_details


def main():
    """
    Drives the program.
    """


if __name__ == "__main__":
    main()
