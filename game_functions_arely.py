import pygame
import sys
from fireball import Fireball
from mario import Mario



def mario_walk(event, mario):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                mario.moving_right = True
            elif event.key == pygame.K_LEFT:
                mario.moving_left = True
            elif event.key == pygame.K_SPACE:
                mario.jump = True
            elif event.key == pygame.K_LSHIFT or pygame.K_RSHIFT:
                if len(fireball) < settings.fireballs_allowed:
                    new_fireball = Fireball(settings, screen, mario)
                    fireball.add(new_fireball)
            elif event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                mario.moving_right = False
            elif event.key == pygame.K_LEFT:
                mario.moving_left = False
            elif event.key == pygame.K_SPACE:
                mario.jump = False

