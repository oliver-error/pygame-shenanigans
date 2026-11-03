import pygame
import random
import math
import time

# config 
nestPos = (0, 0)
foodPos = (10, 0)
worldHeight = 50
worldWidth = 50
strengthIncrement = 0.05
antCount = 100
decayRate = 0.1 # range of 0.0 inclusive to 1.0 exclusive
explorationRate = 0.2 # range of 0.0 inclusive to 1.0 exclusive
maxSteps = 1000

# setup
pygame.init()
screen = pygame.display.set_mode((worldHeight * 15, worldWidth * 15))
pygame.display.set_caption("ant simulation")
screenWidth = screen.width
screenHeight = screen.height
ants = []
world = {} # trail format is [strength, isFood]
row = []
checkingPixel = [0, 0]
paths = None
stepCounter = 0

# get starting values
world[(foodPos[0], foodPos[1])] = [100000, True] 
world[(nestPos[0], nestPos[1])] = [100000, False]
ants = [nestPos[0], nestPos[1], 1, False] * antCount

# clamp values
nestPos = (round(nestPos[0]), round(nestPos[1]))
foodPos = (round(foodPos[0]), round(foodPos[1]))

if decayRate < 0.0:
    decayRate = 0.0
elif decayRate > 1.0:
    decayRate = 1.0

if explorationRate < 0:
    explorationRate = 0.0
elif explorationRate >= 1:
    explorationRate = 0.9

def renderPixel(position: tuple, color: tuple, pathStrength: float = 0):
    global screen
    if screenWidth < screenHeight:
        pixelSize = (screenWidth / worldWidth, screenWidth / worldWidth)
    else:
        pixelSize = (screenHeight / worldHeight, screenHeight / worldHeight)
    pixelSurface = pygame.Surface(pixelSize, pygame.SRCALPHA) 
    trasparency = 255
    if pathStrength:
        trasparency = 255 / (pathStrength * 10)
    pixelSurface.fill((color[0], color[1], color[2], trasparency))
    screen.blit(pixelSurface, ((position[0] + worldWidth / 2) * pixelSize[0], (position[1] + worldHeight / 2) * pixelSize[1]))

screen.fill((100, 100, 100))
renderPixel((0, 0), (255, 0, 0))
pygame.display.flip()
while True:
    time.sleep(1)