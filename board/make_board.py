from board import MINIMUM_NUMBER_OF_COLUMNS, MINIMUM_NUMBER_OF_ROWS


def make_board(rows: int, columns: int) -> dict:
    """
    Create a board of rows by columns.

    A function that creates a board of coordinates with a room description at each coordinate.
    :param rows: an integer greater than or equal to 2
    :param columns: an integer greater than or equal to 2
    :precondition: rows must be an integer greater than or equal to 2
    :precondition: columns must be an integer greater than or equal to 2
    :postcondition: creates a board of specified size
    :return: dictionary of rooms with the keys as coordinates and the values as descriptions
    """
    if rows < MINIMUM_NUMBER_OF_ROWS or columns < MINIMUM_NUMBER_OF_COLUMNS:
        raise ValueError('Dimensions must be 2 or greater')
    list_of_descriptions = ['Hospital  ', 'Shop   ', 'Ocean  ', 'Volcano', 'Volcano',
                            'Forest ', 'Forest ', 'Ocean  ', 'Volcano', 'Volcano',
                            'Forest ', 'Forest ', 'Ocean  ', 'Ocean  ', 'Ocean  ',
                            "Mine   ", "Mine   ", 'Forest ', 'Plains ', 'Plains ',
                            "Mine   ", "Mine   ", 'Forest ', 'Plains ', 'Plains ']
    board = {(row, column): '' for row in range(rows) for column in range(columns)}
    index = 0
    for column in range(columns):
        for row in range(rows):
            board[(row, column)] = list_of_descriptions[index]
            index += 1
    return board


def display_board() -> None:
    """
    Displays a board.
    :postcondition: prints the game board
    """
    board = "_________________________________________________\n" \
            "Hospital | Shop    | Ocean   | Volcano | Volcano \n" \
            "_________________________________________________\n" \
            "Forest   | Forest  | Ocean   | Volcano | Volcano \n" \
            "_________________________________________________\n" \
            "Forest   | Forest  | Ocean   | Ocean   | Ocean   \n" \
            "_________________________________________________\n" \
            "Mine     | Mine    | Forest  | Plains  | Plains  \n" \
            "_________________________________________________\n" \
            "Mine     | Mine    | Forest  | Plains  | Plains  \n" \
            "_________________________________________________\n"
    print(board)
