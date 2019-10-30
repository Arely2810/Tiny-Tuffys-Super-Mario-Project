import pygame
from pygame.sprite import Sprite

# TEST CODE


class TempMario(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.height = 50
        self.width = 30
        self.color = (0, 255, 0)
        self.vel = 1
        self.x = 200
        self.y = 365
        self.moveRight = False
        self.moveLeft = False
        self.moveUp = False
        self.moveDown = False
        self.jump = False
        self.dead = False
        self.count = 0

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        # self.mario_rect = self.mario.get_rect()

    def move(self):
        if self.moveRight:
            self.rect.left += self.vel
        elif self.moveLeft:
            self.rect.left -= self.vel
        if self.moveUp:
            self.rect.top -= self.vel
        elif self.moveDown:
            self.rect.top += self.vel

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def fall(self):
        self.moveDown = False
        self.moveUp = False
        self.moveRight = False
        self.moveLeft = False
        self.rect.top += self.vel

    def update(self):
        self.draw()
        self.move()
        if self.dead:
            self.fall()
