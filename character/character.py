from utilities.utilities import read_json
from utilities.display import display_pokemon


def choose_starter_pokemon() -> str:
    """
    Choose starter pokemon

    A function that asks the user to choose a starter pokemon.
    :postcondition: gets a starter pokemon from the user
    :return: name of a starter pokemon as a string
    """
    starters_evolution_1 = ['bulbasaur', 'charmander', 'squirtle']
    starter_dict = {}
    for pokemon in starters_evolution_1:
        starter_dict[pokemon] = read_json("json_data/starter_pokemon.json")[pokemon]
    display_pokemon(starter_dict)
    while True:
        chosen_pokemon = input("Choose a starter Pokemon: ").lower()
        if chosen_pokemon not in starters_evolution_1 and chosen_pokemon not in ["1", "2", "3"]:
            print("That's not one of the starter Pokemon! Pick again.")
            continue
        elif chosen_pokemon in starters_evolution_1:
            return chosen_pokemon
        else:
            return starters_evolution_1[int(chosen_pokemon)-1]


def make_character(tutorial_bool: bool, login_data: dict) -> dict:
    """
    Make a character.

    A function that creates a new character at the starting coordinates (0, 0) with 5 HP.
    :param tutorial_bool: a boolean value representing the character has played the tutorial
    :param login_data: a dictionary containign the users login details
    :precondition: tutorial bool must be a boolean value
    :precondition: login_data must be a dictionary
    :precondition: login_data must contain the keys 'Username' and 'Password'
    :postcondition: creates a character
    :return: dictionary with starting character values
    :raise: TypeError if tutorial_bool is not a boolean
    :raise: TypeError if login_data is not a dictionary
    :raise: KeyError if login_data does not contain the keys 'Username' and 'Password'
    >>> login_details = {"Username": "Username", "Password": "Password"}
    >>> tutorial_boolean = True
    >>> make_character(tutorial_boolean, login_details)["Tutorial"]
    True
    >>> login_details = {"Username": "Bob", "Password": "RobertRules"}
    >>> tutorial_boolean = True
    >>> make_character(tutorial_boolean, login_details)["Username"]
    'Bob'
    """
    if type(tutorial_bool) != bool:
        raise TypeError("tutorial_bool must be a boolean value")
    if type(login_data) != dict:
        raise TypeError("login_data must be a dictionary")
    if 'Username' not in list(login_data.keys()) or 'Password' not in list(login_data.keys()):
        raise KeyError("login_data must contain the keys 'Username' and 'Password'")
    character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5, "EXP": 0, "Level": 1, "Boat": False,
                 "Pokeballs": 2, "Gold": 100, "Tutorial": False, "Victory": False, "Username": login_data["Username"],
                 "Password": login_data["Password"]}
    if tutorial_bool:
        character['Tutorial'] = True
    return character


def get_starter_pokemon(pokemon: str) -> dict:
    """
    Retrieve data of a given starter pokemon.
    :param: the name of a pokemon as a string
    :precondition: pokemon must be a string
    :precondition: pokemon must a key in json_data/starter_pokemon.json
    :return: dictionary of specified starter pokemon stats
    :raise: TypeError if pokemon is not a string
    :raise: KeyError if pokemon not in starter pokemon
    """
    if type(pokemon) != str:
        raise TypeError("pokemon must be a string")
    if pokemon not in ['bulbasaur', 'charmander', 'squirtle']:
        raise KeyError("pokemon must be one of the starter pokemon")
    pokemon = {pokemon: read_json("json_data/starter_pokemon.json")[pokemon]}
    return pokemon


def achieved_goal(character: dict) -> bool:
    """
    Checks whether character has achieved victory.
    :param character: a dictionary containing character stats
    :precondition: character must have a key 'Victory' and a boolean as a value
    :postcondition: checks if victory is achieved
    :return: True if victory, else False
    :raise: TypeError if character is not a dictionary
    :raise: KeyError if character does not have the key 'Victory'
    >>> player = {"Victory": False}
    >>> achieved_goal(player)
    False
    >>> player = {"Victory": True}
    >>> achieved_goal(player)
    True
    """
    if type(character) != dict:
        raise TypeError("pokemon must be a dictionary")
    if 'Victory' not in list(character.keys()):
        raise KeyError("character must contain the key 'Victory'")
    if character['Victory']:
        return True
    else:
        return False


def main():
    """
    Drives the program.
    """


if __name__ == "__main__":
    main()
