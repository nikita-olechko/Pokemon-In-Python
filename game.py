"""
Nikita Olechko
A01337397
"""


from board.make_board import make_board, display_board
from character.character import make_character, get_starter_pokemon, choose_starter_pokemon
from character.tutorial import play_tutorial
from combat.combat import combat
from movement.movement import describe_current_location, get_user_choice, validate_move, move_character, check_for_foes

"""
Ideas for game:
Time-based combat
Pokemon-like combat
Increase in level grants new combat ability based on character type (mage, warrior)
Difficulty scaling based on time-based combat (3 seconds to respond vs 1 second to respond)


Minecraft (crafting)
Pokemon (optional inventory of pokemon from grassy areas)

Pokemon Freestyle
Pokemon, but optional crafting elements and using your own character as a fighter
(DnD style chance of success?)
"""


def check_if_goal_attained(board: dict, character: dict) -> bool:
    """
    Checks if goal attained.

    A function that checks whether the character has reached the bottom right corner.
    :param character: a dictionary containing the character's current coordinates as a tuple of length two containing
        two integers
    :param board: a dictionary containing tuples of length two containing positive integers
        as keys and strings as values
    :precondition: character must be a dictionary containing the character's current coordinates
    :precondition: board must be a dictionary containing tuples of length two with positive integers as
        keys and strings as values
    :postcondition: verifies if goal has been attained
    :return: True if goal attained, else False
    >>> game_board = {(0,0): "Room", (0,1): "Room", (1,0): "Room", (1,1): "Room"}
    >>> player = {"X-coordinate": 1, "Y-coordinate": 1}
    >>> check_if_goal_attained(game_board, player)
    True
    >>> game_board = {(0,0): "Room", (0,1): "Room", (1,0): "Room", (1,1): "Room"}
    >>> player = {"X-coordinate": 0, "Y-coordinate": 1}
    >>> check_if_goal_attained(game_board, player)
    False
    """
    current_position = (character['X-coordinate'], character['Y-coordinate'])
    if current_position == [board.keys()][-1]:
        return True
    return False


def is_alive(character: dict):
    """
    Checks if character is alive.

    A function that checks whether the character is alive.
    :param character: a dictionary containing the character's "Current HP" as a key and corresponding
        value as an integer
    :precondition: character must be a dictionary containing the character's "Current HP" as a key and corresponding
        value as an integer
    :postcondition: verifies if character is alive
    :return: True if alive, else False
    >>> player = {"Current HP": 5}
    >>> is_alive(player)
    True
    >>> player = {"Current HP": 0}
    >>> is_alive(player)
    False
    """
    if character["Current HP"] > 0:
        return True
    return False


def death():
    """
    Runs death scenario.

    A function that prints a post-mortem message.
    :postcondition: prints a post-mortem message to the user
    >>> death()
    Welp, you've died. Wow, that's impressive, this really wasn't a hard game. Better luck next time!
    """
    print("Welp, you've died. Wow, that's impressive, this really wasn't a hard game. Better luck next time!")


def win():
    """
    Runs win scenario.

    A function that prints a congratulatory message.
    :postcondition: prints a congratulatory message to the user
    >>> win()
    Congratulations! You have mastered this technically, physically, and even philosophically challenging game.
    Go on, noble warrior, and rejoice in your victory. Full marks await you!
    """
    print("Congratulations! You have mastered this technically, physically, and even philosophically challenging"
          " game.\nGo on, noble warrior, and rejoice in your victory. Full marks await you!")


def game():
    """
    Drives the game.
    """
    board = make_board(5, 5)
    display_board()
    tutorial_bool = play_tutorial()
    character = make_character(tutorial_bool)
    pokemon_inventory = get_starter_pokemon(choose_starter_pokemon())
    achieved_goal = False
    while not achieved_goal and is_alive(character):
        display_board()
        describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction, pokemon_inventory)
        if valid_move:
            move_character(character, direction)
            describe_current_location(board, character)
            if special_location():
                continue
            if (character["X-coordinate"], character["Y-coordinate"]) == (4, 4):
                if combat(character, board, pokemon_inventory, enemy_name='Arceus'):
                    achieved_goal = True
                    continue
                else:
                    death()
                    return
            # if check_for_foes():
            if True:
                if combat(character, board, pokemon_inventory):
                    continue
                else:
                    death()
                    return
    if not is_alive(character):
        death()
        return
    if achieved_goal:
        win()


def main():
    """
    Drives the program.
    """
    game()


if __name__ == "__main__":
    main()
