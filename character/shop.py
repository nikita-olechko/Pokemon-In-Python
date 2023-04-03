from utilities.utilities import print_rolling_dialogue, all_prefixes


def display_shop_items(character):
    shop_list = "| 1: Pokéball, 50 Gold | "
    if not character['Boat']:
        shop_list += "2: Boat, 150 Gold |"
    print(f"\t{shop_list}\n")


def buy_items(character):
    while True:
        print(f"\tYou have {character['Gold']} gold and {character['Pokeballs']} Pokéballs.\n")
        display_shop_items(character)
        item = input("\tPress Q to leave the shop. What would you like to buy?: ").lower()
        if item == "1" or item in all_prefixes("pokeball"):
            if enough_gold(character, item):
                character["Pokeballs"] += 1
                character['Gold'] -= 50
                print("\n\tYou bought a Pokeball!\n")
        elif item == "2" or item in all_prefixes("boat"):
            if enough_gold(character, item):
                character["Boat"] += 1
                character['Gold'] -= 150
                print("\n\tYou bought a Boat! You can now cross the ocean.\n")
        elif item == 'q':
            return
        else:
            print("\tThat's not a valid option.\n")
            continue


def enough_gold(character, item):
    gold = character["Gold"]
    if (item == "1" or item in all_prefixes("pokeball")) and gold >= 50:
        return True
    elif (item == "2" or item in all_prefixes("boat")) and gold >= 150:
        return True
    elif (item == "1" or item in all_prefixes("pokeball")) and gold < 50:
        print_rolling_dialogue(f"\n\tYou don't have enough gold for a Pokeball.\n")
        return False
    else:
        print_rolling_dialogue(f"\n\tYou don't have enough gold for a Boat.\n")
        return False


def shop_tutorial():
    print_rolling_dialogue(
        "\tOh hello! Haven't seen you around before - you must be new here. Let me give you a tour of my shop!\n")
    print("\t⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜\n"
          "\t⬜⬜⬜⬛⬛🟥🟥🟥🟥🟥⬛⬜⬜⬜\n"
          "\t⬜⬜⬛🟥🟥🟥🟥🟥🟥🟥🟥⬛⬜⬜\n"
          "\t⬜⬛🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛⬜\n"
          "\t⬜⬛🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛⬜\n"
          "\t⬛🟥🟥🟥🟥🟥⬛⬛🟥🟥🟥🟥🟥⬛\n"
          "\t⬛🟥🟥🟥🟥⬛⬜⬜⬛🟥🟥🟥🟥⬛\n"
          "\t⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛\n"
          "\t⬛⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬛\n"
          "\t⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜\n"
          "\t⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜\n"
          "\t⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜\n"
          "\t⬜⬜⬜⬛⬛⬜⬜⬜⬜⬛⬛⬜⬜⬜\n"
          "\t⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜\n")
    print_rolling_dialogue("\tThese are Pokéballs! They're for sale here in my shop.\n\t"
                           "Out there in the wild, after you defeat a Pokémon you can try to capture it "
                           "using a Pokéball.\n\t"
                           "It won't always work, but if it does, the Pokémon will be added to your inventory, "
                           "and you can use it in combat later.\n\t"
                           "\n"
                           "Looks like you have some Pokéballs already. To buy more, just come back here.\n"
                           "I've also got a boat for sale! Limited time offer: only 100 gold!!\n")


def enter_shop(character):
    if character['Tutorial']:
        shop_tutorial()
        character['Tutorial'] = False
    buy_items(character)
    print("\tThank you, come again!")