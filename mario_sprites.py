import pygame
import spritesheet

ss = spritesheet.spritesheet('mario/mario_sprites.png')

# standing still mario
still_image = ss.image_at()
