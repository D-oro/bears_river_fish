import unittest
from src.river import River
from src.fish import Fish

class TestRiver(unittest.TestCase):

    def setUp(self):
        self.river = River("Clyde")
        self.fish_1 = Fish("Fred")
        self.fish_2 = Fish("Fin")
        self.river.holds_fish.append(self.fish_1)
        self.river.holds_fish.append(self.fish_2)

    def test_river_has_name(self):             
        actual = self.river.name                
        self.assertEqual ("Clyde", actual)                                            

    def test_fish_count(self):
        actual = self.river.fish_count()
        self.assertEqual(2, actual)