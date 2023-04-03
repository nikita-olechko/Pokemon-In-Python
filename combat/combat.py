import random

from character.leveling import level_up
from utilities.display import swap_pokemon, display_pokemon, display_moves, choose_a_conscious_pokemon
from utilities.utilities import randomize_within_10_percent
from pokemon.finding_pokemon import get_a_pokemon_by_location, get_pokemon_dict
from pokemon.moves import get_moves

from playsound import playsound


def your_move(current_pokemon, pokemon_inventory):
    move = display_moves(current_pokemon, pokemon_inventory)
    return move


def enemy_move(combat_pokemon, pokemon_name):
    while True:
        moves = [combat_pokemon[pokemon_name]['Move-One'], combat_pokemon[pokemon_name]['Move-Two'],
                 combat_pokemon[pokemon_name]['Move-Three'], combat_pokemon[pokemon_name]['Move-Four']]
        for index, move in enumerate(moves):
            if move.strip() == "":
                moves.pop(index)
        else:
            return random.choice(moves).lower()


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
    character["EXP"] += exp_gain*(character["Level"]*0.75)
    character["Gold"] += gold_gain
    print(f"{enemy_name.title()} has been defeated. You have gained {exp_gain} EXP and {gold_gain} Gold!")
    # if level_up(character, pokemon_inventory):
    #     pass
    while True:
        if enemy_name == 'arceus':
            return
        capture = input(f"Capture {enemy_name.title()}?\n\t1: Yes, 2: No\t\n").lower()
        if capture in ['yes', 'no', '1', '2']:
            if capture in ['yes', '1'] and character["Pokeballs"] > 0 and len(pokemon_inventory) < 6:
                pokemon_inventory[enemy_name] = get_a_pokemon_by_location(board, character,
                                                                          enemy_name)[enemy_name]
                pokemon_inventory[enemy_name]['Current HP'] = 0
                character["Pokeballs"] -= 1
                print(f"You have captured {enemy_name.title()}! To revive {enemy_name.title()}, "
                      f"return to the hospital.")
                return
            elif capture in ['yes', '1'] and character["Pokeballs"] == 0:
                print("You do not have any Pokéballs left!")
                return
            elif capture in ['yes', '1'] and len(pokemon_inventory) >= 6:
                swap_pokemon(pokemon_inventory, enemy_name, board, character)
                return
            else:
                return


def defeat_sequence(character, enemy_name):
    character["Current HP"] = 0
    print(f"All your Pokémon are unconscious. With no one to defend you, you were eaten by {enemy_name.title()}.\n")
    input("Press any button to quit the game. Loser.")


def initialize_arceus_music(enemy):
    if enemy is not None:
        playsound('music/Arceus-Battle.wav', block=False)


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
                    current_pokemon = choose_a_conscious_pokemon(pokemon_inventory)
                    turn = random.randint(0, 1)
                else:
                    defeat = True
    display_pokemon(pokemon_inventory)
    if defeat:
        defeat_sequence(character, enemy_name)
        return False
    if victory:
        victory_sequence(pokemon_inventory, enemy_name, character, board)
        level_up(character, pokemon_inventory)
        return True


def get_combat_details(character, board, pokemon_inventory, enemy_name=None):
    initialize_arceus_music(enemy_name)
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
    # combat_loop(character, board, pokemon_inventory, enemy_name, enemy_stats, current_pokemon,
    #             defeat=False, victory=False)
    return combat_details
