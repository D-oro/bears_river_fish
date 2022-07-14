class River:
    def __init__(self, name, fishes):
        self.name = name
        self.fishes = fishes

    def fish_count(self):
        return len(self.fishes)

    def give_fish(self):
        return self.fishes.pop()