import random


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
    You are at (0, 0), Room. You have 5 HP
    <BLANKLINE>
    >>> game_board = {(0,0): "Room", (0,1): "Room", (1,0): "Room", (1,1): "Room"}
    >>> player = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 3}
    >>> describe_current_location(game_board, player)
    You are at (1, 1), Room. You have 3 HP
    <BLANKLINE>
    """
    if (character['X-coordinate'], character['Y-coordinate']) not in board:
        raise ValueError("Character's position is outside of the board")
    print(f"You are at {character['X-coordinate'], character['Y-coordinate']},"
          f" {board[(character['X-coordinate'], character['Y-coordinate'])]}. You have {character['Current HP']} HP\n")


def get_user_choice():
    """
    Get user's direction choice.

    A function that gets a chosen direction as standard input from the user.
    :postcondition: continually prompts the user until a valid input is provided
    :return: string of a valid user direction
    """
    directions = ["1", "2", "3", '4', "up", "down", "left", "right",
                  'w', 'a', 's', 'd', 'north', 'south', 'east', 'west']
    while True:
        user_input = str.lower(input("To move, enter\nW: North, A: East, S: South, or D: West: "))
        if user_input not in directions:
            print("Please enter a valid direction")
            continue
        else:
            break
    return user_input


def validate_move(board: dict, character: dict, direction: str) -> bool:
    """
    Verify that direction is a moveable direction within the board.

    A function that checks if direction will move the character to a valid position on the board
    :param board: a dictionary containing tuples of length two containing positive integers
        as keys and strings as values
    :param character: a dictionary containing the character's current coordinates as a tuple of length two containing
        integers and HP as key values
    :param direction: a string from 1-4 or "up", "down", "left", or "right"
    :precondition: board must be a dictionary containing 'coordinate' keys of tuples of length two containing
        two positive integers and their corresponding values as strings
    :precondition: character must be a dictionary containing the key values "X-coordinate", "X-coordinate", "Current HP"
    :precondition: direction must be a string from 1-4 or "up", "down", "left", or "right"
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
    direction_dict = {"up": -1, "down": 1, "left": -1, "right": 1, "1": -1, "2": 1, "3": -1, "4": 1}
    current_position = (character['X-coordinate'], character['Y-coordinate'])
    if current_position not in board:
        return False
    if direction == "up" or direction == "down" or direction == "1" or direction == "2":
        new_y = character['Y-coordinate'] + direction_dict[direction]
        if (character['Y-coordinate'], new_y) not in board:
            print("That is not a valid move")
            return False
    else:
        new_x = character['X-coordinate'] + direction_dict[direction]
        if (new_x, character['X-coordinate']) not in board:
            print("That is not a valid move")
            return False
    return True


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
    direction_dict = {"up": -1, "down": 1, "left": -1, "right": 1, "1": -1, "2": 1, "3": -1, "4": 1}
    if direction == "up" or direction == "down" or direction == "1" or direction == "2":
        character['Y-coordinate'] += direction_dict[direction]
    else:
        character['X-coordinate'] += direction_dict[direction]


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


def check_for_ocean(board: dict, character: dict, direction: str) -> bool:
    current_position = (character['X-coordinate'], character['Y-coordinate'])
    if current_position not in board:
        return False
    if direction == "up" or direction == "down" or direction == "1" or direction == "2":
        new_y = character['Y-coordinate'] + direction_dict[direction]
        if (character['Y-coordinate'], new_y) not in board:
            print("That is not a valid move")
            return False
    else:
        new_x = character['X-coordinate'] + direction_dict[direction]
        if (new_x, character['X-coordinate']) not in board:
            print("That is not a valid move")
            return False
    return True