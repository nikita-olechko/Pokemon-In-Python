from character.shop import enter_shop


def at_shop(character):
    if (character["X-coordinate"], character["Y-coordinate"]) == (1, 0):
        return True


def at_arceus(character):
    if (character["X-coordinate"], character["Y-coordinate"]) == (4, 4):
        return True
    else:
        return False


def at_special_location(character):
    if at_shop(character) or at_arceus(character):
        return True
    else:
        return False
