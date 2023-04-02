from utilities.utilities import print_rolling_dialogue
from pokemon.finding_pokemon import get_pokemon_dict


def print_evolution(pokemon, new_pokemon):
    print_rolling_dialogue(". . . ", delay=0.5)
    print_rolling_dialogue("What's this?? ", new_line=False)
    print_rolling_dialogue(". . . ", delay=0.25)
    print_rolling_dialogue(pokemon, new_line=False)
    print_rolling_dialogue(" is evolving!")
    print_rolling_dialogue(pokemon, new_line=False)
    print_rolling_dialogue(" has evolved into ", new_line=False)
    print_rolling_dialogue(new_pokemon, new_line=False)
    print_rolling_dialogue("!")
    print_rolling_dialogue(new_pokemon, new_line=False)
    print_rolling_dialogue(" has more HP and new moves!")


def evolve(pokemon_inventory, current_evolution=None):
    inventory_copy = pokemon_inventory.copy()
    for pokemon, value in inventory_copy.items():
        for key, stat_value in value.items():
            stat_value = str(stat_value).lower()
            if stat_value == pokemon.lower():
                current_evolution = key
        if current_evolution == 'Evolution-One' and pokemon_inventory[pokemon]['Evolution-Two'].strip() != "":
            new_pokemon = pokemon_inventory[pokemon]['Evolution-Two'].lower()
            pokemon_inventory[new_pokemon] = get_pokemon_dict(search_parameter=value["Location"])[new_pokemon]
            pokemon_inventory.pop(pokemon)
            print_evolution(pokemon.title(), new_pokemon.title())
        if current_evolution == 'Evolution-Two' and pokemon_inventory[pokemon]['Evolution-Three'].strip() != "":
            new_pokemon = pokemon_inventory[pokemon]['Evolution-Three'].lower()
            pokemon_inventory[new_pokemon] = get_pokemon_dict(search_parameter=value["Location"])[new_pokemon]
            pokemon_inventory.pop(pokemon)
            print_evolution(pokemon.title(), new_pokemon.title())


def level_up(character, pokemon_inventory):
    if character["EXP"] >= 100:
        character["Level"] += 1
        character["EXP"] -= 100
        print(f"You have leveled up!\nCurrent Level: {character['Level']}")
        evolve(pokemon_inventory)
