import pygame
from pygame.sprite import Sprite


class Fireball(Sprite):
    fireballs = [pygame.image.load('Cut-Sprites-For-Mario/Misc-3/190.png'),
                 pygame.image.load('Cut-Sprites-For-Mario/Misc-3/191.png'),
                 pygame.image.load('Cut-Sprites-For-Mario/Misc-3/192.png'),
                 pygame.image.load('Cut-Sprites-For-Mario/Misc-3/193.png')]

    fire_idle_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/23.png')]
    fire_run_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/19.png'),
                      pygame.image.load('Cut-Sprites-For-Mario/Mario/20.png'),
                      pygame.image.load('Cut-Sprites-For-Mario/Mario/21.png'),
                      pygame.image.load('Cut-Sprites-For-Mario/Mario/22.png')]
    fire_jump_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/17.png')]
    fire_swim_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/11.png'),
                       pygame.image.load('Cut-Sprites-For-Mario/Mario/12.png'),
                       pygame.image.load('Cut-Sprites-For-Mario/Mario/13.png'),
                       pygame.image.load('Cut-Sprites-For-Mario/Mario/14.png'),
                       pygame.image.load('Cut-Sprites-For-Mario/Mario/15.png')]
    fire_crouch_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/16.png')]
    fire_throw_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/20.png')]

    fire_idle_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/24.png')]
    fire_run_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/28.png'),
                     pygame.image.load('Cut-Sprites-For-Mario/Mario/27.png'),
                     pygame.image.load('Cut-Sprites-For-Mario/Mario/26.png'),
                     pygame.image.load('Cut-Sprites-For-Mario/Mario/25.png')]
    fire_jump_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/30.png')]
    fire_swim_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/10.png'),
                      pygame.image.load('Cut-Sprites-For-Mario/Mario/9.png'),
                      pygame.image.load('Cut-Sprites-For-Mario/Mario/8.png'),
                      pygame.image.load('Cut-Sprites-For-Mario/Mario/7.png'),
                      pygame.image.load('Cut-Sprites-For-Mario/Mario/6.png'),
                      pygame.image.load('Cut-Sprites-For-Mario/Mario/5.png')]
    fire_crouch_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/31.png')]
    fire_throw_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/27.png')]

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

    def fireballs_right(self):
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

    def fireballs_left(self):
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
            if self.pos_y + self.fire_height > 385 or self.pos_y < mario.rect.top/2:
                self.velocity[1] = -self.velocity[1]
        elif mario.is_facing_left:
            self.image = self.fireballs_left()
            self.pos_x -= self.velocity[0]
            self.pos_y -= self.velocity[1]

            if self.pos_x + self.fire_height > self.screen.width or self.pos_x < 0:
                self.velocity[0] = +self.velocity[0]

            if self.pos_y + self.fire_height > 385 or self.pos_y < mario.rect.top/2:
                self.velocity[1] = -self.velocity[1]
        self.blitme()
    # ill finish this after i have the images and code ready

    def blitme(self):
        self.screen.blit(self.image, self.rect)
