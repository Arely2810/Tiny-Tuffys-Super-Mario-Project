import pygame
from pygame.sprite import Sprite
small_pipe = pygame.image.load('images/small_pipe.png')
medium_pipe = pygame.image.load('images/medium_pipe.png')
large_pipe = pygame.image.load('images/large_pipe.png')


class Pipe(Sprite):
    def __init__(self, pos, screen, size = 0):
        self.pos = pos
        self.screen = screen
        self.size = size
        self.set_pipe_size()

    def update(self):
        self.rect.x = self.x



    def set_pipe_size(self):
        if self.size == 0:
            self.image = small_pipe
        if self.size == 1:
            self.image = medium_pipe
        if self.size == 2:
            self.image = large_pipe

        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

