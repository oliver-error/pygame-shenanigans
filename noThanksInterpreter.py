import pygame
import random
import sys
import time
import math
random.seed(hash("not the final password" + str(time.time_ns())))
pygame.init()

fullDeck = list(range(3, 36))
deck = fullDeck.copy()
currentCard = None
chipsInPot = 0
CARDS_TO_REMOVE = 9
currentBot = None
bots = {"bot0": {"name": "bot 1", "chips": 0, "color": (0, 255, 0), "inventory": []}, 
        "bot1": {"name": "bot 2", "chips": 0, "color": (255, 0, 0), "inventory": []}} # key: file path value: name, chips, color, inventory
botCount = len(bots.keys())
chipsPerPlayer = 0
botName = None
botChips = None
botInventory = None
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screenRect = screen.get_rect()
cardPositions = [
    # this entire thing is just the midpoint formula OVER AND OVER AGAIN
    # top row
    ((screenRect.midleft[0] + screenRect.center[0]) / 2, (screenRect.midtop[1] + screenRect.center[1]) / 2), 
    (screenRect.center[0], (screenRect.midtop[1] + screenRect.center[1]) / 2), 
    ((screenRect.midright[0] + screenRect.center[0]) / 2, (screenRect.midtop[1] + screenRect.center[1]) / 2), 
    
    # middle row
    ((screenRect.midleft[0] + screenRect.center[0]) / 2, screenRect.center[1]), 
    screenRect.center, 
    ((screenRect.midright[0] + screenRect.center[0]) / 2, screenRect.center[1]),
    
    # bottom row
    ((screenRect.midleft[0] + screenRect.center[0]) / 2, (screenRect.midbottom[1] + screenRect.center[1]) / 2), 
    (screenRect.center[0], (screenRect.midbottom[1] + screenRect.center[1]) / 2), 
    ((screenRect.midright[0] + screenRect.center[0]) / 2, (screenRect.midbottom[1] + screenRect.center[1]) / 2)
]
cardColors = {
    3: (158, 27, 27), 4: (158, 27, 27), 5: (158, 27, 27), 6: (158, 27, 27), 7: (158, 27, 27),
    8: (230, 92, 0), 9: (230, 92, 0), 10: (230, 92, 0), 11: (230, 92, 0),
    12: (230, 184, 0), 13: (230, 184, 0), 14: (230, 184, 0), 15: (230, 184, 0),
    16: (46, 139, 87), 17: (46, 139, 87), 18: (46, 139, 87), 19: (46, 139, 87), 20: (46, 139, 87),
    21: (0, 139, 139), 22: (0, 139, 139), 23: (0, 139, 139), 24: (0, 139, 139), 25: (0, 139, 139),
    26: (31, 69, 252), 27: (31, 69, 252), 28: (31, 69, 252), 29: (31, 69, 252),
    30: (106, 13, 145), 31: (106, 13, 145), 32: (106, 13, 145),
    33: (162, 0, 109), 34: (162, 0, 109), 35: (162, 0, 109)
}



pygame.display.set_caption("No thanks!")

def play(takeCard: bool, message: str = None):
    global currentBot, currentCard, chipsInPot, deck
    if takeCard:
        currentBot["chips"] += chipsInPot
        currentBot["inventory"].append(currentCard)
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
            currentCard = deck.pop()
            chipsInPot = 0
        else:
            chipsInPot += 1
            currentBot["chips"] -= 1
            if message == None:
                print(f"{currentBot["name"]}: no thanks!")
            else:
                print(f"{currentBot["name"]}: {message}")



def rotAround0(x,y,radians):
    X = x * math.cos(radians) - y * math.sin(radians)
    Y = x * math.sin(radians) + y * math.cos(radians)
    return X, Y

