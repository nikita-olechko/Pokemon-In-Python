from pokemon.finding_pokemon import get_a_pokemon_by_location
from utilities.display import choose_any_pokemon
from utilities.utilities import print_rolling_dialogue, yes_or_no_input


def capture_no_swap(pokemon_inventory, enemy_name, board, character):
    """
    Captures a pokemon.

    A function that adds a captured pokemon to a character's pokemon inventory.
    :param pokemon_inventory: a dictionary containing pokemon names as keys and stats as values
    :param enemy_name: the name of a pokemon
    :param board: a dictionary containing coordinates as keys and descriptions as values
    :param character: a dictionary containing 'pokeballs' as a key and an integer as a value
    :precondition: pokemon_inventory must be a dictionary containing pokemon names as keys and stats as values
    :precondition: enemy_name must be a the name of a pokemon
    :precondition: board must be a a dictionary containing coordinates as keys and descriptions as values
    :precondition: character must be a dictionary containing 'pokeballs' as a key and an integer as a value
    :postcondition: adds a key-value pair to pokemon_inventory as the captured pokemon and associated stats
    :raises: TypeError if board or character or pokemon_inventory not dictionaries
    :raises: TypeError if enemy_name not a string
    """
    if type(board) != dict or type(character) != dict or type(pokemon_inventory) != dict:
        raise TypeError("board, character, and pokemon_inventory must be dictionaries")
    if type(enemy_name) != str:
        raise TypeError("enemy_name must be a string")
    pokemon_inventory[enemy_name] = get_a_pokemon_by_location(board, character, enemy_name)[enemy_name]
    pokemon_inventory[enemy_name]['Current HP'] = 0
    character["Pokeballs"] -= 1
    print(f"You have captured {enemy_name.title()}! To revive {enemy_name.title()}, "
          f"return to the hospital.")


def capture_pokemon(character, board, pokemon_inventory, enemy_name, capture=None):
    """
    Captures a pokemon if enough pokeballs and inventory space.
    :param pokemon_inventory: a dictionary containing pokemon names as keys and stats as values
    :param enemy_name: the name of a pokemon
    :param board: a dictionary containing coordinates as keys and descriptions as values
    :param character: a dictionary containing 'pokeballs' as a key and an integer as a value
    :param capture: an optional paramater indicating whether or not to capture a pokemon
    :precondition: pokemon_inventory must be a dictionary containing pokemon names as keys and stats as values
    :precondition: enemy_name must be a the name of a pokemon
    :precondition: board must be a dictionary containing coordinates as keys and descriptions as values
    :precondition: character must be a dictionary containing 'pokeballs' as a key and an integer as a value
    :precondition: capture must be a string, else None
    :postcondition: adds a key-value pair to pokemon_inventory as the captured pokemon and associated stats
    :raises: TypeError if board or character or pokemon_inventory not dictionaries
    :raises: TypeError if enemy_name not a string
    """
    if type(board) != dict or type(character) != dict or type(pokemon_inventory) != dict:
        raise TypeError("board, character, and pokemon_inventory must be dictionaries")
    if type(enemy_name) != str:
        raise TypeError("enemy_name must be a string")
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
    """
    Swaps a pokemon with another pokemon in inventory.
    :param pokemon_inventory: a dictionary containing pokemon names as keys and stats as values
    :param enemy_name: the name of a pokemon
    :param board: a dictionary containing coordinates as keys and descriptions as values
    :param character: a dictionary containing 'pokeballs' as a key and an integer as a value
    :precondition: pokemon_inventory must be a dictionary containing pokemon names as keys and stats as values
    :precondition: enemy_name must be a the name of a pokemon
    :precondition: board must be a a dictionary containing coordinates as keys and descriptions as values
    :precondition: character must be a dictionary containing 'pokeballs' as a key and an integer as a value
    :postcondition: swaps a specified pokemon in your inventory with the enemy pokemon with 0 HP
    :raises: TypeError if board or character or pokemon_inventory not dictionaries
    :raises: TypeError if enemy_name not a string
    """
    if type(board) != dict or type(character) != dict or type(pokemon_inventory) != dict:
        raise TypeError("board, character, and pokemon_inventory must be dictionaries")
    if type(enemy_name) != str:
        raise TypeError("enemy_name must be a string")
    while True:
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
            return


def main():
    """
    Drives the program.
    """


if __name__ == "__main__":
    main()
