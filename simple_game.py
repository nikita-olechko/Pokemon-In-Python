"""
Nikita Olechko
A01337397
"""

import random


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

def get_villain():
    """
    Get a random villain and catchphrase.

    A function that picks a random villain and catchphrase from a predetermined list.
    :postcondition: gives a random villain and catchphrase
    :return: list of two elements containing a villain catchphrase and a villain name
    """
    villains = {
        'Doctor Darkhearted, the Diabolical Devil': 'Daring Daredevil',
        'Countess Coldblooded, the Cruel Crone': 'Cunning Crusader',
        'Lord Lethal, the Loathsome Lycanthrope': 'Lethal Legend',
        'Lady Lunatic, the Larcenous Leprechaun': 'Lucky Looter',
        'Baroness Bonecrusher, the Brutal Buccaneer': 'Brutal Buccaneer',
        'Captain Clawed, the Conniving Conquistador': 'Crafty Corsair',
        'Duke Doom, the Dastardly Desperado': 'Deadly Duelist',
        'Emperor Evil, the Egotistical Enigma': 'Eerie Explorer',
        'Fang Face, the Fierce Fiend': 'Fearless Fighter',
        'General Greed, the Greedy Goblin': 'Glorious Guardian',
        'Henchman Hades, the Harried Henchman': 'Heroic Hunter',
        'Inquisitor Ironheart, the Insidious Inquisitor': 'Intrepid Investigator',
        'Jester Jinx, the Jovial Jester': 'Jolly Juggler',
        'King Kraken, the Knavish Kraken': 'Knightly Knight',
        'Lava Lady, the Lascivious Lava Witch': 'Luminous Luminary',
        'Madame Malice, the Monstrous Madwoman': 'Merciless Mercenary',
        'Noble Nefarious, the Nasty Nobleman': 'Nimble Ninja',
        'Overlord Omega, the Omnipotent Overlord': 'Outstanding Overcomer',
        'Pharaoh Phantom, the Phantasmal Pharaoh': 'Phenomenal Phantom',
        'Queen Quicksilver, the Quizzical Queen': 'Quick Quicksilver',
        'Rogue Rascal, the Ruthless Renegade': 'Resourceful Ranger',
        'Sultan Sable, the Sinister Sultan': 'Sneaky Scoundrel',
        'Titan Tenebrous, the Terrible Titan': 'Tenacious Treasure-hunter',
        'Viceroy Venom, the Vengeful Viceroy': 'Valiant Voyager',
        'Wraith Wrangler, the Wily Wraith': 'Wise Wanderer',
        'Xenon Xylophone, the Xenophobic Xylophonist': 'Xenial Xenologist',
        'Yakuzi Yakuza, the Yearning Yokai': 'Yare Yachtsman',
        'Zany Zephyr, the Zesty Zealot': 'Zany Zorro'
    }
    return random.choice(list(villains.items()))


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
        raise ValueError("Dimensions must be 2 or greater")
    list_of_descriptions = ["Game Room", "Kitchen", "Secret Escape Room", "Freezer", "Nude Beach Room", "Beer Room",
                            "Other Beer Room", "Third Beer Room", "Wine Room - Just Kidding It's a Beer Room",
                            "Motorcycle Room", "Other Motorcycle Room", "Flying Kittens Room", "Giant Ducks Room",
                            "Bedroom", "Perpetually Expanding Room", "7-Dimensional Room of Terrors", "Python Room",
                            "Verboten Java Room", "Tiny Room", "Quite Extravagant Room", "Room of Random Adjectives",
                            "Room of 1510 Assignments", "Entrance to the Back Rooms", "Entrance to the Front Rooms",
                            f"Room probably not located at ({rows-1}, {columns-1})", "Ro.om, of! bAd,, gramm0r",
                            f"Room slightly more likely to be located at ({rows-1}, {columns-1})",
                            f"Room slightly more likely to be located at ({rows-1}, {columns-1})",
                            "Room of Eternal Despair", "Room of Eternal Happiness", "Room of Appropriate Allocation of "
                                                                                    "despair and happiness",
                            "Room of Chairs", "Room of High-End Gaming PCs that can only run Minecraft",
                            "Room of Low-End Gaming PCs that can only run CyberPunk on Ultra-High Graphics",
                            "Room of Mild Malcontent", "Room of Wabbajack", "Room of #FF06B5", "This is the Garden",
                            "Entrance to Underworld", "Room of Secrets", "Room of Custard", "The King of All"
                                                                                            " Rooms",
                            "Room of slightly grumpy old people", "Room of all your exes", "Room of your browser"
                                                                                           " history",
                            "Room of friendship", "Room A", "Room Containing 4 pigs",
                            # "Room containing the 5th pig",
                            # "This Room Contains Instructions to the Pig Game - Find all the Pigs in all the Rooms to "
                            # "Win",
                            "This Room contains a duck dressed as a pig",
                            "A Room without any pigs",
                            # "A Room that deducts a pig from your total pig count",
                            # "A Room that is quickly flooding - you have 5 seconds to get out",
                            # "A Room that is quickly flooding - you have 5 seconds to get out",
                            # "A Room that is slowly flooding - you have 10 seconds to get out",
                            # "A Room that is slowly flooding - you have 10 seconds to get out",
                            "A Plain Old Room", "You shouldn't have come to this Room - Please Leave", "Room of BEES",
                            "Room of Pesticides",

                            "This Room Shouldn't Exist", "A room with 'A Brief History of Japan' playing on repeat"
                                                         " on all 6 walls.", "A really pleasant room - please stay",
                            "An emotionally unstable ro-PLEASE DON'T LEAVE ME", "Very Angry Ro-GET OUT "
                                                                                "GET OUT GET OUT!"]
    return {(row, column): f"{random.choice(list_of_descriptions)}" for row in range(rows) for column in range(columns)}


