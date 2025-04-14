import league as L
import math
import random
from player import player as player
from deck import deck as deck

names = ["Nic", "Gisi", "Robin", "Pesche", "Gabs", "Nicole", "Swe", "Clemy"]

commanders = [
    "Atraxa, Praetors' Voice",
    "Narset, Enlightened Exile",
    "Edgar Markov",
    "Krenko, Mob Boss",
    "Meren of Clan Nel Toth",
    "Shattergang Brothers",
    "Nicol Bolas, the Ravager",
    "Omnath, Locus of Creation",
    "Teysa, Envoy of Ghosts",
    "Yuriko, the Tiger's Shadow",
    "Azami, Lady of Scrolls",
    "Chulane, Teller of Tales",
    "Lazav, Dimir Mastermind",
    "Thrasios, Triton Hero",
    "Aurelia, the Warleader",
    "Prossh, Skyraider of Kher",
    "Golos, Tireless Pilgrim",
    "Vorel of the Hull Clade",
    "Karn, Silver Golem",
    "Rafiq of the Many",
    "Jhoira of the Ghitu",
    "Niv-Mizzet, the Firemind",
    "Syr Faren, the Hengehammer",
    "Kaalia of the Vast",
    "Muldrotha, the Gravetide",
    "Vraska, Golgari Queen",
    "Karn, the Great Creator",
    "Samut, Tyrant Smasher",
    "Teysa, the Seer",
    "Muzzio, Visionary Architect",
    "Llanowar Elves",
    "Mikaeus, the Unhallowed",
    "Bastion of Remembrance",
    "Karn, Living Legacy",
    "Chandra, Awakened Inferno",
    "Liliana, Dreadhorde General",
    "Cisse, Weatherlight Captain",
    "Yidris, Maelstrom Wielder",
    "Tymna the Weaver",
    "Meren of Clan Nel Toth",
    "Narset, the Ancient Way",
    "Atla Palani, Nest Tender",
    "Roon of the Hidden Realm",
    "Horde of Notions",
    "Xenagos, the Reveler",
    "Sigarda, Host of Herons",
    "Alesha, Who Smiles at Death",
    "Jeskai Ascendancy",
    "Sigarda, Host of Herons",
    "Kenrith, the Returned King",
    "Niv-Mizzet, Parun",
    "Hidetsugu, Devouring Chaos",
    "Omnath, Locus of Rage",
    "Yidris, Maelstrom Wielder",
    "Ashling the Pilgrim",
    "Animar, Soul of Elements",
    "Narset, Enlightened Exile",
    "Arahbo, Roar of the World",
    "Riku of Two Reflections",
    "Teysa, Envoy of Ghosts",
    "Aragorn",
    "Zada, Hedrigal",
    "Kaalia of the Vast",
    "Brago, King Eternal",
    "Sorin, Imperious Bloodlord",
    "Garruk, Wildspeaker",
    "Shalai, Voice of Plenty",
    "Muldrotha, the Gravetide",
    "Sidisi, Brood Tyrant",
    "Jace, Vryn's Prodigy",
    "Teysa, Envoy of Ghosts",
    "Zur the Enchanter",
    "Karn, the Great Creator",
    "Harmonize",
    "Teysa, Envoy of Ghosts",
    "gary",
    "loller",
    "moxy",
    "trump",
    "elon"
]

decks = []
players = []
commanders = commanders[0:80]
for cmdr in commanders:
    decks.append(deck(commander = cmdr, power =random.randint(1, 4)))
for name in names:
    players.append(player(name))

players=players[0:6]


num_players = len(players)
random.shuffle(decks)

for i in range(len(decks)):
    pl = players[i%num_players]
    pl.decks.append(decks[i])
    decks[i].owner = pl

    """
    if(pl.name == "Robin" or pl.name == "Pesche"):
        decks[i].power += random.randint(1,4)
    if(pl.name == "Nic"):
        decks[i].power = max(1, decks[i].power - random.randint(1,4))
    """
league = L.league(players)

stepnr = 0
while(league.step()):
    print(stepnr)
    stepnr += 1

print("done")




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
    print(str(d.commander) + " winrate is:" + str(d.get_winrate()))

for p in players:
    average_winrate = 0
    for d in p.decks:
        average_winrate += d.get_winrate()
    
    average_winrate = average_winrate / len(p.decks)

    print(p.name + "   has a winrate of " + str(average_winrate))
# Show the plot
plt.show()

