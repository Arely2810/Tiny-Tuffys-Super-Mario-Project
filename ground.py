import pygame
from pygame.sprite import Sprite


class Ground(Sprite):
    def __init__(self, screen, pos, size):
        super(Ground, self).__init__()
        self.screen = screen
        self.pos = pos
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.image = self.image.convert_alpha(screen)  # ?
        self.rect = self.image.get_rect()

        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
