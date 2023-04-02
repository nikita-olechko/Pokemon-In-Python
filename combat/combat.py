import random

from character.leveling import level_up
from utilities.utilities import randomize_within_10_percent
from pokemon.finding_pokemon import get_a_random_pokemon_by_location, get_pokemon_dict
from pokemon.moves import get_moves

from playsound import playsound


def display_pokemon(pokemon_inventory):
    list_of_pokemon = "| "
    for index, pokemon in enumerate(pokemon_inventory):
        list_of_pokemon += f"{index + 1}: {pokemon.title()}, "
        list_of_pokemon += f"Current HP: {pokemon_inventory[pokemon]['Current HP']} | "
    print(f"\n\t{list_of_pokemon}\n")


def choose_a_pokemon(pokemon_inventory):
    """
    Returns a chosen pokemon index in your inventory (e.g. '1', '2', '4')
    """
    poke_list = []
    poke_nums = []
    for index, pokemon in enumerate(pokemon_inventory):
        poke_list.append(pokemon)
        poke_list.append(str(index + 1))
        poke_nums.append(str(index + 1))
    while True:
        display_pokemon(pokemon_inventory)
        chosen_pokemon = input("\tChoose a Pokémon from your inventory: \n\n").lower()
        print("")
        if chosen_pokemon.lower() in poke_nums:
            chosen_pokemon = list(pokemon_inventory.keys())[int(chosen_pokemon) - 1]
        if chosen_pokemon.lower() not in poke_list:
            print("That's not of your Pokémon")
            continue
        elif pokemon_inventory[chosen_pokemon]["Current HP"] <= 0:
            print(f"{chosen_pokemon.title()} is unconscious")
            continue
        # elif chosen_pokemon.isdigit():

        #     return poke_dict[chosen_pokemon]
        else:
            return chosen_pokemon


def display_moves(combat_pokemon, pokemon_inventory):
    pokemon = pokemon_inventory[combat_pokemon]
    options = [pokemon['Move-One'].lower(), pokemon['Move-Two'].lower(), pokemon['Move-Three'].lower(),
               pokemon['Move-Four'].lower()]
    numbered_list = ["1:", "2:", "3:", "4:"]
    move_index_list = ["1", "2", "3", "4"]
    for index, move in enumerate(options):
        if move.strip() == "":
            numbered_list[index] = ""
            move_index_list[index] = ""
    line = ''
    if pokemon['Move-Four'] != '':
        line = '|'
    while True:
        print("\n\tChoose a move:")
        choice = input(f"\n\t{numbered_list[0]} {pokemon['Move-One']} | {numbered_list[1]} {pokemon['Move-Two']}\n"
                       f"\t{numbered_list[2]} {pokemon['Move-Three']} {line} {numbered_list[3]} "
                       f"{pokemon['Move-Four']}\n").lower().strip()
        if (choice not in options and choice not in move_index_list) or choice == '':
            print("\tThat's not of your moves")
            continue
        elif choice in options:
            return choice
        else:
            return options[int(choice) - 1]


def your_move(current_pokemon, pokemon_inventory):
    move = display_moves(current_pokemon, pokemon_inventory)
    return move


