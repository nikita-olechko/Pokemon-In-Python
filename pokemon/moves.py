from pokemon.finding_pokemon import read_json


def get_moves() -> dict:
    """
    Retrieves all moves from a json file.
    @postcondition: retrieves dictionary of moves
    @return: dictionary of moves with move names as keys and values as stats
    """
    all_moves = read_json("json_data/moves.json")
    return all_moves
