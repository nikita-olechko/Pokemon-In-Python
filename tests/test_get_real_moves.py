from unittest import TestCase

from utilities.display import get_real_moves


class TestGetRealMoves(TestCase):
    def test_all_possible_moves(self):
        pokemon_inventory = {"arceus": {
            "Class": "Legendary",
            "Current HP": 600,
            "Evolution-One": "Arceus",
            "Location": "Volcano",
            "Move-Four": "Earthquake",
            "Move-One": "Judgment",
            "Move-Three": "Fissure",
            "Move-Two": "Hyper Beam"
        }}
        combat_pokemon = 'arceus'
        self.assertEqual(get_real_moves(combat_pokemon, pokemon_inventory), {'move_index_list': ['1', '2', '3', '4'],
                                                                             'numbered_list': ['1:', '2:', '3:', '4:'],
                                                                             'options': ['judgment', 'hyper beam',
                                                                                         'fissure', 'earthquake'],
                                                                             'pokemon': {'Class': 'Legendary',
                                                                                         'Current HP': 600,
                                                                                         'Evolution-One': 'Arceus',
                                                                                         'Location': 'Volcano',
                                                                                         'Move-Four': 'Earthquake',
                                                                                         'Move-One': 'Judgment',
                                                                                         'Move-Three': 'Fissure',
                                                                                         'Move-Two': 'Hyper Beam'}})

    def test_three_possible_moves(self):
        pokemon_inventory = {"arceus": {
            "Class": "Legendary",
            "Current HP": 600,
            "Evolution-One": "Arceus",
            "Location": "Volcano",
            "Move-Four": "",
            "Move-One": "Judgment",
            "Move-Three": "Fissure",
            "Move-Two": "Hyper Beam"
        }}
        combat_pokemon = 'arceus'
        self.assertEqual(get_real_moves(combat_pokemon, pokemon_inventory), {'move_index_list': ['1', '2', '3', ''],
                                                                             'numbered_list': ['1:', '2:', '3:', ''],
                                                                             'options': ['judgment', 'hyper beam',
                                                                                         'fissure', ''],
                                                                             'pokemon': {'Class': 'Legendary',
                                                                                         'Current HP': 600,
                                                                                         'Evolution-One': 'Arceus',
                                                                                         'Location': 'Volcano',
                                                                                         'Move-Four': '',
                                                                                         'Move-One': 'Judgment',
                                                                                         'Move-Three': 'Fissure',
                                                                                         'Move-Two': 'Hyper Beam'}})

    def test_only_one_move(self):
        pokemon_inventory = {"arceus": {
            "Class": "Legendary",
            "Current HP": 600,
            "Evolution-One": "Arceus",
            "Location": "Volcano",
            "Move-Four": "",
            "Move-One": "Judgment",
            "Move-Three": "",
            "Move-Two": ""
        }}
        combat_pokemon = 'arceus'
        self.assertEqual(get_real_moves(combat_pokemon, pokemon_inventory), {'move_index_list': ['1', '', '', ''],
                                                                             'numbered_list': ['1:', '', '', ''],
                                                                             'options': ['judgment', '', '', ''],
                                                                             'pokemon': {'Class': 'Legendary',
                                                                                         'Current HP': 600,
                                                                                         'Evolution-One': 'Arceus',
                                                                                         'Location': 'Volcano',
                                                                                         'Move-Four': '',
                                                                                         'Move-One': 'Judgment',
                                                                                         'Move-Three': '',
                                                                                         'Move-Two': ''}})

    def test_TypeError_combat_pokemon(self):
        with self.assertRaises(TypeError):
            get_real_moves({}, {})

    def test_TypeError_pokemon_inventory(self):
        with self.assertRaises(TypeError):
            get_real_moves("", "")
