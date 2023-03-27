import random


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
    list_of_descriptions = ['Start', 'Shop', 'Ocean', 'Volcano', 'Volcano',
                            'Forest', 'Forest', 'Ocean', 'Ocean', 'Ocean',
                            'Forest', 'Forest', 'Ocean', 'Ocean', 'Ocean',
                            "Mine", "Mine", 'Forest', 'Plain', 'Plain',
                            "Mine", "Mine", 'Forest', 'Plain', 'Boss']
    board = {(row, column): '' for row in range(rows) for column in range(columns)}
    index = 0
    for row in range(rows):
        for column in range(columns):
            board[(row, column)] = list_of_descriptions[index]
            index += 1
    return board


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
