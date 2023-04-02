from utilities.utilities import display_pokemon


def choose_any_pokemon(pokemon_inventory):
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
        else:
            return chosen_pokemon
