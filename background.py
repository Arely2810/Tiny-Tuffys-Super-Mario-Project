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
from temp_settings import Settings
from blocks import Block

pygame.init()
CLOCK = pygame.time.Clock()
settings = Settings()
display_screen = settings.display_screen
pygame.display.set_caption("Super Mario")

goomba1 = Goomba(display_screen, (1500, 385), 1)
goomba2 = Goomba(display_screen, (1550, 385), 1)
goomba3 = Goomba(display_screen, (1600, 385), 1)
goomba4 = Goomba(display_screen, (1650, 385), 1)
goomba5 = Goomba(display_screen, (1700, 385), 1)
goomba6 = Goomba(display_screen, (1750, 385), 1)
goomba7 = Goomba(display_screen, (1800, 385), 1)
greenkoopa1 = KoopaTroopa(display_screen, (1500, 380), 1)
redkoopa1 = KoopaTroopa(display_screen, (850, 380), 2, 800, 1100)
plant1 = PiranhaPlant(display_screen, (1100, 380), 2, 350, 390)
flyingred1 = KoopaParatroopa(display_screen, (1100, 200), 2, 180, 250)
blooper1 = Blooper(display_screen, (2000, 200))
cheep1 = CheepCheep(display_screen, (2100, 300), 1)
cheep2 = CheepCheep(display_screen, (2100, 350), 2)
po1 = Podoboo(display_screen, (2225, 480), 300, 500)
fire1 = FireBar(display_screen, (300, 200), 0)
fire2 = FireBar(display_screen, (300, 200), 15)
fire3 = FireBar(display_screen, (300, 200), 30)
fire4 = FireBar(display_screen, (300, 200), 45)
fire5 = FireBar(display_screen, (300, 200), 60)
fire6 = FireBar(display_screen, (300, 200), 75)

allEnemies = Group()
pathx_sprites = Group()


# pathx_sprites.add(redkoopa1)
#
# goombas.add(goomba1)
# goombas.add(goomba2)
# goombas.add(goomba3)
# goombas.add(goomba4)
# goombas.add(goomba5)
# goombas.add(goomba6)
# goombas.add(goomba7)
#
# no_pathx_sprites.add(greenkoopa1)
# no_pathx_sprites.add(plant1)
# no_pathx_sprites.add(flyingred1)
# no_pathx_sprites.add(blooper1)
# no_pathx_sprites.add(cheep1)
# no_pathx_sprites.add(cheep2)
# no_pathx_sprites.add(po1)
#
# rotating_sprites.add(fire1)
# rotating_sprites.add(fire2)
# rotating_sprites.add(fire3)
# rotating_sprites.add(fire4)
# rotating_sprites.add(fire5)
# rotating_sprites.add(fire6)

allEnemies.add(redkoopa1)

allEnemies.add(goomba1)
allEnemies.add(goomba2)
allEnemies.add(goomba3)
allEnemies.add(goomba4)
allEnemies.add(goomba5)
allEnemies.add(goomba6)
allEnemies.add(goomba7)

allEnemies.add(greenkoopa1)
# allEnemies.add(plant1)
# allEnemies.add(flyingred1)
# allEnemies.add(blooper1)
# allEnemies.add(cheep1)
# allEnemies.add(cheep2)
# allEnemies.add(po1)

allEnemies.add(fire1)
allEnemies.add(fire2)
allEnemies.add(fire3)
allEnemies.add(fire4)
allEnemies.add(fire5)
allEnemies.add(fire6)

mario = TempMario(display_screen, settings)

blocks = Group()

# main loop
while True:
    gf.check_events(mario)
    display_screen.blit(settings.bg_image, settings.bg_position())

    gf.scroll_eveything_left(settings, mario, allEnemies, blocks)

    allEnemies.update()

    # testing collision
    gf.check_enemy_collision(settings, allEnemies, mario)
    gf.mario_in_range(mario, allEnemies)
    gf.create_block(settings, display_screen, blocks)

    mario.update()
    blocks.update()
    blocks.draw(display_screen)

    pygame.display.update()
    CLOCK.tick(settings.FPS)
    display_screen.fill((0, 0, 0))
