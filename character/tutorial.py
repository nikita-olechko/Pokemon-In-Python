import time

from playsound import playsound

from utilities.utilities import print_rolling_dialogue, yes_or_no_input


def play_tutorial() -> bool:
    """
    Asks the user whether they want to play a tutorial.
    :postcondition: gets user input on whether they would like to play the tutorial
    :return: True if user wants to play, else False
    """
    print_rolling_dialogue("Play Tutorial? ", new_line=False)
    return yes_or_no_input()


def tutorial() -> None:
    """
    Displays a game tutorial.
    :postcondition: displays a game tutorial for the user
    """
    print("")
    print_rolling_dialogue(". . . ", delay=1)
    playsound('music/Opening.wav', block=False)
    time.sleep(2)
    print_rolling_dialogue("?? What's this ??", delay=0.2)
    time.sleep(7.5)
    print_rolling_dialogue("Well hello, look who's finally awoken!")
    time.sleep(1.5)
    print_rolling_dialogue("My name is Professor Oak. People call me the Pokémon Prof. "
                           "You had quite a fall back there, so let me explain what's going on.\n\n"
                           "Welcome to the world of Pokémon! This world is inhabited by creatures called Pokémon.\n"
                           "For some people, Pokémon are pets. Others use them for battle. What? No it's not animal "
                           "cruelty...")
    time.sleep(2.5)
    print_rolling_dialogue("Myself?? . . .", delay=0.5)
    print_rolling_dialogue("I study Pokémon as a profession!\n"
                           "Wild Pokémon live in the Forest, Mine, Plains, Ocean, and Volcano! They also get stronger"
                           " in each of those respective areas, so be careful!\nI wouldn't go to the "
                           "Volcano unless you have some really strong Pokémon with you.\nRegardless, "
                           "if you encounter a "
                           "wild Pokémon, "
                           "you need to be prepared.")
    time.sleep(2.5)
    print_rolling_dialogue("That's why I'm going to give you a Pokémon! Using this Pokémon, you can battle and "
                           "catch Pokémon\nout there in the wild. You can have up to 6 Pokémon with you at a time, "
                           "and you can "
                           "explore the world with them! You can't have more than one of the same Pokémon though.\n"
                           "\nPokémon can also evolve with enough EXP, but if your Pokémon evolves into a "
                           "Pokémon you already have,\nthe "
                           "other one will run away, since you can't have more than one at at time.\n"
                           "\nWell, that's about it. Go ahead and pick one of my Pokémon "
                           "when you're ready.\n")
    print_rolling_dialogue(". . .", delay=1)
    time.sleep(0.5)
    print_rolling_dialogue("Oh yeah, one last thing. Legend has it that Arceus, the God of all Pokémon, "
                           "lives at the top of the "
                           "Volcano.\nArceus was born before the universe as we know it existed, and "
                           "shaped the world we live in today...\n")
    time.sleep(0.5)
    print_rolling_dialogue('So uh, don\'t fight it ok? The universe as we know it might literally cease to exist!\n'
                           'Unless you\'re crazy and want to "beat the game" or whatever you kids say...\nThat\'s it, '
                           'have fun!')
    time.sleep(5)
    input("Enter any key to continue: ")


def main():
    """
    Drives the program.
    """


if __name__ == "__main__":
    main()
