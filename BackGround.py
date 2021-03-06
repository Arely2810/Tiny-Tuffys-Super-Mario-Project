import math
import random
import sys
import pygame
from pygame.locals import *
from MarioScoreBoard import ScoreBoard


# exit the program
def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


# define display surface
W, H = 500, 238
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("Scrolling Background with Player")
FPS = 500

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

bg = pygame.image.load("SuperMarioBrosMap.png").convert()
bgWidth, bgHeight = bg.get_rect().size

stageWidth = bgWidth * 2
stagePosX = 0

startScrollingPosX = HW

circleRadius = 10
circlePosX = circleRadius

playerPosX = circleRadius
playerPosY = 209
playerVelocityX = 0

sb = ScoreBoard(DS)

# main loop
while True:
    events()

    k = pygame.key.get_pressed()

    if k[K_RIGHT] and playerPosX != bgWidth - 300:
        playerVelocityX = 1
    elif k[K_LEFT]:
        playerVelocityX = -1
    else:
        playerVelocityX = 0

    playerPosX += playerVelocityX

    if playerPosX > stageWidth - circleRadius:
        playerPosX = stageWidth - circleRadius

    elif playerPosX < circleRadius:
        playerPosX = circleRadius

    elif playerPosX < startScrollingPosX:
        circlePosX = playerPosX

    elif playerPosX > stageWidth - startScrollingPosX:
        circlePosX = playerPosX - stageWidth + W
    else:
        circlePosX = startScrollingPosX
        playerPosX = startScrollingPosX
        if playerVelocityX > 0 and stagePosX + (bgWidth - W) > 0:
            stagePosX += -playerVelocityX

    DS.blit(bg, (stagePosX, 0))
    sb.update_screen()

    pygame.draw.circle(DS, WHITE, (int(circlePosX), playerPosY - 10), circleRadius, 0)

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)

