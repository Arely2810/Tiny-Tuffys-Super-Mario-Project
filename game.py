# import math
# import random
# import sys
# import pygame
# from pygame.locals import *
from enemy import *
from pygame.sprite import Group
from mario import Mario
import game_functions as gf
from settings import Settings
from scoreboard import ScoreBoard

pygame.init()
CLOCK = pygame.time.Clock()
settings = Settings()
display_screen = settings.display_screen
pygame.display.set_caption("Super Mario")

scoreboard = ScoreBoard(display_screen)
mario = Mario(settings, display_screen)


enemies = Group()
blocks = Group()
pipes = Group()
fireball = Group()

gf.create_block(settings, display_screen, blocks)
gf.create_pipe(settings, display_screen, pipes)
gf.create_enemy(settings, display_screen, enemies)

# main loop
while True:
    # gf.check_events(mario)
    gf.mario_move(mario, settings, display_screen, fireball)
    display_screen.blit(settings.bg_image, settings.bg_position())

    gf.mario_in_range(mario, enemies)
    gf.scroll_eveything_left(settings, mario, enemies, blocks, pipes)
    gf.check_collision(settings, enemies, mario, blocks, pipes)

    scoreboard.update_screen()

    enemies.update()
    mario.update()
    blocks.update()
    blocks.draw(display_screen)
    pipes.update()
    pipes.draw(display_screen)

    pygame.display.update()
    CLOCK.tick(settings.FPS)
    display_screen.fill((0, 0, 0))
