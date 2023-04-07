"""
Nikita Olechko
A01337397
"""

from board.make_board import make_board, display_board
from character.character import make_character, get_starter_pokemon, choose_starter_pokemon, achieved_goal
from character.leveling import level_up, evolve
from character.saving import prompt_load_old_save, get_new_player_details, get_old_save_login, create_new_save, \
    save_game, retrieve_save_data
from character.shop import enter_shop
from character.tutorial import play_tutorial, tutorial
from combat.combat import get_combat_details, combat_loop, victory_sequence, defeat_sequence
from movement.movement import describe_current_location, get_user_choice, validate_move, move_character, check_for_foes
from movement.special_locations import at_special_location, at_shop, beat_the_game, at_arceus, reset_health
from utilities.utilities import print_rolling_dialogue


def game():
    """
    Drives the game.
    """
    board = make_board(5, 5)
    display_board()
    if prompt_load_old_save():
        old_save_data = get_old_save_login()
        if "Don't Load" not in list(old_save_data.values()):
            character = retrieve_save_data(old_save_data)["Character"]
            pokemon_inventory = retrieve_save_data(old_save_data)["Pokemon_Inventory"]
        else:
            tutorial_bool = play_tutorial()
            if tutorial_bool:
                tutorial()
            new_save_data = get_new_player_details()
            character = make_character(tutorial_bool, new_save_data)
            pokemon_inventory = get_starter_pokemon(choose_starter_pokemon())
            create_new_save(character, pokemon_inventory)
    else:
        tutorial_bool = play_tutorial()
        if tutorial_bool:
            tutorial()
        new_save_data = get_new_player_details()
        character = make_character(tutorial_bool, new_save_data)
        pokemon_inventory = get_starter_pokemon(choose_starter_pokemon())
        create_new_save(character, pokemon_inventory)
    while not achieved_goal(character):
        display_board()
        describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            describe_current_location(board, character)
            if at_special_location(character):
                if at_shop(character):
                    enter_shop(character)
                elif at_arceus(character):
                    print_rolling_dialogue("\t\nYou walk into the lair of the God, Arceus.\n")
                    combat_details = get_combat_details(character, board, pokemon_inventory, enemy_name='arceus')
                    if combat_loop(combat_details):
                        character['Victory'] = True
                        beat_the_game()
                        return
                    else:
                        defeat_sequence(character, combat_details["enemy_name"])
                        return
                else:
                    reset_health(pokemon_inventory)
                    save_game(character, pokemon_inventory)

            else:
                if check_for_foes():
                    combat_details = get_combat_details(character, board, pokemon_inventory)
                    if combat_loop(combat_details):
                        victory_sequence(pokemon_inventory, combat_details["enemy_name"], character, board)
                        if level_up(character):
                            evolve(pokemon_inventory)
                    else:
                        defeat_sequence(character, combat_details["enemy_name"])
                        return


def main():
    """
    Drives the program.
    """
    game()


if __name__ == "__main__":
    main()
