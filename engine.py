import league as L
import math
import string
import random
from player import player as player
from deck import deck as deck
from typing import List




def generate_decks(nr_of_decks: int) -> List[deck]:
    
    def generate_random_cmdr(n : int) -> List[str]:
        commanders = []

        for i in range(n):
            chars = string.ascii_letters
            commanders.append(''.join(random.choices(chars, k=12)))
        return commanders
    
    commanders = generate_random_cmdr(nr_of_decks)

    decks = []
    for cmdr in commanders:
        decks.append(deck(commander = cmdr, power =random.randint(1, 4)))
    return decks

def generate_players(nr_of_players: int) -> List[player]:

    names = ["Nic", "Gisi", "Robin", "Pesche", "Gabs", "Nicole", "Swe", "Clemy"]
    assert(nr_of_players <= len(names), "more players than available")
    players = [] 
    for i in range(nr_of_players):
        players.append(player(names[i]))
    return players

def distribute_decks(decks, players):

    num_players = len(players)
    for i in range(len(decks)):
        pl = players[i%num_players]
        pl.decks.append(decks[i])
        decks[i].owner = pl




