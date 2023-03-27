from pokemon.pokemon import starter_pokemon


def new_character():
    name = input("Please enter your character's name: ")
    while True:
        char_class = input("Choose a starter Pokemon: ")
        if char_class not in starter_pokemon():
            print("That's not one of the starter Pokemon! Pick again.")
            continue
        else:
            break
    difficulties = ["easy", "medium", "hard", "excruciating"]
    while True:
        difficulty = input("Please choose a difficulty: ")
        if difficulty not in difficulties:
            print("That's not a real difficulty.")
            continue
        else:
            break
    chosen_stats = (name, char_class, difficulty)
    return chosen_stats


def make_character(user_info):
    """
    Make a character.

    A function that creates a new character at the starting coordinates (0, 0) with 5 HP.
    :postcondition: creates a character
    :return: dictionary with starting character values
    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    """
    character = {"Name": user_info[0], "Class": user_info[1], "Difficulty": user_info[2],
                 "X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5, "EXP": 0, "Level": 1, "Boat": False}
    return character


def get_starter_pokemon(user_info):
    pokemon = {"Slot 1": starter_pokemon()[user_info]}
    return pokemon
