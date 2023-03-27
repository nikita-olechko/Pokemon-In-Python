"""
Nikita Olechko
A01337397
"""

import random

from board.make_board import make_board
from character.character import make_character, new_character, get_starter_pokemon

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
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    user_info = new_character()
    character = make_character(user_info)
    pokemon = get_starter_pokemon(user_info)
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
