import random

from character.leveling import gain_stats
from combat.capturing_pokemon import capture_pokemon
from utilities.display import display_pokemon, display_moves, choose_a_conscious_pokemon
from utilities.utilities import randomize_within_10_percent
from pokemon.finding_pokemon import get_a_pokemon_by_location, get_pokemon_dict
from pokemon.moves import get_moves


def your_move(current_pokemon, pokemon_inventory):
    """
    Gets a move associated with a pokemon from the user.
    @param current_pokemon: a pokemon in pokemon_inventory
    @param pokemon_inventory: a dictionary containing pokemon names as keys and stats as values
    @precondition: pokemon must be a string
    @precondition: pokemon must be a key in pokemon_inventory
    @precondition: pokemon inventory must be a a dictionary containing pokemon names as keys and stats as values
    @postcondition: gets a valid move from the user
    @return: a valid move associated with current_pokemon as a string
    """
    move = display_moves(current_pokemon, pokemon_inventory)
    return move


def enemy_move(combat_pokemon_stats, pokemon_name):
    """
    Picks a random enemy move.
    @param combat_pokemon_stats: stats associated with an enemy pokemon
    @param pokemon_name: the name of a pokemon
    @precondition: combat_pokemon_stats must be a dictionary containing at least one move ('Move-One')
    @precondition: pokemon_name must be a string
    @postcondition: gets a valid enemy move
    @return: an enemy move as a string
    """
    moves = [combat_pokemon_stats[pokemon_name]['Move-One'], combat_pokemon_stats[pokemon_name]['Move-Two'],
             combat_pokemon_stats[pokemon_name]['Move-Three'], combat_pokemon_stats[pokemon_name]['Move-Four']]
    while True:
        move = random.choice(moves).lower()
        if move.strip() == "":
            continue
        else:
            return random.choice(moves).lower()


def has_conscious_pokemon(pokemon_inventory):
    """
    Checks whether an inventory has any conscious pokemon.
    @param pokemon_inventory: a dictionary containing pokemon names as keys and stats as values
    @precondition: pokemon inventory must be a a dictionary containing pokemon names as keys and stats as values
    @return: True if has conscious pokemon, else False
    """
    for pokemon in pokemon_inventory:
        if pokemon_inventory[pokemon]["Current HP"] > 0:
            return True
        else:
            continue
    return False


def victory_sequence(pokemon_inventory, enemy_name, character, board):
    """

    @param pokemon_inventory:
    @param enemy_name:
    @param character:
    @param board:
    @return:
    """
    stat_gain = gain_stats(character)
    print(f"{enemy_name.title()} has been defeated. You have gained {stat_gain['exp_gain']} EXP and "
          f"{stat_gain['gold_gain']} Gold!")
    if enemy_name != "arceus":
        capture_pokemon(character, board, pokemon_inventory, enemy_name)


def defeat_sequence(character, enemy_name):
    character["Current HP"] = 0
    print(f"All your Pokémon are unconscious. With no one to defend you, you were eaten by {enemy_name.title()}.\n")
    input("Press any button to quit the game. Loser.")


def your_turn(combat_details, moves, victory=False):
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
    if victory:
        return True
    return False


def enemy_turn(combat_details, moves, defeat=False):
    move = enemy_move(combat_details['enemy_stats'], combat_details["enemy_name"]).lower()
    damage = randomize_within_10_percent(moves[move]["Damage"])
    print(f"\t{combat_details['enemy_name'].title()} used {move.title()}! It did {damage} damage.")
    combat_details["pokemon_inventory"][combat_details["current_pokemon"]][
        "Current HP"] -= damage
    if combat_details["pokemon_inventory"][combat_details["current_pokemon"]]["Current HP"] <= 0:
        print(f"\n\t{combat_details['current_pokemon'].title()} was defeated!\n")
        combat_details["pokemon_inventory"][combat_details["current_pokemon"]]["Current HP"] = 0
        defeat = True
    if defeat:
        return True
    return False


def combat_loop(combat_details, defeat=False, victory=False):
    turn = random.randint(0, 1)
    while not victory and not defeat:
        if turn:
            victory = your_turn(combat_details, get_moves())
            turn -= 1
        else:
            defeat = enemy_turn(combat_details, get_moves())
            if defeat and has_conscious_pokemon(combat_details["pokemon_inventory"]):
                combat_details['current_pokemon'] = choose_a_conscious_pokemon(combat_details["pokemon_inventory"])
                turn = random.randint(0, 1)
                defeat = False
            else:
                turn += 1
    display_pokemon(combat_details["pokemon_inventory"])
    return victory


def get_combat_details(character, board, pokemon_inventory, enemy_name=None):
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
