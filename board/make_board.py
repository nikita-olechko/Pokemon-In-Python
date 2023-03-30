

def forest_biome():
    pass


def volcano_biome():
    pass


def ocean_biome():
    pass


def mine_biome():
    pass


def make_board(rows: int, columns: int) -> dict:
    """
    Create a board of rows by columns.

    A function that creates a board of coordinates with a funky room description at each coordinate.
    :param rows: an integer greater than or equal to 2
    :param columns: an integer greater than or equal to 2
    :precondition: rows must be an integer greater than or equal to 2
    :precondition: columns must be an integer greater than or equal to 2
    :postcondition: creates a board of specified size
    :return: dictionary of rooms with the keys as coordinates and the values as descriptions
    """
    if rows < 2 or columns < 2:
        raise ValueError('Dimensions must be 2 or greater')
    list_of_descriptions = ['Start  ', 'Shop   ', 'Ocean  ', 'Volcano', 'Volcano',
                            'Forest ', 'Forest ', 'Ocean  ', 'Ocean  ', 'Ocean  ',
                            'Forest ', 'Forest ', 'Ocean  ', 'Ocean  ', 'Ocean  ',
                            "Mine   ", "Mine   ", 'Forest ', 'Plains ', 'Plains ',
                            "Mine   ", "Mine   ", 'Forest ', 'Plains ', 'Boss   ']
    board = {(row, column): '' for row in range(rows) for column in range(columns)}
    index = 0
    for column in range(columns):
        for row in range(rows):
            board[(row, column)] = list_of_descriptions[index]
            index += 1
    return board


def display_board():
    board = "_________________________________________________\n" \
            "Start   | Shop    | Ocean   | Volcano | Volcano  \n" \
            "_________________________________________________\n" \
            "Forest  | Forest  | Ocean   | Ocean   | Ocean    \n" \
            "_________________________________________________\n" \
            "Forest  | Forest  | Ocean   | Ocean   | Ocean    \n" \
            "_________________________________________________\n" \
            "Mine    | Mine    | Forest  | Plains  | Plains   \n" \
            "_________________________________________________\n" \
            "Mine    | Mine    | Forest  | Plains  | Boss     \n" \
            "_________________________________________________\n"
    print(board)
    # board_pairs = list(board.items())
    # index = 0
    # board_string = ""
    # while index < 24:
    #     while index < 24 and board_pairs[index][0][0] == board_pairs[index + 1][0][0]:
    #         board_string += f"{str(board_pairs[index][1])} | "
    #         index += 1
    #     board_string += f"{str(board_pairs[index][1])}  "
    #     if index < 5:
    #         print("_"*len(board_string))
    #     print(board_string)
    #     print("_"*len(board_string))
    #     board_string = ""
    #     index += 1


display_board()
print(make_board(5, 5))
"""
PokeCraft


v = volcano
o = ocean
f = forest
m = mines
s = shop
c = castle


B = Big Boss

_ s o v v
f f o v v 
f f o o o 
m m f _ _
m m f _ B three guards must be fought before final boss


"""
