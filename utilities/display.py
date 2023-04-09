def choose_any_pokemon(pokemon_inventory: dict) -> str:
    """
    Prompts the user to choose a pokemon from their inventory.
    :param pokemon_inventory: a dictionary containing pokemon names as keys
    :precondition: pokemon_inventory must be a dictionary containing pokemon names as keys
    :postcondition: prompts the user to choose a pokemon
    :return: chosen pokemon name as a string
    :raise: TypeError if pokemon_inventory not a dictionary
    """
    if type(pokemon_inventory) != dict:
        raise TypeError("pokemon_inventory must be a dictionary")
    poke_list = []
    poke_nums = []
    for index, pokemon in enumerate(pokemon_inventory):
        poke_list.append(pokemon)
        poke_list.append(str(index + 1))
        poke_nums.append(str(index + 1))
    while True:
        display_pokemon(pokemon_inventory)
        chosen_pokemon = input(f"\tChoose a Pokémon from your inventory: \n\n").lower()
        if chosen_pokemon.lower() in poke_nums:
            chosen_pokemon = list(pokemon_inventory.keys())[int(chosen_pokemon) - 1]
        if chosen_pokemon.lower() not in poke_list:
            print(f"That's not of your Pokémon")
            continue
        else:
            return chosen_pokemon


def display_pokemon(pokemon_inventory: dict) -> None:
    """
    Displays pokemon in pokemon_inventory.
    :param pokemon_inventory: a dictionary containing pokemon names as keys
    :precondition: pokemon_inventory must be a dictionary containing pokemon names as keys
    :postcondition: displays pokemon in pokemon_inventory
    :raise: TypeError if pokemon_inventory not a dictionary
    """
    if type(pokemon_inventory) != dict:
        raise TypeError("pokemon_inventory must be a dictionary")
    list_of_pokemon = "| "
    for index, pokemon in enumerate(pokemon_inventory):
        list_of_pokemon += f"{index + 1}: {pokemon.title()}, "
        list_of_pokemon += f"Current HP: {pokemon_inventory[pokemon]['Current HP']} | "
    print(f"\n\t{list_of_pokemon}\n")


def display_moves(combat_pokemon: str, pokemon_inventory: dict, line: str = "") -> str:
    """
    Displays available moves of a pokemon.
    :param pokemon_inventory: a dictionary containing pokemon names as keys
    :param combat_pokemon: the name of a pokemon
    :param line: an optional parameter indicating whether a break between moves should be printed
    :precondition: pokemon_inventory must be a dictionary containing pokemon names as keys
    :precondition: combat_pokemon must be a string
    :precondition: combat_pokemon must be a key in pokemon_inventory
    :precondition: line must be a string
    :postcondition: displays available moves of combat_pokemon
    :raise: TypeError if pokemon_inventory not a dictionary
    :raise: TypeError if combat_pokemon not a string
    """
    if type(pokemon_inventory) != dict:
        raise TypeError("pokemon_inventory must be a dictionary")
    if type(combat_pokemon) != str:
        raise TypeError("combat_pokemon must be a string")
    real_moves = get_real_moves(combat_pokemon, pokemon_inventory)
    if real_moves["pokemon"]['Move-Four'] != '':
        line = '|'
    while True:
        print(f"\n\tChoose a move:")
        choice = input(f"\n\t{real_moves['numbered_list'][0]} {real_moves['pokemon']['Move-One']} | "
                       f"{real_moves['numbered_list'][1]} {real_moves['pokemon']['Move-Two']}\n"
                       f"\t{real_moves['numbered_list'][2]} {real_moves['pokemon']['Move-Three']} {line} "
                       f"{real_moves['numbered_list'][3]} "
                       f"{real_moves['pokemon']['Move-Four']}\n").lower().strip()
        if (choice not in real_moves['options'] and choice not in real_moves['move_index_list']) or choice == '':
            print("\tThat's not of your moves")
            continue
        elif choice in real_moves['options']:
            return choice
        else:
            return real_moves['options'][int(choice) - 1]


def get_real_moves(combat_pokemon: str, pokemon_inventory: dict) -> dict:
    """
    Gets a dictionary of real pokemon moves for use in display_moves().
    :param pokemon_inventory: a dictionary containing pokemon names as keys
    :param combat_pokemon: the name of a pokemon
    :precondition: pokemon_inventory must be a dictionary containing pokemon names as keys
    :precondition: combat_pokemon must be a string
    :precondition: combat_pokemon must be a key in pokemon_inventory
    :postcondition: displays available moves of combat_pokemon
    :return: a dictionary containing move data for use in display_moves()
    :raise: TypeError if pokemon_inventory not a dictionary
    :raise: TypeError if combat_pokemon not a string
    """
    if type(pokemon_inventory) != dict:
        raise TypeError("pokemon_inventory must be a dictionary")
    if type(combat_pokemon) != str:
        raise TypeError("combat_pokemon must be a string")
    pokemon = pokemon_inventory[combat_pokemon]
    options = [pokemon['Move-One'].lower(), pokemon['Move-Two'].lower(), pokemon['Move-Three'].lower(),
               pokemon['Move-Four'].lower()]
    numbered_list = ["1:", "2:", "3:", "4:"]
    move_index_list = ["1", "2", "3", "4"]
    for index, move in enumerate(options):
        if move.strip() == "":
            numbered_list[index] = ""
            move_index_list[index] = ""
    return {"pokemon": pokemon, "options": options, "numbered_list": numbered_list, "move_index_list": move_index_list}


def choose_a_conscious_pokemon(pokemon_inventory: dict) -> str:
    """
    Prompts the user to choose a conscious pokemon from the inventory.
    :param pokemon_inventory: a dictionary containing pokemon names as keys and stats as values
    :precondition: pokemon_dictionary must be a dictionary containing pokemon names as keys and stats as values
    :postcondition: gets a conscious pokemon from the user
    :return: the name of a conscious pokemon in pokemon_inventory as a string
    :raise: TypeError if pokemon_inventory is not a dictionary
    """
    if type(pokemon_inventory) != dict:
        raise TypeError("pokemon_inventory must be a dictionary")
    poke_nums = [str(index + 1) for index, pokemon in enumerate(pokemon_inventory)]
    while True:
        display_pokemon(pokemon_inventory)
        chosen_pokemon = input("\tChoose a Pokémon from your inventory: \n\n").lower()
        if chosen_pokemon.lower() in poke_nums:
            chosen_pokemon = list(pokemon_inventory.keys())[int(chosen_pokemon) - 1]
        else:
            print(f"That's not of your Pokémon")
            continue
        if pokemon_inventory[chosen_pokemon]["Current HP"] <= 0:
            print(f"{chosen_pokemon.title()} is unconscious")
            continue
        else:
            return chosen_pokemon


def main():
    """
    Drives the program.
    """


if __name__ == "__main__":
    main()
