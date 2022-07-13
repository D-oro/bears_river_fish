import unittest
from src.fish import Fish

class TestFish(unittest.TestCase):

    def setUp(self):
        self.fish = Fish("Florence")

    def test_fish_has_name(self):
        actual = self.fish.name
        self.assertEqual("Florence", actual)
