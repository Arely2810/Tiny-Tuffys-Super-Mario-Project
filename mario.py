import pygame
from pygame.sprite import Sprite



class Mario(Sprite):
    def __init__(self, settings, screen):
        super(Mario, self).__init__()
        self.screen = screen

        # i'll do his image later cuz my sprites don't look the way i want them to
        # self.idle_image = [pygame.load('')]

        self.rect = pygame.Rect(540, 20, 40, 70)
        self.screen_rect = screen.get_rect()
        # r, sr = self.rect, self.screen_rect

        self.settings = settings
        self.moving_right = False
        self.moving_left = False
        self.jump = False


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right/2:
            self.rect.x += self.settings.mario_speed
        elif self.moving_right and self.rect.right == self.screen_rect.right/2:
            pass
            # continue his animation
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.mario_speed
        # ill edit this part later
        if self.jump and self.rect.top < self.screen_rect.top:
            self.rect.y += self.settings.mario_jump_speed
        elif not self.jump:
            self.rect.y -= self.settings.mario_jump_speed
        self.rect.centerx = self.rect.center

    # ill do this when the sprites are ready
    def blitme(self):
        pass

