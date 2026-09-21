import pygame
import random

fullDeck = []
deck = []
currentCard = None
chipsInPot = 0
CARDSTOREMOVE = 9
bots = {"bot0": {"name": "me", "chips": 0, "color": (0, 255, 0)},} # key: file path value: name, chips, color

for path in bots.keys():
    exec(f"from {path} import run_turn as runBot{path[3:]}") 

for card in range(3, 36):
    fullDeck.append(card)

deck = fullDeck.copy()
deck = random.sample(deck, len(deck) - CARDSTOREMOVE) # remove 9 cards at random
removedCards = list(set(deck) ^ set(fullDeck))
for card in removedCards:
    print(f"removed card: {card}.")
random.shuffle(deck)

