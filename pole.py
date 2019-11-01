import pygame
from pygame.sprite import Sprite

class Pole(Sprite):
    def __init__(self, screen, pos):
        super(Pole, self).__init__()
        self.screen = screen
        self.pos = pos
        self.image = pygame.image.load('images/pole.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

