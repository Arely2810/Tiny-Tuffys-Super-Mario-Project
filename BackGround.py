import math
import random
import sys
import pygame
from pygame.locals import *
from enemy import Goomba
from pygame.sprite import Group
from mario import Mario
from settings_arely import Settings
import game_functions_arely as gf


# exit the program
def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


# define display surface
W, H = 1000, 480
HW, HH = W / 2, H / 2
AREA = W * H
settings = Settings()
screen = pygame.display.set_mode(settings.dims())
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

# goomba1 = Goomba(DS, (500, 400), 1)
# allSprite = Group()
# allSprite.add(goomba1)
mario = Mario(settings, screen)
fireballs = Group()
# just a temp variable
ground = Group()

# main loop
while True:
    events()

    k = pygame.key.get_pressed()

    # if k[K_RIGHT] and playerPosX != bgWidth - 300:
    #     playerVelocityX = 1
    # elif k[K_LEFT]:
    #     playerVelocityX = -1
    # else:
    #     playerVelocityX = 0

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

    # rel_x = stagePosX % bgWidth
    DS.blit(bg, (stagePosX, 0))

    # for enemyy in allSprite:
    #     if playerVelocityX > 0 and circlePosX == startScrollingPosX:
    #         enemyy.enemy_rect.x -= playerVelocityX
    #     elif playerVelocityX < 0 and circlePosX == startScrollingPosX:
    #         enemyy.enemy_rect.x -= playerVelocityX
    # allSprite.update()

    pygame.draw.circle(DS, WHITE, (int(circlePosX), playerPosY - 10), circleRadius, 0)
    gf.mario_move(mario, settings, screen, fireballs)

    if mario.death == False:
        mario.update()
        # mario.blitme()

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)