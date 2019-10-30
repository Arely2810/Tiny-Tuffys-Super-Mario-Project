import pygame
import sys
from pygame.locals import *

# TEST CODE


def check_events(mario):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            check_keydown_events(event, mario)
        if event.type == KEYUP:
            check_keyup_events(event, mario)


def check_keydown_events(event, mario):
    if event.key == K_LEFT:
        mario.moveRight = False
        mario.moveLeft = True
    if event.key == K_RIGHT:
        mario.moveLeft = False
        mario.moveRight = True
    if event.key == K_UP:
        mario.moveDown = False
        mario.moveUp = True
    if event.key == K_DOWN:
        mario.moveUp = False
        mario.moveDown = True


def check_keyup_events(event, mario):
    if event.key == K_LEFT:
        mario.moveLeft = False
    if event.key == K_RIGHT:
        mario.moveRight = False
    if event.key == K_UP:
        mario.moveUp = False
    if event.key == K_DOWN:
        mario.moveDown = False

# def check_enemy_collision(goombas, mario):
#     collision = pygame.sprite.spritecollide(mario, goombas, True)


# MOVE THIS TO GAME_FUNCTIONS IN MASTER....make pixel range bigger???
def mario_in_range(mario, enemies):
    for enemy in enemies:
        if enemy.enemy_rect.x - mario.rect.x <= 800:
            enemy.is_move = True


def update_screen(mario):
    pass
