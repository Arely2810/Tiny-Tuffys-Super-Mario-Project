import pygame
from pygame.sprite import Sprite

# TEST CODE


class TempMario(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.height = 32
        self.width = 32
        self.color = (0, 255, 0)
        self.vel_x = 0
        self.vel_y = 0
        self.x = 200
        self.y = 385
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
            self.vel_x = 1
        elif self.moveLeft:
            self.vel_x = -1
        else:
            self.vel_x = 0
        self.rect.x += self.vel_x
        if self.moveDown:
            self.vel_y = 1
        elif self.moveUp:
            self.vel_y = -1
        else:
            self.vel_y = 0
        self.rect.y += self.vel_y


        if self.rect.x <= self.screen_rect.left:
            self.rect.x = self.screen_rect.left
        elif self.rect.x >= self.settings.start_scrolling_pos_x:
            self.rect.x = self.settings.start_scrolling_pos_x
            if self.settings.bg_x + (self.settings.bg_width + - self.settings.screen_width) >= 0:
                self.settings.bg_x -= self.vel_x



    def fall(self):
        self.moveDown = False
        self.moveUp = False
        self.moveRight = False
        self.moveLeft = False
        self.vel_y = 1
        self.rect.top += self.vel_y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        self.draw()
        self.move()
        if self.dead:
            self.fall()
