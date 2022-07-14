import unittest
from src.river import River
from src.fish import Fish

class TestRiver(unittest.TestCase):

    def setUp(self):
        self.fish1 = Fish("Fred")
        self.fish2 = Fish("Jaws")
        self.river = River("Clyde", [self.fish1, self.fish2])

    def test_river_has_name(self):                         
        self.assertEqual ("Clyde", self.river.name)                                            

    def test_river_has_fish(self):
        self.assertEqual(2, self.river.fish_count())

    def test_can_get_fish(self):
        fish = self.river.give_fish()
        self.assertEqual(1, self.river.fish_count())
        self.assertEqual("Jaws", fish.name)