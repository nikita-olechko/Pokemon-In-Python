def choose_any_pokemon(pokemon_inventory):
    """
    Prompts the user to choose a pokemon from their inventory.
    :param pokemon_inventory: a dictionary containing pokemon names as keys
    :precondition: pokemon_inventory must be a dictionary containing pokemon names as keys
    :postcondition: prompts the user to choose a pokemon
    :return: chosen pokemon name as a string
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
        else:
            return chosen_pokemon


def display_pokemon(pokemon_inventory):
    """
    Displays pokemon in pokemon_inventory.
    :param pokemon_inventory: a dictionary containing pokemon names as keys
    :precondition: pokemon_inventory must be a dictionary containing pokemon names as keys
    :postcondition: displays pokemon in pokemon_inventory
    """
    list_of_pokemon = "| "
    for index, pokemon in enumerate(pokemon_inventory):
        list_of_pokemon += f"{index + 1}: {pokemon.title()}, "
        list_of_pokemon += f"Current HP: {pokemon_inventory[pokemon]['Current HP']} | "
    print(f"\n\t{list_of_pokemon}\n")


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


def choose_a_conscious_pokemon(pokemon_inventory):
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
        else:
            return chosen_pokemon
