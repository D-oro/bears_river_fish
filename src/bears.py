class Bear:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.stomach = []

    def eat_fish(self, fish):
        self.stomach.append(fish)

    def food_count(self):
        return len(self.stomach)

    def get_fish_from_river(self, river):
        fish = river.give_fish()
        self.eat_fish(fish)

    # def take_fish(self, fish):
    #     self.river.holds_fish.remove(fish)