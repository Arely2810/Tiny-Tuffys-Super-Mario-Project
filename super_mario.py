import pygame
import sys
from enemy import Goomba
from enemy import KoopaTroopa
from enemy import Podoboo
from pygame.sprite import Group
from pygame.locals import *


def run_game():
    pygame.init()
    screen_width = 900
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
    pygame.display.set_caption("Super Mario")

    # Sprites
    koopa1 = KoopaTroopa(screen, 500, 420)
    koopa2 = KoopaTroopa(screen, 400, 420, 300, 700)
    goomba1 = Goomba(screen, 850, 430)
    podoboo1 = Podoboo(screen, 350, 500)
    allSprites = Group()
    allSprites.add(koopa1)
    allSprites.add(goomba1)
    allSprites.add(podoboo1)
    allSprites.add(koopa2)

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 150, 255))  # sky
        pygame.draw.rect(screen, (0, 200, 0), (0, 450, 300, 50))  # ground
        pygame.draw.rect(screen, (0, 200, 0), (400, 450, 500, 50))  # ground

        # goomba.drawMe(screen)
        # koopa.drawMe(screen)
        # goombas.update(screen)
        #goombas.update()
        #goombas.draw(screen)
        # goombas.draw(screen)
        allSprites.update()


        pygame.display.update()


run_game()
sys.exit()
