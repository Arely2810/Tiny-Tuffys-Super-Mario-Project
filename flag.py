import pygame
from pygame.sprite import Sprite

class Flag(Sprite):

    def __init__(self, screen, pos):
        super(Flag, self).__init__()
        self.screen = screen
        self.pos = pos
        self.yvel = 10
        self.captured = False
        self.image = pygame.image.load('images/flag.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y= float(self.rect.y)


    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

        while self.captured == True:
            if self.y > 384:
                self.y -= self.yvel
