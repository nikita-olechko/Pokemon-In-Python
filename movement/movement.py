from board.make_board import make_board
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
    :raises: TypeError if board or character not dictionaries
    :raises: KeyError if character's position not in board keys
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
    if type(board) != dict or type(character) != dict:
        raise TypeError("board and character must be dictionaries")
    if (character['X-coordinate'], character['Y-coordinate']) not in board:
        raise KeyError("Character's position is outside of the board")
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
        user_input = str.lower(input("To move, enter\nW: North, A: West, S: South, or D: East: "))
        if user_input not in directions:
            print("Please enter a real direction\n")
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
    :raises: TypeError if board or character not dictionaries
    :raises: TypeError if direction not a string
    >>> player = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> game_board = make_board(5, 5)
    >>> player_direction = "s"
    >>> validate_move(game_board, player, player_direction)
    True
    >>> player = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> game_board = make_board(5, 5)
    >>> player_direction = "w"
    >>> validate_move(game_board, player, player_direction)
    <BLANKLINE>
    That is not a valid move
    <BLANKLINE>
    <BLANKLINE>
    False
    """
    if type(board) != dict or type(character) != dict:
        raise TypeError("board and character must be dictionaries")
    if type(direction) != str:
        raise TypeError("direction must be a string")
    if not direction_in_board(board, character, direction):
        return False
    if ocean_in_way(board, character, direction):
        if can_cross_ocean(character):
            return True
        else:
            return False
    return True


def direction_in_board(board, character, direction):
    """
    Checks if user input is a direction in the board.
    :param board: a dictionary containing coordinates as tuples
    :param character: a character with "X-coordinate" and "Y-coordinate" as keys
    :param direction: a valid direction
    :precondition: board must be a dictionary containing coordinates as tuples
    :precondition: character must be a dictionary containing the key values "X-coordinate", "X-coordinate", "Current HP"
    :precondition: direction must be a string from 1-4 or "up", "down", "left", or "right"
    :return: True if direction in board, else False
    :raises: TypeError if board or character not dictionaries
    :raises: TypeError if direction not a string
    >>> player = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> game_board = make_board(5, 5)
    >>> player_direction = "w"
    >>> direction_in_board(game_board, player, player_direction)
    <BLANKLINE>
    That is not a valid move
    <BLANKLINE>
    <BLANKLINE>
    False
    >>> player = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> game_board = make_board(5, 5)
    >>> player_direction = "s"
    >>> direction_in_board(game_board, player, player_direction)
    True
    """
    if type(board) != dict or type(character) != dict:
        raise TypeError("board and character must be dictionaries")
    if type(direction) != str:
        raise TypeError("direction must be a string")
    current_position = (character['X-coordinate'], character['Y-coordinate'])
    if current_position not in board:
        return False
    if direction in {'w': -1, 's': 1, 'north': -1, 'south': 1}:
        new_y = character['Y-coordinate'] + {'w': -1, 's': 1, 'north': -1, 'south': 1}[direction]
        if (character['X-coordinate'], new_y) not in board:
            print_rolling_dialogue("\nThat is not a valid move\n")
            return False
    else:
        new_x = character['X-coordinate'] + {'a': -1, 'd': 1, 'east': -1, 'west': 1}[direction]
        if (new_x, character['X-coordinate']) not in board:
            print_rolling_dialogue("\nThat is not a valid move\n")
            return False
    return True


def ocean_in_way(board: dict, character: dict, direction: str) -> bool:
    """
    Checks if ocean in way.
    :param board: a dictionary containing coordinates as tuples
    :param character: a character with "X-coordinate" and "Y-coordinate" as keys
    :param direction: a valid direction
    :precondition: board must be a dictionary containing coordinates as tuples
    :precondition: character must be a dictionary containing the key values "X-coordinate", "X-coordinate", "Current HP"
    :precondition: direction must be a string from 1-4 or "up", "down", "left", or "right"
    :return: True if ocean in way, else False
    :return: True if direction in board, else False
    :raises: TypeError if board or character not dictionaries
    :raises: TypeError if direction not a string
    >>> player = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> game_board = make_board(5, 5)
    >>> player_direction = "d"
    >>> ocean_in_way(game_board, player, player_direction)
    False
    >>> player = {"X-coordinate": 2, "Y-coordinate": 2}
    >>> game_board = make_board(5, 5)
    >>> player_direction = "d"
    >>> ocean_in_way(game_board, player, player_direction)
    True
    """
    if type(board) != dict or type(character) != dict:
        raise TypeError("board and character must be dictionaries")
    if type(direction) != str:
        raise TypeError("direction must be a string")
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


def can_cross_ocean(character: dict) -> bool:
    """
    Verifies if character can cross the ocean.
    :param character: a character with "X-coordinate", "Y-coordinate", and "Boat" as keys
    :precondition: character must be a dictionary
    :precondition: character must contain the key values "X-coordinate", "Y-coordinate", "Boat"
    :return: True if character can cross ocean, else False
    :raise: TypeError if character is not a dictionary
    :raise: KeyError if character does have the keys "X-coordinate", "Y-coordinate", "Boat"
    >>> player = {"Boat": False, "X-coordinate" : 2, "Y-coordinate": 2}
    >>> can_cross_ocean(player)
    <BLANKLINE>
    Hmmm...you need some way to cross the water...
    <BLANKLINE>
    False
    >>> player = {"Boat": True, "X-coordinate" : 2, "Y-coordinate": 2}
    >>> can_cross_ocean(player)
    True
    """
    if type(character) != dict:
        raise TypeError("character must be a dictionary")
    if "X-coordinate" not in character.keys() or "Y-coordinate" not in character.keys() or \
            "Boat" not in character.keys():
        raise KeyError('character must contain the keys "X-coordinate", "Y-coordinate", and "Boat"')
    if character["Boat"]:
        return True
    print("\nHmmm...you need some way to cross the water...\n")
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
    :raises: TypeError if character not a dictionary
    :raises: TypeError if direction not a string
    >>> player = {"X-coordinate": 1, "Y-coordinate": 1}
    >>> direct = "w"
    >>> move_character(player, direct)
    >>> player
    {'X-coordinate': 1, 'Y-coordinate': 0}
    >>> player = {"X-coordinate": 1, "Y-coordinate": 1}
    >>> direct = "d"
    >>> move_character(player, direct)
    >>> player
    {'X-coordinate': 2, 'Y-coordinate': 1}
    """
    if type(character) != dict:
        raise TypeError("character must be a dictionary")
    if type(direction) != str:
        raise TypeError("direction must be a string")
    y_dict = {'w': -1, 's': 1, 'north': -1, 'south': 1}
    x_dict = {'a': -1, 'd': 1, 'east': -1, 'west': 1}
    if direction in y_dict:
        character['Y-coordinate'] += y_dict[direction]
    else:
        character['X-coordinate'] += x_dict[direction]


def main():
    """
    Drives the program.
    """


if __name__ == "__main__":
    main()
