import pygame
import sys
from fireball import Fireball
# from settings_arely import Settings
from mario import Mario



def mario_move(event, mario, settings, screen, fireball, ground):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                mario.is_idle = False
                mario.moving_right = True
                mario.moving_left = False
                mario.is_facing_right = True
                mario.is_facing_left = False
            elif event.key == pygame.K_LEFT:
                mario.is_idle = False
                mario.moving_left = True
                mario.moving_right = False
                mario.is_facing_left = True
                mario.is_facing_right = False
            elif event.key == pygame.K_SPACE:
                check_mario_ground(settings, screen, mario, ground)
                mario.is_idle = False
                mario.jump = True
            if mario.get_big:
                if event.key == pygame.K_DOWN:
                    mario.is_idle = False
                    mario.go_down = True
            if mario.is_fire:
                if event.key == pygame.K_LSHIFT or pygame.K_RSHIFT:
                    if len(fireball) < settings.fireballs_allowed:
                        new_fireball = Fireball(settings, screen, mario)
                        fireball.add(new_fireball)
            elif event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                mario.is_idle = True
            elif event.key == pygame.K_LEFT:
                mario.is_idle = True
            elif event.key == pygame.K_SPACE:
                mario.is_idle = True
                mario.jump = False
            if mario.is_big:
                if event.key == pygame.K_DOWN:
                    mario.go_down = False

def check_mario_ground(settings, screen, mario, ground):
    ground_check = mario.rect.colliderect(ground.rect)
    mario.touch_ground = ground_check


# will finish this after we figure out how the platforms will work
def check_mario_plat(settings, screen, mario, ground):
    pass

# def
