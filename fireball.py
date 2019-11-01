import pygame
from pygame.sprite import Sprite


class Fireball(Sprite):
    fireballs = [pygame.image.load('Cut-Sprites-For-Mario/Misc-3/190.png'),
                 pygame.image.load('Cut-Sprites-For-Mario/Misc-3/191.png'),
                 pygame.image.load('Cut-Sprites-For-Mario/Misc-3/192.png'),
                 pygame.image.load('Cut-Sprites-For-Mario/Misc-3/193.png')]
    def __init__(self, settings, screen, mario):
        super(Fireball, self).__init__()
        self.screen = screen
        self.count = 0

        self.rect = pygame.Rect(0, 0, settings.fireball_width, settings.fireball_height)
        self.rect.centerx = mario.rect.centerx
        self.rect.top = mario.rect.top / 2

        self.y = float(self.rect.y)
        self.image = pygame.transform.scale(self.fireballs[0], (self.rect.width, self.rect.height))

        # self.rect_image = [pygame.load('')]
        self.speed_ = settings.fireball_speed
        self.fire_height = 5
        self.velocity = [1, 1]

        self.pos_x = mario.rect.right
        self.pos_y = mario.rect.top/2

    def fireballs_right(self, timer=30):
        if self.count < 7:
            self.image = pygame.transform.scale(self.fire_run_right[0], (self.rect.width,
                                                                         self.rect.height))
        elif 7 <= self.count < 15:
            self.image = pygame.transform.scale(self.fire_run_right[1], (self.rect.width,
                                                                         self.rect.height))
        elif 15 <= self.count < 22:
            self.image = pygame.transform.scale(self.fire_run_right[2], (self.rect.width,
                                                                         self.rect.height))
        elif 22 <= self.count < 30:
            self.image = pygame.transform.scale(self.fire_run_right[3], (self.rect.width,
                                                                         self.rect.height))
        elif self.count > 30:
            self.count = 0
        self.count += 1
        return self.image

    def fireballs_left(self, timer=30):
        if self.count < 7:
            self.image = pygame.transform.scale(self.fire_run_right[3], (self.rect.width,
                                                                         self.rect.height))
        elif 7 <= self.count < 15:
            self.image = pygame.transform.scale(self.fire_run_right[2], (self.rect.width,
                                                                         self.rect.height))
        elif 15 <= self.count < 22:
            self.image = pygame.transform.scale(self.fire_run_right[1], (self.rect.width,
                                                                         self.rect.height))
        elif 22 <= self.count < 30:
            self.image = pygame.transform.scale(self.fire_run_right[0], (self.rect.width,
                                                                         self.rect.height))
        elif self.count > 30:
            self.count = 0
        self.count += 1
        return self.image

    def update(self, mario):
        if mario.is_facing_right:
            self.pos_x += self.velocity[0]
            self.pos_y += self.velocity[1]
            self.image = self.fireballs_right()
            if self.pos_x + self.fire_height > self.screen.width or self.pos_x < 0:
                self.velocity[0] = -self.velocity[0]
            if self.pos_y + self.fire_height > self.screen.height or self.pos_y < mario.rect.top/2:
                self.velocity[1] = -self.velocity[1]
        elif mario.is_facing_left:
            self.image = self.fireballs_left()
            self.pos_x -= self.velocity[0]
            self.pos_y -= self.velocity[1]

            if self.pos_x + self.fire_height > self.screen.width or self.pos_x < 0:
                self.velocity[0] = +self.velocity[0]

            if self.pos_y + self.fire_height > self.screen.height or self.pos_y < mario.rect.top/2:
                self.velocity[1] = -self.velocity[1]

    # ill finish this after i have the images and code ready
    def blitme(self):
        self.screen.blit(self.image, self.rect)
