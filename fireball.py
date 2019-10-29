import pygame
from pygame.sprite import Sprite


class Fireball(Sprite):
    def __init__(self, settings, screen, mario):
        super(Fireball, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.fireball_width, settings.fireball_height)
        self.rect.centerx = mario.rect.centerx
        self.rect.top = mario.rect.top

        self.y = float(self.rect.y)

        # self.rect_image = [pygame.load('')]
        self.speed_ = settings.fireball_speed

    def update(self, mario):
        if mario.is_facing_right:
            self.x += self.speed_
        elif mario.is_facing_left:
            self.x -= self.speed_

    # ill finish this after i have the images and code ready
    def blitme(self):
        pass
