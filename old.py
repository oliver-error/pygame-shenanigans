import pygame
import random
import sys

fullDeck = list(range(3, 36))
deck = fullDeck.copy()
currentCard = None
chipsInPot = 0
CARDSTOREMOVE = 9
currentBot = None
bots = {"bot0": {"name": "me", "chips": 0, "color": (0, 255, 0), "inventory": []},} # key: file path value: name, chips, color, inventory
botCount = len(bots.keys())
chipsPerPlayer = 0
botName = None
botChips = None
botInventory = None

def endGame():
    global bots
    scores = {}
    for bot in bots.keys:
        scores[bot] = []
        bot["inventory"].sort()
        lastCard = 0
        for card in bot["inventory"]:
            if not lastCard + 1 == card:
                scores[bot].append(card)
            lastCard = card
        scores[bot].append(-bot["chips"])

    for bot, score in scores.items():
        scores[bot] = sum(score)

    scores = dict(sorted(scores.items(), key=lambda item: item[1])) # this sorts the dict from highest scores to lowest
    i = 1
    for score in scores.keys():
        print(f"{i}. {score}, {bots[score]["name"]}")
        i += 1
    sys.exit()

def play(takeCard: bool, message: str = None):
    global currentBot, currentCard, chipsInPot
    if takeCard:
        currentBot["chips"] += chipsInPot
        currentBot["inventory"].append(currentCard)
        if not deck:
            endGame()     
        currentCard = deck.pop()
        chipsInPot = 0
        if message == None:
            print(f"{currentBot["name"]}: I'll take!")
        else:
            print(f"{currentBot["name"]}: {message}")
    else:
        if currentBot["chips"] == 0:
            print(f"currentBot {currentBot["name"]} tried to no thanks but had no chips")
            if not message == None:
                print(f"{currentBot["name"]}: {message}")
            currentBot["chips"] += chipsInPot
            currentBot["inventory"].append(currentCard)
        else:
            chipsInPot += 1
            currentBot["chips"] -= 1
            if message == None:
                print(f"{currentBot["name"]}: no thanks!")
            else:
                print(f"{currentBot["name"]}: {message}")



if botCount < 3:
    print("not enough players!")
    sys.exit()
elif botCount <= 5:
    chipsPerPlayer = 11
elif botCount == 6:
    chipsPerPlayer = 9
else:
    chipsPerPlayer = 7

for path, currentBot in bots.items():
    currentBot["chips"] = chipsPerPlayer
    exec(f"from {path} import run_turn as runBot{path[3:]}") 

deck = random.sample(deck, len(deck) - CARDSTOREMOVE) # remove 9 cards at random
removedCards = list(set(deck) ^ set(fullDeck))
for card in removedCards:
    print(f"removed card: {card}.")
random.shuffle(deck)

while True:
    currentCard = deck.pop(random.sample(deck))
    chipsInPot = 0

    for path in bots.keys():
        currentBot = bots[path]
        botName = currentBot["name"]
        botChips = currentBot["chips"]
        botInventory = currentBot["inventory"]
        exec(f"runBot{path[3:]}()")