import itertools

from board import EXACT_NUMBER_OF_ROWS, EXACT_NUMBER_OF_COLUMNS


def make_board(rows: int, columns: int) -> dict:
    """
    Create a board of rows by columns.

    A function that creates a board of coordinates with a room description at each coordinate.
    :param rows: the integer 5
    :param columns: the integer 5
    :precondition: rows must be an integer equal to 5
    :precondition: columns must be an integer equal to 5
    :postcondition: creates a 5x5 board
    :return: dictionary of rooms with the keys as coordinates and the values as descriptions
    """
    if rows != EXACT_NUMBER_OF_ROWS or columns != EXACT_NUMBER_OF_COLUMNS:
        raise ValueError('Dimensions must be 2 or greater')
    list_of_descriptions = ['Hospital  ', 'Shop   ', 'Ocean  ', 'Volcano', 'Volcano',
                            'Forest ', 'Forest ', 'Ocean  ', 'Volcano', 'Volcano',
                            'Forest ', 'Forest ', 'Ocean  ', 'Ocean  ', 'Ocean  ',
                            "Mine   ", "Mine   ", 'Forest ', 'Plains ', 'Plains ',
                            "Mine   ", "Mine   ", 'Forest ', 'Plains ', 'Plains ']
    y_coords = [number for number in range(0, rows)]
    x_coords = [number for number in range(0, columns)]
    coordinates = list(itertools.product(y_coords, x_coords, repeat=1))
    flipped_coords = {coord_pair[::-1]: description for coord_pair in coordinates for description
                      in list_of_descriptions}
    return dict(zip(flipped_coords, list_of_descriptions))


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


def main():
    """
    Drives the program.
    """


if __name__ == "__main__":
    main()
