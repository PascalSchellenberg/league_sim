import league as L
import math
import string
import random
from player import player as player
from deck import deck as deck
import engine
import argparse


parser = argparse.ArgumentParser(description="Configure the amount of players and decks in the league")
parser.add_argument("--players", type=int,default = 8, help="number of players")
parser.add_argument("--decks", type=int, default=160, help="number of decks")
parser.add_argument("--rounds", type=int, default = 10000, help="number of simulated rounds")
args = parser.parse_args()
decks = engine.generate_decks(args.decks)
players = engine.generate_players(args.players)
engine.distribute_decks(decks, players)



league = L.league(players, level_select_policy="highest")

stepnr = 0

while(league.step() and stepnr < args.rounds):
    
    stepnr += 1

playerwins = 0
for p in league.players:
    for d in p.get_decks():
        playerwins += d.wins

assert(playerwins == stepnr + 1, "total wins not equal to total games!")





import numpy as np

level_count = {}
for i in range(1, 20):
    level_count[i] = 0
for d in decks:
    level_count[d.league_level] += 1

import matplotlib.pyplot as plt


# Extract keys (levels) and values (counts)
levels = list(level_count.keys())
counts = list(level_count.values())

# Create the bar plot
plt.figure(figsize=(10, 6))
plt.bar(levels, counts, color='skyblue')

# Add labels and title
plt.xlabel('Level')
plt.ylabel('Count')
plt.title('Level Counts Visualization')

for d in decks:
    #print(str(d.commander) + " winrate is:" + str(d.get_winrate()))
    True

for p in players:
    average_winrate = 0
    for d in p.decks:
        average_winrate += d.get_winrate()
    
    average_winrate = average_winrate / len(p.decks)

    #print(p.name + "   has a winrate of " + str(average_winrate))


for k,v in league.games_per_level.items():
    #print("at level " + str(k) + " there was " + str(v) + " games played")
    True

# Show the plot
plt.show()

