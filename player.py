class player:

    def __init__(self, name):
        self.name = name
        self.level_count = {}

        for i in range(1, 11):
            self.level_count[i] = 0
        self.decks = []

    def set_decks(self,decks):
        self.decks = decks
    def get_decks(self):
        return self.decks