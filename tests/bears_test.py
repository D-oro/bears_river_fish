import unittest
from src.bears import Bear
from src.fish import Fish
from src.river import River

class TestBear(unittest.TestCase):

    def setUp(self):
        self.bear = Bear("Brad", "Grizzly")

    def test_bear_has_name(self):
        actual = self.bear.name
        self.assertEqual("Brad", actual)

    def test_bear_has_type(self):
        actual = self.bear.type
        self.assertEqual("Grizzly", actual)

    def test_bear_has_empty_stomach(self):
        self.assertEqual(0, self.bear.food_count())

    def test_eat_fish(self):
        fish = Fish("Jaws")
        self.bear.eat_fish(fish)
        self.assertEqual(1, len(self.bear.stomach))
        self.assertEqual([fish], self.bear.stomach)

    def test_food_count(self):
        actual = len(self.bear.stomach)
        self.assertEqual(0, actual)

    def test_bear_can_get_fish_from_river(self):
        river = River("Amazon", [self.fish])
        self.bear.get.fish_from_river(river)
        self.assertEqual(1, self.bear.food_count())
        self.assertEqual(0, river.fish_count())

    # def test_take_fish(self):
    #     fish = Fish
    #     self.bear.take_fish(fish)
    #     self.assertEqual(1, len(self.river.holds_fish))