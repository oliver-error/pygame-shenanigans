import pygame
import random

fullDeck = []
deck = []
currentCard = None

cardsToRemove = 9

for card in range(3, 36):
    fullDeck.append(card)

deck = fullDeck.copy()
deck = random.sample(deck, len(deck) - cardsToRemove) # remove 9 cards at random
removedCards = list(set(deck) ^ set(fullDeck))
for card in removedCards:
    print(f"removed card: {card}.")
random.shuffle(deck)