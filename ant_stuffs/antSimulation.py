import pygame
import random
import math
import time
import sys

# config 
nestPos = (0, 0)
foodPos = (0, 20)
worldHeight = 50
worldWidth = 50
strengthIncrement = 0.05 
antCount = 100
decayRate = 0.003 # range of 0.0 inclusive to 1.0 exclusive
explorationRate = 0.24 # range of 0.0 inclusive to 1.0 exclusive
maxSteps = 2000

# setup
pygame.init()
screen = pygame.display.set_mode((worldHeight * 15, worldWidth * 15))
pygame.display.set_caption("ant simulation")
screenWidth = screen.get_width()
screenHeight = screen.get_height()
ants = []
world = {} # trail format is [strength, isFood]
row = []
checkingPixel = [0, 0]
paths = None
stepCounter = 0
foodPickedUp = 0
foodDeposited = 0

# get starting values
world[(foodPos[0], foodPos[1])] = [[100000, True]]
world[(nestPos[0], nestPos[1])] = [[100000, False]]
for i in range(antCount):
    ants.append([nestPos[0], nestPos[1], 1, False, (0, 0)])

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

    if pathStrength > 0:
        transparency = max(0, min(255, int(pathStrength)))
    else:
        transparency = 255

    pixelSurface.fill((color[0], color[1], color[2], transparency))
    screen.blit(pixelSurface, ((position[0] + worldWidth / 2) * pixelSize[0], (position[1] + worldHeight / 2) * pixelSize[1]))


# main simulation loop
while stepCounter <= maxSteps:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    for ant in ants:
        xPosition = ant[0]
        yPosition = ant[1]
        direction = ant[2]
        hasFood = ant[3]
        lastPos = ant[4]

        currentPos = (xPosition, yPosition)

        # direction -> forward and right values
        if direction == 1:
            forward = (0, 1)
            right = (1, 0)
        elif direction == 3:
            forward = (0, -1)
            right = (-1, 0)
        elif direction == 2:
            forward = (1, 0)
            right = (0, -1)
        elif direction == 4:
            forward = (-1, 0)
            right = (0, 1)

        # checking surrounding tiles logic
        paths = {}

        directions = [
            forward,
            right,
            (-right[0], -right[1])
        ]

        for dx, dy in directions:
            checkPos = (xPosition + dx, yPosition + dy)

            if checkPos == lastPos:
                continue

            pixel = world.get(checkPos, [])

            for path in pixel:
                if path[1] != hasFood:
                    paths[checkPos] = path[0]

        sumPos = [0, 0]

        lastPos = currentPos

        if paths and random.random() >= explorationRate:
            chosenPos = random.choices(list(paths.keys()), weights=list(paths.values()), k=1)[0]

            sumPos = [
                chosenPos[0] - xPosition,
                chosenPos[1] - yPosition
            ]

            if sumPos == [0, 1]:
                direction = 1
            elif sumPos == [1, 0]:
                direction = 2
            elif sumPos == [0, -1]:
                direction = 3
            elif sumPos == [-1, 0]:
                direction = 4
        else:
            # randomly move if there are no paths avalible
            if random.randint(1, 5) > 2:
                # go forward
                sumPos[0] += forward[0]
                sumPos[1] += forward[1]
            elif random.randint(1, 2) == 1:
                # go right
                sumPos[0] += right[0]
                sumPos[1] += right[1]
                direction += 1
            else:
                # go left
                sumPos[0] += right[0] * -1
                sumPos[1] += right[1] * -1
                direction -= 1

            # wrapping logic
            if direction == 0:
                direction = 4
            if direction == 5:
                direction = 1

        xPosition += sumPos[0]
        yPosition += sumPos[1]

        if abs(xPosition) > worldWidth:
            xPosition = worldWidth * math.copysign(1, xPosition)

        if abs(yPosition) > worldHeight:
            yPosition = worldHeight * math.copysign(1, yPosition)

        currentPos = (xPosition, yPosition)

        # food check
        if currentPos == foodPos:
            hasFood = True
            foodPickedUp += 1
        elif currentPos == nestPos:
            hasFood = False
            foodDeposited += 1

        # path creation / strengthing
        pixel = world.setdefault(currentPos, [])

        pathIndex = -1

        for i, path in enumerate(pixel):
            if path[1] == hasFood:
                pathIndex = i
                break

        if pathIndex == -1:
            pixel.append([strengthIncrement, hasFood])
        else:
            if pixel[pathIndex][0] < 1.0:
                pixel[pathIndex][0] += strengthIncrement

        ant[0] = xPosition
        ant[1] = yPosition
        ant[2] = direction
        ant[3] = hasFood
        ant[4] = lastPos


    # path decay and removal
    for position, pixel in list(world.items()):
        if position == foodPos or position == nestPos:
            continue
        
        for path in pixel[:]:
            path[0] *= (1 - decayRate)

            if path[0] < decayRate / 10:
                pixel.remove(path)

        if not pixel:
            del world[position]

    # render screen
    screen.fill((100, 100, 100))
    for position, pixel in world.items():
        for trail in pixel:
            if trail[1]:
                renderPixel(position, (255, 0, 0), abs(trail[0]) * 600)
            else:
                renderPixel(position, (0, 0, 255), abs(trail[0]) * 600)

    for ant in ants:
        renderPixel((ant[0], ant[1]), (0, 0, 0))

    renderPixel(foodPos, (0, 255, 0))
    renderPixel(nestPos, (255, 255, 0))

    pygame.display.flip()

    stepCounter += 1
    #time.sleep(0.01)

print(f"food picked up: {foodPickedUp}")
print(f"food deposited: {foodDeposited}")