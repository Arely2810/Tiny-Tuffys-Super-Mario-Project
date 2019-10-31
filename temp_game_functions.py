import pygame
import sys
from pygame.locals import *
from blocks import Block

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
        mario.is_moving = True
    if event.key == K_RIGHT:
        mario.moveLeft = False
        mario.moveRight = True
        mario.is_moving = True
    # if event.key == K_UP:
    #     mario.moveDown = False
    #     mario.moveUp = True
    #     mario.is_moving = True
    # if event.key == K_DOWN:
    #     mario.moveUp = False
    #     mario.moveDown = True
    #     mario.is_moving = True
    if event.key == K_SPACE:
        mario.jump = True
        mario.is_moving = True


def check_keyup_events(event, mario):
    if event.key == K_LEFT:
        mario.moveLeft = False
    if event.key == K_RIGHT:
        mario.moveRight = False
    # if event.key == K_UP:
    #     mario.moveUp = False
    # if event.key == K_DOWN:
    #     mario.moveDown = False
    # if event.key == K_SPACE:
    #     mario.jump = False


def check_enemy_collision(settings, enemies, mario):
    collision = pygame.sprite.spritecollide(mario, enemies, False)
    if collision:
        for enemy in enemies:
            # checks if mario collides with any of the top 3 points of enemy
            if mario.vel_y > 0 and (mario.rect.collidepoint(enemy.rect.topright)
                                    or mario.rect.collidepoint(enemy.rect.midtop)
                                    or mario.rect.collidepoint(enemy.rect.topleft)):
                enemy.dead = True
            # checks if goomba collides with mario's left top and right
            elif enemy.rect.collidepoint(mario.rect.topright) or enemy.rect.collidepoint(mario.rect.midright) or \
                    enemy.rect.collidepoint(mario.rect.bottomright) or enemy.rect.collidepoint(mario.rect.topleft) \
                    or enemy.rect.collidepoint(mario.rect.midleft) or enemy.rect.collidepoint(mario.rect.bottomleft)\
                    or enemy.rect.collidepoint(mario.rect.topright) or enemy.rect.collidepoint(mario.rect.midtop)\
                    or enemy.rect.collidepoint(mario.rect.topleft):
                mario.dead = True
                enemy.killed_mario = True
                for enemy_ in enemies:  # this loop stops all the enemies
                    enemy_.killed_mario = True
            if enemy.enemy_rect.y > settings.screen_width:
                enemies.remove(enemy)


def scroll_eveything_left(settings, mario, enemies, blocks):
    # type 1 -> sprites with no path x
    # type 2 -> sprites with path x
    # type 3 -> rotating sprites
    for enemy in enemies:
        if enemy.group_type == 1:
            if mario.moveRight and mario.rect.x == settings.start_scrolling_pos_x:
                enemy.enemy_rect.x -= mario.vel_x
        elif enemy.group_type == 2:
            if mario.moveRight and mario.rect.x == settings.start_scrolling_pos_x:
                enemy.enemy_rect.x -= mario.vel_x
                enemy.path_left -= mario.vel_x
                enemy.path_right -= mario.vel_x
        elif enemy.group_type == 3:
            if mario.moveRight and mario.rect.x == settings.start_scrolling_pos_x:
                enemy.center_rot_x -= mario.vel_x

    for block in blocks:
        if mario.moveRight and mario.rect.x == settings.start_scrolling_pos_x:
            block.x -= mario.vel_x

# MOVE THIS TO GAME_FUNCTIONS IN MASTER....make pixel range bigger???
def mario_in_range(mario, enemies):
    for enemy in enemies:
        if enemy.enemy_rect.x - mario.rect.x <= 800:
            enemy.is_move = True


def create_block(settings, screen, blocks):
    while settings.current_block < settings.number_of_blocks[settings.current_level]:
        block = Block(settings.block_positions[settings.current_level][settings.current_block], screen, settings.block_types[settings.current_level][settings.current_block], settings.block_items[settings.current_level][settings.current_block])
        settings.current_block += 1

        block.x = block.pos[0]
        block.y = block.pos[1]
        blocks.add(block)


def update_screen(mario):
    pass
