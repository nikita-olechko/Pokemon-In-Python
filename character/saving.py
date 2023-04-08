import json

from utilities.utilities import print_rolling_dialogue, yes_or_no_input, read_json


def create_new_save(character: dict, pokemon_inventory: dict) -> None:
    """
    Creates a new save file for the player
    :param character: a dictionary containing character data
    :param pokemon_inventory: a dictionary containing pokemon names as keys and stats as values
    :precondition: character must be a dictionary containing character data
    :precondition: pokemon_inventory must be a dictionary containing pokemon names as keys and stats as values
    :postcondition: creates a new save file for the user
    :raise: TypeError if character or pokemon_inventory is not a dictionary
    :raise: KeyError if "Username" or "Password" are not keys in character
    """
    if type(character) != dict or type(pokemon_inventory) != dict:
        raise TypeError("character and pokemon_inventory must be dictionaries")
    if "Username" not in character.keys() or "Password" not in character.keys():
        raise KeyError("character must contain the keys 'Username' and 'Password'")
    with open("json_data/saves.json") as file:
        saved_games = json.load(file)
        saved_games[character["Username"]] = {character["Password"]: {"Character": character,
                                                                      "Pokemon_Inventory": pokemon_inventory}}
    with open("json_data/saves.json", 'w') as file:
        json.dump(saved_games, file)


def save_game(character: dict, pokemon_inventory: dict) -> None:
    """
    Prompts the user to save the game.
    :param character: a dictionary containing character data
    :param pokemon_inventory: a dictionary containing pokemon names as keys and stats as values
    :precondition: character must be a dictionary containing character data
    :precondition: pokemon_inventory must be a dictionary containing pokemon names as keys and stats as values
    :postcondition: saves game data to json file
    :raise: TypeError if character or pokemon_inventory is not a dictionary
    :raise: KeyError if "Username" or "Password" are not keys in character
    """
    if type(character) != dict or type(pokemon_inventory) != dict:
        raise TypeError("character and pokemon_inventory must be dictionaries")
    if "Username" not in character.keys() or "Password" not in character.keys():
        raise KeyError("character must contain the keys 'Username' and 'Password'")
    print_rolling_dialogue("\nWould you like to save the game? ", new_line=False)
    if yes_or_no_input():
        with open("json_data/saves.json") as file:
            saved_games = json.load(file)
            saved_games[character["Username"]][character["Password"]]["Character"] = character
            saved_games[character["Username"]][character["Password"]]["Pokemon_Inventory"] = pokemon_inventory
        with open("json_data/saves.json", 'w') as file:
            json.dump(saved_games, file)
        print_rolling_dialogue("\nGame has been saved!", delay=0.06)


def prompt_load_old_save() -> bool:
    """
    Asks the user if they want to load an old save file.
    :postcondition: gets user input on loading a save file
    :return: True if yes (y), False if no (n)
    """
    print_rolling_dialogue("Would you like to load a save file? ", new_line=False)
    load = yes_or_no_input()
    return load


def get_new_player_details() -> dict:
    """
    Gets the login details of to create a new save file from the user.
    :postcondition: gets the login details of a new user.
    :return: a dictionary containing the username and password of the new user
    """
    saved_games = read_json("json_data/saves.json")
    while True:
        username = input(
            "Please enter a Username: ")
        password = input("Please enter a Password: ")
        if username not in list(saved_games.keys()):
            print_rolling_dialogue(f"Your Username is {username}!")
            return {"Username": username, "Password": password}
        else:
            print_rolling_dialogue("\nSorry, that Username is not available. Please try a different one!")


def get_old_save_login() -> dict:
    """
    Gets the valid login details of an existing user.
    :postcondition: gets the valid login details of an existing user
    :return: a dictionary containing the valid username and password of the existing user
    """
    saved_games = read_json("json_data/saves.json")
    while True:
        username = input("\nPlease enter your Username: ")
        password = input("\nPlease enter your Password: ")
        if username in list(saved_games.keys()) and list(saved_games[username].keys())[0] == password:
            print_rolling_dialogue(f"Welcome back {username}!")
            return {"Username": username, "Password": password}
        elif username not in list(saved_games.keys()):
            print_rolling_dialogue("\nSorry, that Username does not exist in my database. Try a different one? ",
                                   new_line=False)
            if not yes_or_no_input():
                return {"Don't Load": "Don't Load"}
        else:
            print_rolling_dialogue("\nYour Username and Password do not match. Try again? ",
                                   new_line=False)
            if not yes_or_no_input():
                return {"Don't Load": "Don't Load"}


def retrieve_save_data(old_save_data: dict) -> dict:
    """
    Retrieves the save file of an existing user.
    :postcondition: gets the save file of an existing user
    :return: a dictionary containing the character and pokemon_inventory of an existing user
    :raise: TypeError if old_save_data is not a dictionary
    :raise: KeyError if "Username" or "Password" are not keys in old_save_data
    """
    if type(old_save_data) != dict:
        raise TypeError("old_save_data must be a dictionary")
    if "Username" not in old_save_data.keys() or "Password" not in old_save_data.keys():
        raise KeyError("old_save_data must contain the keys 'Username' and 'Password'")
    all_player_data = read_json("json_data/saves.json")
    username = old_save_data["Username"]
    password = old_save_data["Password"]
    return {"Character": all_player_data[username][password]['Character'],
            "Pokemon_Inventory": all_player_data[username][password]['Pokemon_Inventory']}


def main():
    """
    Drives the program.
    """


if __name__ == "__main__":
    main()
