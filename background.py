import math
import random
import sys
import pygame
from pygame.locals import *
from enemy import *
from pygame.sprite import Group


# exit the program
def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


# define display surface
W, H = 1000, 480  #EDITED
HW, HH = W // 2, H // 2  # EDITED
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

# stageWidth = bgWidth * 2
stageWidth = bgWidth
stagePosX = 0

startScrollingPosX = HW

circleRadius = 10
circlePosX = circleRadius

playerPosX = circleRadius
playerPosY = 209
playerVelocityX = 0

goomba1 = Goomba(DS, (500, 385), 1)
greenkoopa1 = KoopaTroopa(DS, (1500, 380), 1)
redkoopa1 = KoopaTroopa(DS, (850, 380), 2, 800, 1100)
plant1 = PiranhaPlant(DS, (1100, 380), 2, 350, 390)
flyingred1 = KoopaParatroopa(DS, (1100, 200), 2, 180, 250)
blooper1 = Blooper(DS, (2000, 200))
cheep1 = CheepCheep(DS, (2100, 300), 1)
cheep2 = CheepCheep(DS, (2100, 350), 2)
po1 = Podoboo(DS, (2225, 480), 300, 500)
fire1 = FireBar(DS, (300, 200), 0)
fire2 = FireBar(DS, (300, 200), 15)
fire3 = FireBar(DS, (300, 200), 30)
fire4 = FireBar(DS, (300, 200), 45)
fire5 = FireBar(DS, (300, 200), 60)
fire6 = FireBar(DS, (300, 200), 75)

no_pathx_sprites = Group()
pathx_sprites = Group()

pathx_sprites.add(redkoopa1)

no_pathx_sprites.add(goomba1)
no_pathx_sprites.add(greenkoopa1)
no_pathx_sprites.add(plant1)
no_pathx_sprites.add(flyingred1)
no_pathx_sprites.add(blooper1)
no_pathx_sprites.add(cheep1)
no_pathx_sprites.add(cheep2)
no_pathx_sprites.add(po1)
no_pathx_sprites.add(fire1)
no_pathx_sprites.add(fire2)
no_pathx_sprites.add(fire3)
no_pathx_sprites.add(fire4)
no_pathx_sprites.add(fire5)
no_pathx_sprites.add(fire6)

# main loop
while True:
    events()

    k = pygame.key.get_pressed()

    if k[K_RIGHT] and playerPosX != bgWidth - 300:
        playerVelocityX = 10  # was 1
    elif k[K_LEFT]:
        playerVelocityX = -10  # was -1
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

    # rel_x = stagePosX % bgWidth
    DS.blit(bg, (stagePosX, 0))

    for enemyy in no_pathx_sprites:
        if playerVelocityX > 0 and circlePosX == startScrollingPosX:
            enemyy.enemy_rect.x -= playerVelocityX
        # elif playerVelocityX < 0 and circlePosX == startScrollingPosX:
        #     enemyy.enemy_rect.x -= playerVelocityX

    for enemyy in pathx_sprites:
        if playerVelocityX > 0 and circlePosX == startScrollingPosX:
            enemyy.enemy_rect.x -= playerVelocityX
            enemyy.path_left -= playerVelocityX
            enemyy.path_right -= playerVelocityX
        # elif playerVelocityX < 0 and circlePosX == startScrollingPosX:
        #     enemyy.enemy_rect.x -= playerVelocityX
        #     enemyy.path_left -= playerVelocityX
        #     enemyy.path_right -= playerVelocityX

    no_pathx_sprites.update()
    pathx_sprites.update()

    pygame.draw.circle(DS, WHITE, (circlePosX, playerPosY - 10), circleRadius, 0)
    pygame.draw.circle(DS, (0, 0, 255), (playerPosX, playerPosY - 50), circleRadius, 0)

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