# ask Chris if this sort of recursion is bad practice - could theoretically overflow?
def enemy_move(combat_pokemon, pokemon_name):
    while True:
        moves = [combat_pokemon[pokemon_name]['Move-One'], combat_pokemon[pokemon_name]['Move-Two'],
                 combat_pokemon[pokemon_name]['Move-Three'], combat_pokemon[pokemon_name]['Move-Four']]
        for index, move in enumerate(moves):
            if move.strip() == "":
                moves.pop(index)
        else:
            return random.choice(moves).lower()


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
    exp_gain = randomize_within_10_percent(50)
    gold_gain = randomize_within_10_percent(50)
    character["EXP"] += exp_gain
    character["Gold"] += gold_gain
    print(f"{enemy_name.title()} has been defeated. You have gained {exp_gain} EXP and {gold_gain} Gold!")
    # if level_up(character, pokemon_inventory):
    #     pass
    while True:
        if enemy_name == 'arceus':
            return
        capture = input(f"Capture {enemy_name.title()}?\n\t1: Yes, 2: No\t\n").lower()
        if capture in ['yes', 'no', '1', '2']:
            if capture in ['yes', '1'] and character["Pokeballs"] > 0:
                pokemon_inventory[enemy_name] = get_a_random_pokemon_by_location(board, character,
                                                                                 enemy_name)[enemy_name]
                pokemon_inventory[enemy_name]['Current HP'] = 0
                character["Pokeballs"] -= 1
                print(f"You have captured {enemy_name.title()}! To revive {enemy_name.title()}, "
                      f"return to the hospital.")
                level_up(character, pokemon_inventory)
                return
            elif capture in ['yes', '1'] and character["Pokeballs"] == 0:
                print("You do not have any Pokéballs left!")
                level_up(character, pokemon_inventory)
                return
            else:
                level_up(character, pokemon_inventory)
                return


def defeat_sequence(character, enemy_name):
    character["Current HP"] = 0
    print(f"All your Pokémon are unconscious. With no one to defend you, you were eaten by {enemy_name.title()}.\n")
    input("Press any button to quit the game. Loser.")


def initialize_arceus_music(enemy):
    if enemy is not None:
        playsound('combat/Arceus-Battle.wav', block=False)


def combat_loop(character, board, pokemon_inventory, enemy_name, enemy_stats, current_pokemon, defeat=False,
                victory=False):
    moves = get_moves()
    turn = random.randint(0, 1)
    while not victory and not defeat:
        if turn:
            display_pokemon(pokemon_inventory)
            move = your_move(current_pokemon, pokemon_inventory)
            damage = randomize_within_10_percent(moves[move]["Damage"])
            enemy_stats[enemy_name]["Current HP"] -= damage
            if enemy_stats[enemy_name]["Current HP"] <= 0:
                enemy_stats[enemy_name]["Current HP"] = 0
                victory = True
            print(f"\t{current_pokemon.title()} used {move.title()}! {enemy_name.title()} took "
                  f"{damage} damage.")
            display_pokemon(enemy_stats)
            turn -= 1
        else:
            move = enemy_move(enemy_stats, enemy_name).lower()
            damage = randomize_within_10_percent(moves[move]["Damage"])
            print(f"\t{enemy_name.title()} used {move.title()}! It did {damage} damage.")
            pokemon_inventory[current_pokemon]["Current HP"] -= damage
            turn += 1
            if pokemon_inventory[current_pokemon]["Current HP"] <= 0:
                print(f"\n\t{current_pokemon.title()} was defeated!\n")
                pokemon_inventory[current_pokemon]["Current HP"] = 0
                if has_conscious_pokemon(pokemon_inventory):
                    current_pokemon = choose_a_pokemon(pokemon_inventory)
                    turn = random.randint(0, 1)
                else:
                    defeat = True
    if defeat:
        defeat_sequence(character, enemy_name)
        return False
    if victory:
        victory_sequence(pokemon_inventory, enemy_name, character, board)
        return True


def initialize_combat(character, board, pokemon_inventory, enemy_name=None):
    initialize_arceus_music(enemy_name)
    if enemy_name is None:
        enemy_stats = get_a_random_pokemon_by_location(board, character)
        enemy_name = list(enemy_stats.keys())[0]
        print(f"\n\tYou encounter a wild {enemy_name.title()}!")
    else:
        enemy_dict = get_pokemon_dict(character, board=board, search_parameter="Legendary")[enemy_name.lower()]
        enemy_stats = {enemy_name: enemy_dict}
    current_pokemon = choose_a_pokemon(pokemon_inventory)
    combat_loop(character, board, pokemon_inventory, enemy_name, enemy_stats, current_pokemon,
                defeat=False, victory=False)
