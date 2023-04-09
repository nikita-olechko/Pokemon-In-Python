from playsound import playsound

from utilities.utilities import print_rolling_dialogue, all_prefixes


def display_shop_items(character: dict) -> None:
    """
    Displays shop items
    :param character: a dictionary representing character information
    :precondition: character must be a dictionary
    :precondition: character must have 'Boat' as a key and True or False as the value
    :postcondition: displays available items in shop
    :raise: TypeError if character is not a dictionary
    :raise: KeyError if "Boat" is not a key in character
    """
    if type(character) != dict:
        raise TypeError("character must be a dictionary")
    if "Boat" not in character.keys():
        raise KeyError("character must contain the key 'Boat'")
    shop_list = f"| 1: Pokéball, 50 Gold | "
    if not character['Boat']:
        shop_list += f"2: Boat, 150 Gold |"
    print(f"\t{shop_list}\n")


def buy_items(character: dict) -> None:
    """
    Buy items from the shop.

    A function that updates a character dictionary with items purchased from a shop.
    :param character: a dictionary representing character information
    :precondition: character must be a dictionary
    :precondition: character must have 'Pokeballs' : integer as a key-value pair
    :precondition: character must have 'Gold' : integer as a key-value pair
    :precondition: character must have 'Boat' : True or False as a key-value pair
    :postcondition: updates character dictionary with purchased items
    :raise: TypeError if character is not a dictionary
    :raise: KeyError if keys 'Gold', 'Pokeballs', and 'Boat' are not in character
    """
    if type(character) != dict:
        raise TypeError("character must be a dictionary")
    if "Boat" not in character.keys() or "Pokeballs" not in character.keys() or "Gold" not in character.keys():
        raise KeyError("character must contain the keys 'Gold', 'Boat', and 'Pokeballs'")
    while True:
        print(f"\tYou have {character['Gold']} gold and {character['Pokeballs']} Pokéballs.\n")
        display_shop_items(character)
        item = input("\tPress Q to leave the shop. What would you like to buy?: ").lower()
        if item == "1" or item in all_prefixes("pokeball"):
            buy_pokeball(character, item)
        elif (item == "2" or item in all_prefixes("boat")) and not character["Boat"]:
            buy_boat(character, item)
        elif item == 'q':
            return
        else:
            print(f"\tThat's not a valid option.\n")
            continue


def buy_pokeball(character: dict, item: str) -> None:
    """
    Buys a pokeball if enough gold
    :param character: a dictionary containing character values
    :param item: a string indicating which item to play
    :precondition: character must contain the keys 'Pokeballs' and 'Gold'
    :precondition: item be the string 1 or a prefix of the word 'Pokeballs'
    :postcondition: adds a pokeball to character if enough gold
    :raise: TypeError if character is not a dictionary
    :raise: TypeError if item is not a string
    :raise: KeyError if keys 'Pokeballs' or 'Gold not in character
    :raise: ValueError if item not the string '1' and not in all_prefixes('Pokeballs')
    """
    if type(character) != dict:
        raise TypeError("character must be a dictionary")
    if type(item) != str:
        raise TypeError("item must be a string")
    if "Pokeballs" not in character.keys() or "Gold" not in character.keys():
        raise KeyError("character must contain the keys 'Gold' and 'Pokeballs'")
    if item != '1' and item not in all_prefixes('pokeballs'):
        raise ValueError("item must be the string '1' or in all_prefixes('pokeballs')")
    if enough_gold(character, item):
        character["Pokeballs"] += 1
        character['Gold'] -= 50
        print("\n\tYou bought a Pokeball!\n")


def buy_boat(character: dict, item: str) -> None:
    """
    Buys a boat if enough gold
    :param character: a dictionary containing character values
    :param item: a string indicating which item to play
    :precondition: character must contain the keys 'Boat' and 'Gold'
    :precondition: item be the string 1 or a prefix of the word 'Boat'
    :postcondition: adds a pokeball to character if enough gold
    :raise: TypeError if character is not a dictionary
    :raise: TypeError if item is not a string
    :raise: KeyError if keys 'Boat' or 'Gold not in character
    :raise: ValueError if item not the string '2' and not in all_prefixes('Boat')
    """
    if type(character) != dict:
        raise TypeError("character must be a dictionary")
    if type(item) != str:
        raise TypeError("item must be a string")
    if "Boat" not in character.keys() or "Gold" not in character.keys():
        raise KeyError("character must contain the keys 'Gold' and 'Boat'")
    if item != '2' and item not in all_prefixes('boat'):
        raise ValueError("item must be the string '2' or in all_prefixes('boat')")
    if enough_gold(character, item):
        character["Boat"] += 1
        character['Gold'] -= 150
        print(f"\n\tYou bought a Boat! You can now cross the ocean.\n")


