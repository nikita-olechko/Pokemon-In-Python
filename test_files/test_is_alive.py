"""
Nikita Olechko
A01337397
"""


from unittest import TestCase
from game import is_alive


class TestIsAlive(TestCase):
    def test_alive_5(self):
        player = {"Current HP": 5}
        alive = is_alive(player)
        self.assertEqual(alive, True)

    def test_alive_3(self):
        player = {"Current HP": 3}
        alive = is_alive(player)
        self.assertEqual(alive, True)

    def test_alive_1(self):
        player = {"Current HP": 1}
        alive = is_alive(player)
        self.assertEqual(alive, True)

    def test_dead(self):
        player = {"Current HP": 0}
        alive = is_alive(player)
        self.assertEqual(alive, False)
