import json

from pokemon.finding_pokemon import read_json


def get_moves() -> dict:
    all_moves = read_json("json_data/moves.json")
    return all_moves


def read_and_write_json_moves(file):
    with open(file) as json_file:
        move_dict = json.load(json_file)
    all_moves = get_moves()
    for move in all_moves:
        move_dict[move] = all_moves[move]
    with open(file, "w") as json_file:
        json.dump(move_dict, json_file)


def standardize_location(func):
    func_dict = func
    new_dict = func_dict
    for pokemon in func_dict:
        new_dict[pokemon]["Location"] = "Mine"
    print(func_dict)