def renderGame(screen):
    global bots, botCount, currentBot, screenRect
    screen.fill((230, 230, 230))
    startingX = screenRect.center[0]
    startingY = screenRect.center[1]
    pygame.draw.circle(screen, (111, 77, 43), screenRect.center, 200)
    degreesPerBot = 360 / botCount
    botToIndex = []
    i = 0
    for bot in bots.values():
        # get current bots position
        radians = math.radians(i * degreesPerBot)
        finalX = startingX + 360 * math.cos(radians)
        finalY = startingY + 360 * math.sin(radians)
        pygame.draw.circle(screen, bot["color"], (finalX, finalY), 100)

        # create name
        font = pygame.font.Font(None, 35 - (len(bot["name"]) - 15))
        textSurface = font.render(bot["name"], True, (0, 0, 0))
        textRect = textSurface.get_rect()
        textRect.center = (finalX, finalY)
        screen.blit(textSurface, textRect)
        botToIndex.append(bot)
        i += 1

    turnMarkerRadius = 500

    radians = math.radians(botToIndex.index(currentBot) * degreesPerBot)
    
    # far right
    startingX, startingY = rotAround0(20, 20,radians)
    finalX1 = startingX + screenRect.center[0] + (turnMarkerRadius * math.cos(radians))
    finalY1 = startingY + screenRect.center[1] + (turnMarkerRadius * math.sin(radians))

    # far left
    startingX, startingY = rotAround0(20, -20,radians)
    finalX2 = startingX + screenRect.center[0] + (turnMarkerRadius * math.cos(radians))
    finalY2 = startingY + screenRect.center[1] + (turnMarkerRadius * math.sin(radians))

    # center
    startingX = screenRect.center[0]
    startingY = screenRect.center[1]
    finalX3 = startingX + (turnMarkerRadius * math.cos(radians))
    finalY3 = startingY + (turnMarkerRadius * math.sin(radians))

    pygame.draw.polygon(screen, (255, 0, 0), ((finalX1, finalY1), (finalX2, finalY2), (finalX3, finalY3)), width=0)


def renderCard(screen, position: tuple = screen.get_rect().center, cardNumber: int = 0, scale: float = 1):
    """render the specified card"""
    global cardColors
    cardBaseRect = pygame.Rect(position[0], position[1], scale * 2.5, scale * 3.5)
    trimmingRect = pygame.Rect(position[0], position[1], scale * 2, scale * 3)
    centerRect = pygame.Rect(position[0], position[1], scale * 1.5, scale * 2.5)
    cardBaseRect.center = position
    trimmingRect.center = position
    centerRect.center = position

    font = pygame.font.Font(None, int(scale * 1.8)) #mult will also have to apply here
    middleTextSurface = font.render(str(cardNumber), True, cardColors[cardNumber])
    middleNumberRect = middleTextSurface.get_rect()
    middleNumberRect.center = cardBaseRect.center

    pygame.draw.rect(screen, (255, 255, 255), cardBaseRect)
    pygame.draw.rect(screen, cardColors[cardNumber], trimmingRect)
    pygame.draw.rect(screen, (255, 255, 255), centerRect)
    screen.blit(middleTextSurface, middleNumberRect)
    


if botCount < 3:
    print("not enough players!")
    #sys.exit()
elif botCount <= 5:
    chipsPerPlayer = 11
elif botCount == 6:
    chipsPerPlayer = 9
else:
    chipsPerPlayer = 7

for path, currentBot in bots.items():
    currentBot["chips"] = chipsPerPlayer
    #exec(f"from {path} import run_turn as runBot{path[3:]}") 

deck = random.sample(deck, len(deck) - CARDS_TO_REMOVE) # remove 9 cards at random
removedCards = list(set(deck) ^ set(fullDeck))

screen.fill((230, 230, 230))
# make removed card text
font = pygame.font.Font(None, 90)
textSurface = font.render("removed cards:", True, (0, 0, 0))
textRect = textSurface.get_rect()
textRect.center = (screenRect.midtop[0], screenRect.midtop[1] + 75)
screen.blit(textSurface, textRect)
i = 0
for card in removedCards:
    # render all removed cards
    renderCard(screen, cardPositions[i], card, 50)
    i += 1
    
pygame.display.flip()
time.sleep(5)

random.shuffle(deck)

currentCard = deck.pop()
chipsInPot = 0
while True:
    for path in bots.keys():
        currentBot = bots[path]
        botName = currentBot["name"]
        botChips = currentBot["chips"]
        botInventory = currentBot["inventory"]
        #exec(f"runBot{path[3:]}()") 
        renderGame(screen)
        renderCard(screen, cardNumber=currentCard, scale=45)
        pygame.display.flip()
        time.sleep(0.1)
        loop = True
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                    loop = False
            time.sleep(0.1)
                
