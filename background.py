import math
import random
import sys
import pygame
from pygame.locals import *
from enemy import *
from pygame.sprite import Group
# from mario import Mario
from temp_mario import TempMario
import temp_game_functions as gf


# exit the program
# def events():
    # for event in pygame.event.get():
    #     if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
    #         pygame.quit()
    #         sys.exit()
    #
    #     if event.type == KEYDOWN:
    #         if event.key == K_LEFT:
    #             moveRight = False
    #             moveLeft = True
    #         if event.key == K_RIGHT:
    #             moveLeft = False
    #             moveRight = True
    #         if event.key == K_UP:
    #             moveDown = False
    #             moveUp = True
    #         if event.key == K_DOWN:
    #             moveUp = False
    #             moveDown = True
    #     if event.type == KEYUP:
    #         if event.key == K_ESCAPE:
    #             pygame.quit()
    #             sys.exit()
    #         if event.key == K_LEFT:
    #             moveLeft = False
    #         if event.key == K_RIGHT:
    #             moveRight = False
    #         if event.key == K_UP:
    #             moveUp = False
    #         if event.key == K_DOWN:
    #             moveDown = False




# define display surface
W, H = 1000, 480  #EDITED
HW, HH = W // 2, H // 2  # EDITED
AREA = W * H


moveUp = False
moveDown = False
moveRight = False
moveLeft = False


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

goomba1 = Goomba(DS, (1500, 385), 1)
goomba2 = Goomba(DS, (1550, 385), 1)
goomba3 = Goomba(DS, (1600, 385), 1)
goomba4 = Goomba(DS, (1650, 385), 1)
goomba5 = Goomba(DS, (1700, 385), 1)
goomba6 = Goomba(DS, (1750, 385), 1)
goomba7 = Goomba(DS, (1800, 385), 1)
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
rotating_sprites = Group()
goombas = Group()

pathx_sprites.add(redkoopa1)

goombas.add(goomba1)
goombas.add(goomba2)
goombas.add(goomba3)
goombas.add(goomba4)
goombas.add(goomba5)
goombas.add(goomba6)
goombas.add(goomba7)

no_pathx_sprites.add(greenkoopa1)
no_pathx_sprites.add(plant1)
no_pathx_sprites.add(flyingred1)
no_pathx_sprites.add(blooper1)
no_pathx_sprites.add(cheep1)
no_pathx_sprites.add(cheep2)
no_pathx_sprites.add(po1)

rotating_sprites.add(fire1)
rotating_sprites.add(fire2)
rotating_sprites.add(fire3)
rotating_sprites.add(fire4)
rotating_sprites.add(fire5)
rotating_sprites.add(fire6)

mario = TempMario(DS)
# mc = pygame.sprite.GroupSingle()
# mc.add(mario)
# mario = pygame.Rect(200, 365, 30, 50)
# vel = 5

# main loop
while True:
    # events()
    gf.check_events(mario)
    # gf.update_screen(mario)

    k = pygame.key.get_pressed()

    if k[K_RIGHT] and playerPosX != bgWidth - 300:
        playerVelocityX = 2  # was 1
    elif k[K_LEFT]:
        playerVelocityX = -2  # was -1
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
    # mario.update()

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

    for enemyy in rotating_sprites:
        if playerVelocityX > 0 and circlePosX == startScrollingPosX:
            enemyy.center_rot_x -= playerVelocityX

    for enemyy in goombas:
        if playerVelocityX > 0 and circlePosX == startScrollingPosX:
            enemyy.enemy_rect.x -= playerVelocityX

    no_pathx_sprites.update()
    pathx_sprites.update()
    rotating_sprites.update()
    goombas.update()

    # testing collision
    col = pygame.sprite.spritecollide(mario, goombas, False)
    for goomba in goombas:
        if col and (mario.rect.collidepoint(goomba.rect.midtop) or
                    mario.rect.collidepoint(goomba.rect.left + 10, goomba.rect.top)):  # FIX...kinda buggy
            goomba.dead = True
        if goomba.enemy_rect.y > W:
            goombas.remove(goomba)
        if col and goomba.rect.collidepoint(mario.rect.midright):
            mario.dead = True
    gf.mario_in_range(mario, goombas)

    pygame.draw.circle(DS, WHITE, (circlePosX, playerPosY - 10), circleRadius, 0)
    pygame.draw.circle(DS, (0, 0, 255), (playerPosX, playerPosY - 50), circleRadius, 0)
    # pygame.draw.rect(DS, (0, 255, 0), mario)
    mario.update()
    # mc.update()

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
