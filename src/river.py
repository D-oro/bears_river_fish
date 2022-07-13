class River:
    def __init__(self, name):
        self.name = name
        self.holds_fish = []

    def fish_count(self):
        return len(self.holds_fish)