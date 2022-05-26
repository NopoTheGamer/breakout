import random

import pygame
import enum


class dir(enum.Enum):
    down = 0
    up = 1
    left = 2
    right = 3
    upLeft = 4
    upRight = 5
    downLeft = 6
    downRight = 7


pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("balls")
lunar = pygame.image.load("assets/lunar.png")
lunar = pygame.transform.scale(lunar, (112, 64))
lunarWidth = lunar.get_width()
lunarHeight = lunar.get_height()
balls = pygame.image.load("assets/balls.png")
balls = pygame.transform.scale(balls, (64, 64))

ballDir = dir.down
ballXCoords = 400
ballYCoords = 60
speed = 4


def isGoingUp(dir):
    if dir == dir.upLeft or dir == dir.upRight or dir == dir.up:
        return True
    else:
        return False


def isGoingDown(dir):
    if dir == dir.down or dir == dir.downLeft or dir == dir.downRight:
        return True
    else:
        return False


def isGoingRight(dir):
    if dir == dir.right or dir == dir.downRight or dir == dir.upRight:
        return True
    else:
        return False


def isGoingLeft(dir):
    if dir == dir.left or dir == dir.downLeft or dir == dir.upLeft:
        return True
    else:
        return False


def walls(coords):
    coordsList = list(coords)
    if coordsList[0] < 5:
        coordsList[0] = 4
        if isGoingUp(coordsList[2]):
            coordsList[2] = dir.upRight
        elif isGoingDown(coordsList[2]):
            coordsList[2] = dir.downRight
        else:
            if random.randint(0, 1) == 0:
                coordsList[2] = dir.upRight
            else:
                coordsList[2] = dir.downRight
    if coordsList[0] > 735:
        coordsList[0] = 736
        if isGoingUp(coordsList[2]):
            coordsList[2] = dir.upLeft
        elif isGoingDown(coordsList[2]):
            coordsList[2] = dir.downLeft
        else:
            if random.randint(0, 1) == 0:
                coordsList[2] = dir.upLeft
            else:
                coordsList[2] = dir.downLeft
    if coordsList[1] < 5:
        coordsList[1] = 4
        if isGoingUp(coordsList[2]):
            if isGoingRight(coordsList[2]):
                coordsList[2] = dir.downRight
            elif isGoingLeft(coordsList[2]):
                coordsList[2] = dir.downLeft
            else:
                if random.randint(0, 1) == 0:
                    coordsList[2] = dir.downLeft
                else:
                    coordsList[2] = dir.downRighta
    if coordsList[1] > 535:
        coordsList[1] = 536
        print("you suck (nuts)")
        pygame.quit()
    if coordsList[2] == dir.down:
        coordsList[1] += speed
    if coordsList[2] == dir.up:
        coordsList[1] -= speed
    if coordsList[2] == dir.left:
        coordsList[0] -= speed
    if coordsList[2] == dir.right:
        coordsList[0] += speed

    if coordsList[2] == dir.downLeft:
        coordsList[1] += speed
        coordsList[0] -= speed
    if coordsList[2] == dir.upLeft:
        coordsList[1] -= speed
        coordsList[0] -= speed
    if coordsList[2] == dir.downRight:
        coordsList[0] += speed
        coordsList[1] += speed
    if coordsList[2] == dir.upRight:
        coordsList[0] += speed
        coordsList[1] -= speed

    return coordsList


xCoords = 0
yCoords = 500

clock = pygame.time.Clock()
game_over = False
mouse = pygame.mouse.get_pos()
mouseOld = pygame.mouse.get_pos()

while not game_over:
    dt = clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                ballDir = dir.left
            if event.key == pygame.K_d:
                ballDir = dir.right
            if event.key == pygame.K_w:
                ballDir = dir.up
            if event.key == pygame.K_s:
                ballDir = dir.down
                # if event.key == pygame.K_w:
            #     yCoords -= 50
            # if event.key == pygame.K_s:
            #     yCoords += 50Vj

    if mouse != mouseOld:
        xCoords = mouse[0] - int(lunarWidth / 2)
        mouseOld = mouse
    if xCoords < 0:
        xCoords = 0
    if xCoords > 700:
        xCoords = 700
    ballXCoords = walls((ballXCoords, ballYCoords, ballDir))[0]
    ballYCoords = walls((ballXCoords, ballYCoords, ballDir))[1]
    ballDir = walls((ballXCoords, ballYCoords, ballDir))[2]
    speed = random.randint(3, 7)
    if ballXCoords - lunarWidth < xCoords < (
            ballXCoords + balls.get_width()) and yCoords - 64 < ballYCoords < yCoords + 128:
        if random.randint(0, 1) == 0:
            ballDir = dir.upLeft
        else:
            ballDir = dir.upRight

    screen.blit(lunar, (xCoords, yCoords))
    screen.blit(balls, (ballXCoords, ballYCoords))
    print(f"x: {ballXCoords} y: {ballYCoords}")
    pygame.display.update()

pygame.quit()