def make_character():
    """
    Make a character.

    A function that creates a new character at the starting coordinates (0, 0) with 5 HP.
    :postcondition: creates a character
    :return: dictionary with starting character values
    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    """
    character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    return character


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
    directions = ["1", "2", "3", '4', "up", "down", "left", "right"]
    while True:
        user_input = str.lower(input("To move, enter\n1: Up, 2: Down, 3: Left, or 4: Right: "))
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
    Return True 25% of the time.

    A function that ensures a True is returned 25% of the time.
    :postcondition: returns True 25% of the time
    :return: True 25% of the time, False 75% of the time
    """
    if random.randint(1, 4) == 4:
        return True
    return False


def guessing_game(character: dict):
    """
    Plays a guessing game with the user.

    A function that plays a simple number guessing game with the user.
    :param character: a dictionary containing "Current HP" as a key and corresponding value as an integer
    :precondition: character must be a dictionary containing "Current HP" as a key and corresponding
        value as an integer
    :postcondition: plays a guessing game with the user and reduces character HP if the user loses
    """
    secret_number = str(random.randint(1, 5))
    villain = get_villain()
    print("_"*len(f"Welcome {villain[1]}. I am {villain[0]}. Prepare to meet your doom!"))
    print(f"Welcome {villain[1]}. I am {villain[0]}. Prepare to meet your doom!")
    print("I have chosen a number between 1 and 5. You must guess what I picked or face my wrath!\n")
    guess = input(f"Enter a number between 1 and 5 inclusive: ")
    if guess == secret_number:
        print("Damn, you survive another day. Begone from here!")
        print("_" * len("Damn, you survive another day. Begone from here!\n"))
    else:
        print(f"Fool! The number was obviously {secret_number}. Take this!")
        character['Current HP'] -= 1
        print(f"Your HP has dropped to {character['Current HP']}")
        print("_" * len("Damn, you survive another day. Begone from here!\n"))


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
    if current_position == list(board.keys())[-1]:
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
    rows = 3
    columns = 3
    board = make_board(rows, columns)
    character = make_character()
    achieved_goal = False
    describe_current_location(board, character)
    while not achieved_goal and is_alive(character):
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            describe_current_location(board, character)
            there_is_a_challenger = check_for_foes()
            achieved_goal = check_if_goal_attained(board, character)
            if there_is_a_challenger:
                guessing_game(character)
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
