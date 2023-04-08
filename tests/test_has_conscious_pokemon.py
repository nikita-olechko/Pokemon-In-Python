from unittest import TestCase

from combat.combat import has_conscious_pokemon


class TestHasConsciousPokemon(TestCase):
    def test_has_conscious_pokemon_proper_true(self):
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
        self.assertEqual(has_conscious_pokemon(pokemon_inventory), True)

    def test_has_conscious_pokemon_proper_False(self):
        pokemon_inventory = {"arceus": {
            "Class": "Legendary",
            "Current HP": 0,
            "Evolution-One": "Arceus",
            "Location": "Volcano",
            "Move-Four": "Earthquake",
            "Move-One": "Judgment",
            "Move-Three": "Fissure",
            "Move-Two": "Hyper Beam"
        }}
        self.assertEqual(has_conscious_pokemon(pokemon_inventory), False)

    def test_multiple_pokemon_True(self):
        pokemon_inventory = {"arceus": {
            "Class": "Legendary",
            "Current HP": 0,
            "Evolution-One": "Arceus",
            "Location": "Volcano",
            "Move-Four": "Earthquake",
            "Move-One": "Judgment",
            "Move-Three": "Fissure",
            "Move-Two": "Hyper Beam"
        }, "giratina": {
            "Class": "Legendary",
            "Current HP": 60,
            "Evolution-One": "Arceus",
            "Location": "Volcano",
            "Move-Four": "Earthquake",
            "Move-One": "Judgment",
            "Move-Three": "Fissure",
            "Move-Two": "Hyper Beam"
        }}
        self.assertEqual(has_conscious_pokemon(pokemon_inventory), True)

    def test_multiple_pokemon_False(self):
        pokemon_inventory = {"arceus": {
            "Class": "Legendary",
            "Current HP": 0,
            "Evolution-One": "Arceus",
            "Location": "Volcano",
            "Move-Four": "Earthquake",
            "Move-One": "Judgment",
            "Move-Three": "Fissure",
            "Move-Two": "Hyper Beam"
        }, "giratina": {
            "Class": "Legendary",
            "Current HP": 0,
            "Evolution-One": "Arceus",
            "Location": "Volcano",
            "Move-Four": "Earthquake",
            "Move-One": "Judgment",
            "Move-Three": "Fissure",
            "Move-Two": "Hyper Beam"
        }}
        self.assertEqual(has_conscious_pokemon(pokemon_inventory), False)

    def test_TypeError(self):
        pokemon_inventory = "arceus"
        with self.assertRaises(TypeError):
            has_conscious_pokemon(pokemon_inventory)