def enough_gold(character: dict, item: str) -> bool:
    """
    Checks if character has enough gold for an item.
    :param character: a dictionary with character data
    :param item: a string representing the item to buy
    :precondition: character must be a dictionary
    :precondition: character have "Gold" as a key and an integer as a value
    :precondition: character have "Boat" as a key and a boolean as a value
    :precondition: character have "Pokeballs" as a key and an integer as a value
    :precondition: item must be the string "boat" or the string "pokeball"
    :return: True if enough gold to buy item, else False
    :raise: TypeError if character is not a dictionary
    :raise: TypeError if item is not a string
    :raise: KeyError if keys 'Boat' or 'Gold not in character
    :raise: ValueError if item not the string '2' and not in all_prefixes('Boat')
    >>> player = {"Gold": 150, "Pokeballs": 2, "Boat": False}
    >>> buy = "1"
    >>> enough_gold(player, buy)
    True
    >>> player = {"Gold": 180, "Pokeballs": 2, "Boat": False}
    >>> buy = "2"
    >>> enough_gold(player, buy)
    True
    """
    if type(character) != dict:
        raise TypeError("character must be a dictionary")
    if type(item) != str:
        raise TypeError("item must be a string")
    if "Boat" not in character.keys() or "Gold" not in character.keys() or "Pokeballs" not in character.keys():
        raise KeyError("character must contain the keys 'Gold', 'Pokeballs', 'Boat'")
    if item not in ['1', '2'] and item not in all_prefixes('boat') and item not in all_prefixes('pokeball'):
        raise ValueError("item must be the string '1', '2' or in all_prefixes('Boat'), or in all_prefixes('pokeball')")
    if (item == "1" or item in all_prefixes("pokeball")) and character["Gold"] >= 50:
        return True
    elif (item == "2" or item in all_prefixes("boat")) and character["Gold"] >= 150:
        return True
    elif (item == "1" or item in all_prefixes("pokeball")) and character["Gold"] < 50:
        print_rolling_dialogue(f"\n\tYou don't have enough gold for a Pokeball.\n")
        return False
    else:
        print_rolling_dialogue(f"\n\tYou don't have enough gold for a Boat.\n")
        return False


def shop_tutorial() -> None:
    """
    Displays a shop tutorial.
    :postcondition: displays a shop tutorial for the user
    """
    print_rolling_dialogue(
        f"\tOh hello! Haven't seen you around before - you must be new here. Let me give you a tour of my shop!\n")
    print(f"\t⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜\n"
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
    print_rolling_dialogue(f"\tThese are Pokéballs! They're for sale here in my shop.\n\t"
                           "Out there in the wild, after you defeat a Pokémon you can capture it "
                           "using a Pokéball.\n\t"
                           "The Pokémon will be added to your inventory, "
                           "and you can use it in combat later.\n\t"
                           "\n"
                           "Looks like you have some Pokéballs already. To buy more, come back here anytime.\n"
                           "I've also got a boat for sale! Limited time offer: only 150 gold!!\n")


def enter_shop(character: dict) -> None:
    """
    Sets up the conditions to enter the shop.

    A function that sets the conditions to enter the shop by playing the tutorial and music.
    :param character: a dictionary with character data
    :precondition: character must be a dictionary
    :precondition: character have "Gold" as a key and an integer as a value
    :postcondition: sets up the conditions to enter the shop
    :raise: TypeError if character is not a dictionary
    """
    if type(character) != dict:
        raise TypeError("character must be a dictionary")
    if character['Tutorial']:
        shop_tutorial()
        character['Tutorial'] = False
    playsound("music/Jigglypuff's Song.wav", block=False)
    buy_items(character)
    print(f"\tThank you, come again!")


def main():
    """
    Drives the program.
    """


if __name__ == "__main__":
    main()
