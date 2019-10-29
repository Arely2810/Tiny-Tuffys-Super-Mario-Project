import pygame
import sys
from fireball import Fireball
# from settings_arely import Settings
from mario import Mario
from Block import Block
from tube import Tube



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


#Griffin's code
def create_block(settings, screen, blocks):
    while settings.current_block < settings.number_of_blocks[settings.current_level]:
        block = Block(settings.block_positions[settings.current_level][settings.current_block], screen, settings.block_types[settings.current_level][settings.current_block], settings.block_items[settings.current_level][settings.current_block])
        settings.current_block += 1

        block.x = block.pos[0]
        block.y = block.pos[1]
        blocks.add(block)

def create_item(settings, screen, blocks, items):
    for b in blocks:
        if b.item_type == 1:
            item = Item(1)
    pass
def create_tube(settings, screen, tubes):
    while settings.current_tube < settings.number_of_tubes[settings.current_level]:
        tube = Tube(settings.tube_positions[settings.current_level][settings.current_tube], screen, settings.tube_sizes[settings.current_level][settings.current_tube])
        settings.current_tube +=1

        tube.x = tube.pos[0]
        tube.y = tube.pos[1]
        tubes.add(tube)
        
def create_entities(settings, screen, blocks, tubes, enemies):
    create_block(settings, screen, blocks)
    create_tubes(settings, screen, tubes)
    create_enemies(settings, screen, enemies)
    pass

def update_screen(settings, screen, stats, scores, mario, blocks, enemies, items, fireball):
    blocks.draw(screen)
    tubes.draw(screen)
    pass
