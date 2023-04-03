from character.tutorial import yes_or_no_input
from pokemon.finding_pokemon import get_a_pokemon_by_location
from utilities.display import choose_any_pokemon
from utilities.utilities import print_rolling_dialogue


def capture_no_swap(pokemon_inventory, enemy_name, board, character):
    pokemon_inventory[enemy_name] = get_a_pokemon_by_location(board, character, enemy_name)[enemy_name]
    pokemon_inventory[enemy_name]['Current HP'] = 0
    character["Pokeballs"] -= 1
    print(f"You have captured {enemy_name.title()}! To revive {enemy_name.title()}, "
          f"return to the hospital.")


def capture_pokemon(character, board, pokemon_inventory, enemy_name, capture=None):
    while capture not in ['yes', 'no', '1', '2']:
        capture = input(f"Capture {enemy_name.title()}?\n\t1: Yes, 2: No\t\n").lower()
    if capture in ['yes', '1'] and character["Pokeballs"] > 0 and len(pokemon_inventory) < 6:
        capture_no_swap(pokemon_inventory, enemy_name, board, character)
    elif capture in ['yes', '1'] and character["Pokeballs"] == 0:
        print("You do not have any Pokéballs left!")
    elif capture in ['yes', '1'] and len(pokemon_inventory) >= 6:
        swap_pokemon(pokemon_inventory, enemy_name, board, character)
    else:
        return


def swap_pokemon(pokemon_inventory, enemy_name, board, character):
    print_rolling_dialogue(f"\nYou can't carry anymore Pokemon! Would you like to swap out a Pokemon"
                           f" for {enemy_name}? ", delay=0.01, new_line=False)
    if not yes_or_no_input():
        return
    chosen_pokemon = choose_any_pokemon(pokemon_inventory)
    print_rolling_dialogue(f"\nAre you sure you want to swap out {chosen_pokemon.title()} for"
                           f" {enemy_name.title()}? ", delay=0.01,
                           new_line=False)
    if yes_or_no_input():
        del pokemon_inventory[chosen_pokemon]
        pokemon_inventory[enemy_name] = get_a_pokemon_by_location(board, character,
                                                                  enemy_name)[enemy_name]
        pokemon_inventory[enemy_name]['Current HP'] = 0
