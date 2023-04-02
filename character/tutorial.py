import time

from playsound import playsound

from misc.misc import print_dialogue, print_rolling_dialogue


def play_tutorial():
    while True:
        do_tutorial = input("Play Tutorial? (y/n): ").lower()
        if do_tutorial == 'y':
            return True
        elif do_tutorial == 'n':
            return False
        else:
            print("Invalid input")
            continue


def tutorial():
    print_rolling_dialogue(". . . ", delay=1)
    playsound('Opening.wav', block=False)
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
    print_rolling_dialogue("I study Pokémon as a profession! In fact, I have a surprise for you.\n"
                           "Wild Pokémon live in the Forest, Mine, Ocean, Volcano, and Plains! If you encounter them, "
                           "you need to be prepared.")
    time.sleep(2.5)
    print_rolling_dialogue("That's why I have I'm going to give you a Pokémon! Using this Pokémon, you can battle and "
                           "catch Pokémon\nout there in the wild. You can have up to 6 Pokémon with you at at time, "
                           "and you can "
                           "explore the world with them!\nPokémon can also evolve with enough EXP, "
                           "which you get from battling.\nWell, that's about it. Go ahead and pick one of my Pokémon "
                           "when you're ready.\n")
    print_rolling_dialogue(". . .", delay=1)
    time.sleep(0.5)
    print_rolling_dialogue("Oh yeah, one last thing. Legend has it that Arceus, the God of all Pokémon, "
                           "lives at the top of the "
                           "Volcano.\nArceus was born before the universe as we know it existed, and "
                           "shaped the world we live in today...\n")
    time.sleep(0.5)
    print_dialogue('So uh, don\'t fight it ok? The universe as we know it might cease to exist!\n'
                   'Unless you\'re crazy and want to "beat the game" or whatever you kids say\nThat\'s it, '
                   'have fun!')
    time.sleep(5)
    input("Enter any key to choose a pokemon: ")
