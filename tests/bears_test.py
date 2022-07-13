import unittest
from src.bears import Bear
from src.fish import Fish

class TestBear(unittest.TestCase):

    def setUp(self):
        self.bear = Bear("Brad", "Grizzly")

    def test_bear_has_name(self):
        actual = self.bear.name
        self.assertEqual("Brad", actual)

    def test_bear_has_type(self):
        actual = self.bear.type
        self.assertEqual("Grizzly", actual)

    def test_eat_fish(self):
        fish = Fish
        self.bear.eat_fish(fish)
        self.assertEqual(1, len(self.bear.stomach))

    def test_food_count(self):
        actual = len(self.bear.stomach)
        self.assertEqual(0, actual)

    # def test_take_fish(self):
    #     fish = Fish
    #     self.bear.take_fish(fish)
    #     self.assertEqual(1, len(self.river.holds_fish))