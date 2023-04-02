import random

from utilities.utilities import print_rolling_dialogue


def describe_current_location(board: dict, character: dict):
    """
    Describes current location and HP.

    A function that prints the character's current location and HP.
    :param board: a dictionary containing tuples of length two containing positive integers
        as keys and strings as values and their corresponding values as strings
    :param character: a dictionary containing the character's current coordinates and HP as keys
    :precondition: board must be a dictionary containing tuples of length two with positive integers
        as keys and strings as values
    :precondition: character must be a dictionary containing the character's current coordinates and HP
    :postcondition: prints a descriptive update to the user with their charater's current data
    >>> game_board = {(0,0): "Room", (0,1): "Room", (1,0): "Room", (1,1): "Room"}
    >>> player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> describe_current_location(game_board, player)
    You are at (0, 0), Room.
    <BLANKLINE>
    >>> game_board = {(0,0): "Room", (0,1): "Room", (1,0): "Room", (1,1): "Room"}
    >>> player = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 3}
    >>> describe_current_location(game_board, player)
    You are at (1, 1), Room.
    <BLANKLINE>
    """
    if (character['X-coordinate'], character['Y-coordinate']) not in board:
        raise ValueError("Character's position is outside of the board")
    print(f"You are at {character['X-coordinate'], character['Y-coordinate']},"
          f" {board[(character['X-coordinate'], character['Y-coordinate'])].strip()}.\n")


def get_user_choice():
    """
    Get user's direction choice.

    A function that gets a chosen direction as standard input from the user.
    :postcondition: continually prompts the user until a valid input is provided
    :return: string of a valid user direction
    """
    directions = ['w', 'a', 's', 'd', 'north', 'south', 'east', 'west']
    while True:
        user_input = str.lower(input("To move, enter\nW: North, A: East, S: South, or D: West: "))
        if user_input not in directions:
            print("Please enter a real direction\n")
            continue
        else:
            break
    return user_input


def validate_move(board: dict, character: dict, direction: str, pokemon: dict) -> bool:
    """
    Verify that direction is a moveable direction within the board.

    A function that checks if direction will move the character to a valid position on the board
    :param pokemon: a dictionary containing pokemon names as keys
    :param board: a dictionary containing tuples of length two containing positive integers
        as keys and strings as values
    :param character: a dictionary containing the character's current coordinates as a tuple of length two containing
        integers and HP as key values
    :param direction: a string from 1-4 or "up", "down", "left", or "right"
    :precondition: board must be a dictionary containing 'coordinate' keys of tuples of length two containing
        two positive integers and their corresponding values as strings
    :precondition: character must be a dictionary containing the key values "X-coordinate", "X-coordinate", "Current HP"
    :precondition: direction must be a string from 1-4 or "up", "down", "left", or "right"
    :precondition: pokemon must be a dictionary containing pokemon names as keys
    :postcondition: verifies if direction will move the user to a valid location on the board
    :return: True if direction moves character to a valid location on the board, else False
    >>> game_board = {(0,0): "Room", (0,1): "Room", (1,0): "Room", (1,1): "Room"}
    >>> player = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> direct = "2"
    >>> validate_move(game_board, player, direct)
    True
    >>> game_board = {(0,0): "Room", (0,1): "Room", (1,0): "Room", (1,1): "Room"}
    >>> player = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> direct = "up"
    >>> validate_move(game_board, player, direct)
    That is not a valid move
    False
    """
    if not direction_in_board(board, character, direction):
        return False
    if ocean_in_way(board, character, direction):
        if can_cross_ocean(character, pokemon):
            return True
        else:
            return False
    return True


def direction_in_board(board, character, direction):
    y_dict = {'w': -1, 's': 1, 'north': -1, 'south': 1}
    x_dict = {'a': -1, 'd': 1, 'east': -1, 'west': 1}
    current_position = (character['X-coordinate'], character['Y-coordinate'])
    if current_position not in board:
        return False
    if direction in y_dict:
        new_y = character['Y-coordinate'] + y_dict[direction]
        if (character['X-coordinate'], new_y) not in board:
            print_rolling_dialogue("\nThat is not a valid move\n")
            return False
    else:
        new_x = character['X-coordinate'] + x_dict[direction]
        if (new_x, character['X-coordinate']) not in board:
            print_rolling_dialogue("\nThat is not a valid move\n")
            return False
    return True


def check_for_foes():
    """
    Return True 1/3 of the time.

    A function that ensures a True is returned 1/3 of the time.
    :postcondition: returns True 1/3 of the time
    :return: True 1/3 of the time, False 2/3 of the time
    """
    if random.randint(1, 3) == 3:
        return True
    return False


def ocean_in_way(board: dict, character: dict, direction: str) -> bool:
    y_dict = {'w': -1, 's': 1, 'north': -1, 'south': 1}
    x_dict = {'a': -1, 'd': 1, 'east': -1, 'west': 1}
    if direction in y_dict:
        new_y = character['Y-coordinate'] + y_dict[direction]
        if board[(character['X-coordinate'], new_y)].strip() == "Ocean":
            return True
    else:
        new_x = character['X-coordinate'] + x_dict[direction]
        if board[(new_x, character['Y-coordinate'])].strip() == "Ocean":
            return True
    return False


def can_cross_ocean(character: dict, pokemon: dict) -> bool:
    if character["Boat"] or has_rideable_pokemon(pokemon):
        return True
    print("\nHmmm...you need some way to cross the water...\n")
    return False


def has_rideable_pokemon(pokemon):
    list_of_rideable_pokemon = ["gyarados", "kyogre"]
    for ride in list_of_rideable_pokemon:
        if ride in pokemon.values():
            return True
    return False


def move_character(character: dict, direction: str):
    """
    Moves character 1 coordinate in provided direction.

    A function that moves the character 1 coordinate in the provided direction.
    :param character: a dictionary containing the character's current coordinates as a tuple of length two containing
        integers
    :param direction: a string from 1-4 or "up", "down", "left", or "right
    :precondition: character must be a dictionary containing the key values "X-coordinate", "X-coordinate"
    :precondition: direction must be a string from 1-4 or "up", "down", "left", or "right"
    :postcondition: character dictionary is updated with new coordinates
    >>> player = {"X-coordinate": 1, "Y-coordinate": 1}
    >>> direct = "2"
    >>> move_character(player, direct)
    >>> player
    {'X-coordinate': 1, 'Y-coordinate': 2}
    >>> player = {"X-coordinate": 1, "Y-coordinate": 1}
    >>> direct = "4"
    >>> move_character(player, direct)
    >>> player
    {'X-coordinate': 2, 'Y-coordinate': 1}
    """
    y_dict = {'w': -1, 's': 1, 'north': -1, 'south': 1}
    x_dict = {'a': -1, 'd': 1, 'east': -1, 'west': 1}
    if direction in y_dict:
        character['Y-coordinate'] += y_dict[direction]
    else:
        character['X-coordinate'] += x_dict[direction]
