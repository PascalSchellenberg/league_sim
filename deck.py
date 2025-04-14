import math

class deck:
    def __init__(self, commander, power, league_level = 7):
        self.power = power
        self.commander = commander
        self.owner = ""
        self.games_played = 0
        self.wins = 0
        self.league_level = 7

    def get_winrate(self):
        if self.games_played == 0:
            return 0
        else:
            return self.wins/ self.games_played

