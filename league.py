import math
import random
from player import player as player
from deck import deck as deck
class match:

    def __init__(self, players, decks):
    
        self.players = players
        self.decks = decks
    
    def simulate(self):
        """
        Simulates the match with the given decks.
        Returns the winning deck and player.
        """

        total_power = sum([math.sqrt(p.power) for p in self.decks])
        win_probabilities = []
        for deck in self.decks:
            win_probabilities.append(math.sqrt(deck.power) / total_power)
        
        winner = random.choices(self.decks, weights=win_probabilities, k=1)[0]
        return(winner, winner.owner)
    

class league:

    def __init__(self, players, level_select_policy = "random", max_matches = 1000):
        """
        takes a list of players and decks and optional max_matches parameter to simulate a league.
        """
        self.players = players
        self.level_select_policy = level_select_policy
        self.max_matches = max_matches
        self.max_level = 10
        self.start_level = 7
        self.games_per_level = {}
        for i in  range(1, 11):
            self.games_per_level[i] = 0
        decks = []
        for p in players:
            decks = decks + p.decks
        for d in decks:
            d.league_level = self.start_level
        for p in players:
            p.level_count[self.start_level] = len(p.decks)
        #initialize the map and set all players to seven
        self.leaguelevel_map = {}
        for i in range(1, self.max_level + 1):
            self.leaguelevel_map[i] = set()
        self.leaguelevel_map[self.start_level] = set(players)

    def get_level_policy(self):

        """argument: some rule, returns a function that takes a league level and outputs the levels win/loss grants"""
        #policy = self.standard_level_policy
        policy = self.five_to_eight
        return policy
    def five_to_eight(self, leaguelevel):

        if(leaguelevel < 5 ):
            win_level = min(leaguelevel+3, 7)
            loss_level = max(1, leaguelevel-1)
        elif(leaguelevel == 6 or leaguelevel ==5):
            win_level = 8
            loss_level = leaguelevel-1
        else:
            win_level = min(self.max_level, leaguelevel+1)
            loss_level = max(1, leaguelevel-1)
        return win_level, loss_level
    def standard_level_policy(self, leaguelevel):

        if(leaguelevel < 7):
            win_level = min(leaguelevel+3, 7)
            loss_level = max(1, leaguelevel-1)
        else:
            win_level = min(self.max_level, leaguelevel+1)
            loss_level = max(1, leaguelevel-1)
        return win_level, loss_level
    
    def update_leaguelevels(self, leaguelevel, winning_deck, losing_decks, winning_player, losing_players):

        """
        implements the logic with how decks ascend/descend in level
        updates the map accordingly
        """
        self.games_per_level[leaguelevel] += 1
        #set new levels achieved by decks
        
        policy = self.get_level_policy()
        win_level, loss_level = policy(leaguelevel)



        #update each decks power
        winning_deck.league_level = win_level
        winning_deck.games_played += 1
        winning_deck.wins += 1
        for ld in losing_decks:
            ld.games_played += 1
            ld.league_level = loss_level

        #update the level map with the new levels reached
        #if a level 1 game is played, losers dont change
        if(leaguelevel != 1):
            for lp in losing_players:

                lp.level_count[loss_level] += 1
                self.leaguelevel_map[loss_level].add(lp)

                #delete from level that was just played incase no decks left
                lp.level_count[leaguelevel] -= 1
                if lp.level_count[leaguelevel] <= 0:
                    self.leaguelevel_map[leaguelevel].discard(lp)

        #same for winning player
        self.leaguelevel_map[win_level].add(winning_player)
        winning_player.level_count[win_level] += 1
        winning_player.level_count[leaguelevel] -= 1
        if winning_player.level_count[leaguelevel] <= 0:
                self.leaguelevel_map[leaguelevel].discard(winning_player)
    
    def step(self):
        """
        checks all valid leaguelevels, then randomly selects 4 players eglible to play a match of that level. 
        Then selects a valid deck for each player.
        """
        
        valid_levels = [level for level, ps in self.leaguelevel_map.items() if len(ps) >= 4]
        if(len(valid_levels) <= 0):
            return False
        
        #random possible leaguelevel, random set of players
        if self.level_select_policy == "random":
            print("using random")
            current_leaguelevel = random.choice(valid_levels)
        elif self.level_select_policy == "highest":
            print("using highest")
            current_leaguelevel = max(valid_levels)

        current_players = random.sample(self.leaguelevel_map[current_leaguelevel], 4)

        current_decks = []
        for p in current_players:
            posssible_decks = [d for d in p.decks if d.league_level == current_leaguelevel]
            if(len(posssible_decks) <= 0):
                print("ERROR")
            current_decks.append(random.choice(posssible_decks))

        #run simulation
        current_match = match(current_players, current_decks)
        win_deck, win_player = current_match.simulate()

        losers = current_players
        losers.remove(win_player)
        loser_decks = current_decks
        loser_decks.remove(win_deck)

        #update the levels according to league logic
        self.update_leaguelevels(current_leaguelevel, winning_deck = win_deck, 
                            losing_decks = loser_decks, winning_player = win_player, losing_players = losers)

        return True

    