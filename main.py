import league as L
import math
import string
import random
from player import player as player
from deck import deck as deck
import engine
import data_utils
import argparse
import numpy as np

parser = argparse.ArgumentParser(description="Configure the amount of players and decks in the league")
parser.add_argument("--players", type=int,default = 8, help="number of players")
parser.add_argument("--decks", type=int, default=160, help="number of decks")
parser.add_argument("--leaguerounds", type=int, default = 10000, help="number of simulated rounds")
parser.add_argument("--simulationrounds", type=int, default = 50)
parser.add_argument("--policy", type=str, default="random")
args = parser.parse_args()
counts = []
games_per_level = []
for i in range(args.simulationrounds): 
    decks = engine.generate_decks(args.decks)
    players = engine.generate_players(args.players)
    engine.distribute_decks(decks, players)



    league = L.league(players, level_select_policy=args.policy)

    stepnr = 0

    while(league.step() and stepnr < args.leaguerounds):
        
        stepnr += 1

    playerwins = 0
    for p in league.players:
        for d in p.get_decks():
            playerwins += d.wins



    level_count = {}
    for i in range(1, 11):
        level_count[i] = 0
    for d in decks:
        level_count[d.league_level] += 1
    counts.append(level_count)
    games_per_level.append(league.games_per_level)


stor = data_utils.create_store_dir()
print(stor)
for i in range(args.simulationrounds):

    data_utils.store_level_distribution(stor, counts[i], games_per_level[i], i)



