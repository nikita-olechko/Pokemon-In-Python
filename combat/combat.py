import random

from misc.misc import random_multiplier
from pokemon.finding_pokemon import get_random_pokemon, get_pokemon_list
from pokemon.moves import get_moves


def display_pokemon(pokemon_inventory):
    list_of_pokemon = "| "
    for pokemon in pokemon_inventory:
        list_of_pokemon += f"{pokemon.capitalize()}, "
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
        chosen_pokemon = input(f"Choose a Pokémon from your inventory: \n"
                               f"{display_pokemon(pokemon_inventory)}\n\n").lower()
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
        if choice not in options:
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
def enemy_move(combat_pokemon):
    while True:
        move = random.choices(
            [combat_pokemon['Move-One'], combat_pokemon['Move-Two'], combat_pokemon['Move-Three'],
             combat_pokemon['Move-Four']])
        if move == "":
            continue
        else:
            print(f"\tEnemy used {move}!")
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


def victory_sequence(character):
    character["EXP"] += random_multiplier(50)
    print("You win - continue")
    if character["EXP"] >= 100:
        character["Level"] += 1
        character["EXP"] -= 100
        print(f"You have leveled up!\nCurrent Level: {character['Level']}")


def defeat_sequence():
    print("You lose - try again next time")


def combat(character, board, pokemon_inventory):
    #create separate function to get game stats
    enemy_name = get_random_pokemon(board, character)
    # enemy_stats = get_pokemon_list(board, character)[enemy_name]
    enemy_stats = get_pokemon_list(board, character)[enemy_name]
    moves = get_moves()
    current_pokemon = choose_a_pokemon(pokemon_inventory)
    defeat = False
    victory = False
    # turn = random.randint(0, 1)
    turn = 1
    while not victory or not defeat:
        if turn:
            print(f"\n\t{display_pokemon(pokemon_inventory)}")
            move = your_move(current_pokemon, pokemon_inventory)
            damage = random_multiplier(moves[move]["Damage"])
            enemy_stats["Current HP"] -= damage
            print(f"{current_pokemon.title()} used {move.title()}! {enemy_name.title()} took "
                  f"{min(damage, enemy_stats['Current HP'])} damage.")
            if enemy_stats["Current HP"] <= 0:
                victory = True
            turn -= 1
        else:
            move = enemy_move(enemy_stats)
            damage = random_multiplier(moves[move]["Damage"])
            print(f"{enemy_name.title()} used {move.title()}! It did {damage} damage.")
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
        victory_sequence(character)
        return True
