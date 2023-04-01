import random

from misc.misc import randomize_within_10_percent
from pokemon.finding_pokemon import get_a_pokemon, get_pokemon_list
from pokemon.moves import get_moves


def display_pokemon(pokemon_inventory):
    list_of_pokemon = "| "
    for pokemon in pokemon_inventory:
        list_of_pokemon += f"{pokemon.title()}, "
        list_of_pokemon += f"Current HP: {pokemon_inventory[pokemon]['Current HP']} |"
    return list_of_pokemon


def choose_a_pokemon(pokemon_inventory):

    """
    Returns a chosen pokemon index in your inventory (e.g. '1', '2', '4')
    """
    poke_list = []
    for pokemon in pokemon_inventory:
        poke_list.append(pokemon)
    while True:
        chosen_pokemon = input(f"\tChoose a Pokémon from your inventory: \n\n"
                               f"\t{display_pokemon(pokemon_inventory)}\n").lower()
        print("")
        if chosen_pokemon.lower() not in poke_list:
            print("That's not of your Pokémon")
            continue
        elif pokemon_inventory[chosen_pokemon]["Current HP"] <= 0:
            print(f"{chosen_pokemon} is unconscious")
            continue
        # elif chosen_pokemon.isdigit():

        #     return poke_dict[chosen_pokemon]
        else:
            return chosen_pokemon


def display_moves(combat_pokemon, pokemon_inventory):
    pokemon = pokemon_inventory[combat_pokemon]
    options = [pokemon['Move-One'].lower(), pokemon['Move-Two'].lower(), pokemon['Move-Three'].lower(),
               pokemon['Move-Four'].lower()]
    line = ''
    if pokemon['Move-Four'] != '':
        line = '|'
    while True:
        print("\n\tChoose a move:")
        choice = input(f"\n\t{pokemon['Move-One']} | {pokemon['Move-Two']}\n"
                       f"\t{pokemon['Move-Three']} {line} {pokemon['Move-Four']}\n").lower()
        if choice not in options and choice != "":
            print("\tThat's not of your moves")
            continue
        # elif chosen_pokemon.int() <= len(pokemon):
        #     return poke_dict[chosen_pokemon]
        else:
            return choice.lower()


def your_move(current_pokemon, pokemon_inventory):
    move = display_moves(current_pokemon, pokemon_inventory)
    return move


# ask Chris if this sort of recursion is bad practice - could theoretically overflow?
def enemy_move(combat_pokemon, pokemon_name):
    while True:
        move = random.choices(
            [combat_pokemon[pokemon_name]['Move-One'], combat_pokemon[pokemon_name]['Move-Two'],
             combat_pokemon[pokemon_name]['Move-Three'], combat_pokemon[pokemon_name]['Move-Four']])
        if move == '':
            continue
        else:
            return move[0].lower()


# ask Chris how to pass this parameter
# def combat(character, board, pokemon_collection, enemy=get_random_pokemon(*)):
def has_conscious_pokemon(pokemon_inventory):
    for pokemon in pokemon_inventory:
        if pokemon_inventory[pokemon]["Current HP"] > 0:
            return True
        else:
            continue
    return False


def victory_sequence(pokemon_inventory, enemy_name, character, board):

    character["EXP"] += randomize_within_10_percent(50)
    print("You win - continue")
    if character["EXP"] >= 100:
        character["Level"] += 1
        character["EXP"] -= 100
        print(f"You have leveled up!\nCurrent Level: {character['Level']}")
    while True:
        capture = input(f"Capture {enemy_name.title()}?\n\t1: Yes, 2: No\t\n").lower()
        if capture in ['yes', 'no', '1', '2']:
            if capture in ['yes', '1'] and character["Pokeballs"] > 0:
                pokemon_inventory[enemy_name] = get_a_pokemon(board, character, enemy_name)
                pokemon_inventory[enemy_name]['Current HP'] = 0
                print(f"You have captured {enemy_name.title()}! To revive {enemy_name.title()}, return to the shop.")
            elif capture in ['yes', '1'] and character["Pokeballs"] == 0:
                print("You do not have any Pokéballs left!")
                break
            else:
                break


def defeat_sequence():
    print("You lose - try again next time")


def combat(character, board, pokemon_inventory, enemy_name=None):
    #create separate function to get game stats
    if enemy_name is None:
        enemy_stats = get_a_pokemon(board, character)
        enemy_name = list(enemy_stats.keys())[0]
        print(f"\tYou encounter a wild {enemy_name.title()}!\n")
    else:
        enemy_stats = get_pokemon_list(board, character)[enemy_name]
    moves = get_moves()
    current_pokemon = choose_a_pokemon(pokemon_inventory)
    defeat = False
    victory = False
    # turn = random.randint(0, 1)
    turn = 1
    while not victory and not defeat:
        if turn:
            print(f"\n\t{display_pokemon(pokemon_inventory)}")
            move = your_move(current_pokemon, pokemon_inventory)
            damage = randomize_within_10_percent(moves[move]["Damage"])
            enemy_stats[enemy_name]["Current HP"] -= damage
            if enemy_stats[enemy_name]["Current HP"] <= 0:
                enemy_stats[enemy_name]["Current HP"] = 0
                victory = True
            print(f"\t{current_pokemon.title()} used {move.title()}! {enemy_name.title()} took "
                  f"{-damage} damage.")
            print(f"\n\t{display_pokemon(enemy_stats)}")
            turn -= 1
        else:
            move = enemy_move(enemy_stats, enemy_name)
            damage = randomize_within_10_percent(moves[move]["Damage"])
            print(f"\t{enemy_name.title()} used {move.title()}! It did {-damage} damage.")
            pokemon_inventory[current_pokemon]["Current HP"] -= damage
            turn += 1
            if pokemon_inventory[current_pokemon]["Current HP"] <= 0:
                if has_conscious_pokemon(pokemon_inventory):
                    current_pokemon = choose_a_pokemon(pokemon_inventory)
                    turn = random.randint(0, 1)
                else:
                    defeat = True
    if defeat:
        defeat_sequence()
        return False
    if victory:
        victory_sequence(pokemon_inventory, enemy_name, character, board)
        return True
