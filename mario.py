import pygame
from pygame.sprite import Sprite
import math


class Mario(Sprite):
    mario_idle_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/75.png')]
    mario_run_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/79.png'),
                       pygame.image.load('Cut-Sprites-For-Mario/Mario/81.png')]
    mario_jump_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/86.png')]
    mario_swim_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/76.png'),
                        pygame.image.load('Cut-Sprites-For-Mario/Mario/77.png'),
                        pygame.image.load('Cut-Sprites-For-Mario/Mario/78.png'),
                        pygame.image.load('Cut-Sprites-For-Mario/Mario/80.png'),
                        pygame.image.load('Cut-Sprites-For-Mario/Mario/83.png')]
    mario_idle_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/73.png')]
    mario_run_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/69.png'),
                      pygame.image.load('Cut-Sprites-For-Mario/Mario/68.png')]
    mario_jump_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/64.png')]
    mario_swim_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/67.png'),
                       pygame.image.load('Cut-Sprites-For-Mario/Mario/70.png'),
                       pygame.image.load('Cut-Sprites-For-Mario/Mario/71.png'),
                       pygame.image.load('Cut-Sprites-For-Mario/Mario/72.png'),
                       pygame.image.load('Cut-Sprites-For-Mario/Mario/74.png')]
    big_mario_idle_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/54.png')]
    big_mario_run_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/51.png'),
                           pygame.image.load('Cut-Sprites-For-Mario/Mario/52.png'),
                           pygame.image.load('Cut-Sprites-For-Mario/Mario/53.png')]
    big_mario_jump_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/49.png')]
    big_mario_swim_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/40.png'),
                            pygame.image.load('Cut-Sprites-For-Mario/Mario/41.png'),
                            pygame.image.load('Cut-Sprites-For-Mario/Mario/42.png'),
                            pygame.image.load('Cut-Sprites-For-Mario/Mario/43.png'),
                            pygame.image.load('Cut-Sprites-For-Mario/Mario/44.png'),
                            pygame.image.load('Cut-Sprites-For-Mario/Mario/45.png')]
    big_mario_crouch_right = [pygame.image.load('Cut-Sprites-For-Mario/Mario/48.png')]
    big_mario_idle_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/55.png')]
    big_mario_run_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/58.png'),
                          pygame.image.load('Cut-Sprites-For-Mario/Mario/57.png'),
                          pygame.image.load('Cut-Sprites-For-Mario/Mario/56.png')]
    big_mario_jump_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/60.png')]
    big_mario_swim_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/34.png'),
                           pygame.image.load('Cut-Sprites-For-Mario/Mario/35.png'),
                           pygame.image.load('Cut-Sprites-For-Mario/Mario/36.png'),
                           pygame.image.load('Cut-Sprites-For-Mario/Mario/37.png'),
                           pygame.image.load('Cut-Sprites-For-Mario/Mario/38.png'),
                           pygame.image.load('Cut-Sprites-For-Mario/Mario/39.png')]
    big_mario_crouch_left = [pygame.image.load('Cut-Sprites-For-Mario/Mario/61.png')]

    def __init__(self, settings, screen):
        super(Mario, self).__init__()
        self.screen = screen

        # i'll do his image later cuz my sprites don't look the way i want them to
        # self.idle_image = [pygame.load('')]
        #
        # self.rect = pygame.Rect(5, 700, 32, 32)
        # self.screen_rect = screen.get_rect()
        # r, sr = self.rect, self.screen_rect

        self.settings = settings
        self.is_facing_right = False
        self.is_idle = False
        self.is_facing_right = True
        self.is_facing_left = False
        self.moving_right = False
        self.moving_left = False
        self.jump = False
        self.falling = False
        self.touch_ground = False
        # touching platform
        self.touch_plat = False
        self.get_big = False
        self.is_fire = False
        # self.is_big = False
        self.go_down = False
        self.count = 0
        self.death = False
        self.jump_count = 10
        # i'll do his image later cuz my sprites don't look the way i want them to
        # self.idle_image = [pygame.load('')]

        self.rect = pygame.Rect(4, 385, 32, 32)
        # pygame.draw.rect(screen, (255, 255, 255), self.rect)
        self.screen_rect = screen.get_rect()
        self.rect.x = 4
        self.rect.y = 385
        # self.x = float(self.rect.x)
        # self.y = float(self.rect.y)
        self.center = float(self.rect.centerx)
        # self.ycenter = float(self.rect.centery)

        # r, sr = self.rect, self.screen_rect
        self.big_rect = pygame.Rect(self.rect.x, self.rect.y, 32, 64)

        self.image = pygame.transform.scale(self.mario_idle_right[0], (self.rect.width, self.rect.height))
        self.velocity = 0
        self.gravity = 1.2

    def run_right_animation(self, timer=30):
        if self.get_big:
            if self.count < 30:
                self.image = pygame.transform.scale(self.big_mario_run_right[0], (self.rect.width,
                                                                                  self.rect.height))
            elif 10 <= self.count < 20:
                self.image = pygame.transform.scale(self.big_mario_run_right[1], (self.rect.width,
                                                                                  self.rect.height))
            elif 20 <= self.count < 30:
                self.image = pygame.transform.scale(self.big_mario_run_right[2], (self.rect.width,
                                                                                  self.rect.height))
            elif self.count > 30:
                self.count = 0
        elif not self.get_big:
            if self.count < 15:
                self.image = pygame.transform.scale(self.mario_run_right[0], (self.rect.width,
                                                                              self.rect.height))
            elif 15 <= self.count < 30:
                self.image = pygame.transform.scale(self.mario_run_right[1], (self.rect.width,
                                                                              self.rect.height))
            elif self.count > 30:
                self.count = 0
        self.count += 1
        return self.image

    def run_left_animation(self, timer=30):
        if self.get_big:
            if self.count < 10:
                self.image = pygame.transform.scale(self.big_mario_run_left[0], (self.rect.width,
                                                                                 self.rect.height))
            elif 10 <= self.count < 20:
                self.image = pygame.transform.scale(self.big_mario_run_left[1], (self.rect.width,
                                                                                 self.rect.height))
            elif 20 <= self.count < 30:
                self.image = pygame.transform.scale(self.big_mario_run_left[2], (self.rect.width,
                                                                                 self.rect.height))
            elif self.count > 30:
                self.count = 0
        elif not self.get_big:
            if self.count < 15:
                self.image = pygame.transform.scale(self.mario_run_left[0], (self.rect.width,
                                                                             self.rect.height))
            elif 15 <= self.count < 30:
                self.image = pygame.transform.scale(self.mario_run_left[1], (self.rect.width,
                                                                             self.rect.height))
            elif self.count > 30:
                self.count = 0
        self.count += 1
        return self.image

    def jump_right(self):
        if self.get_big:
            self.image = pygame.transform.scale(self.big_mario_jump_right[0], (self.rect.width,
                                                                               self.rect.height))
        elif not self.get_big:
            self.image = pygame.transform.scale(self.mario_jump_right[0], (self.rect.width,
                                                                           self.rect.height))
        return self.image

    def jump_left(self):
        if self.get_big:
            self.image = pygame.transform.scale(self.big_mario_jump_left[0], (self.rect.width,
                                                                              self.rect.height))
        elif not self.get_big:
            self.image = pygame.transform.scale(self.mario_jump_left[0], (self.rect.width,
                                                                          self.rect.height))
        return self.image

    def update(self):
        # self.rect.x = self.x
        # self.rect.y = self.y

        if self.count >= 30:
            self.count = 0

        if not self.death:

            if self.is_facing_right and self.is_idle and not self.moving_right:
                self.image = pygame.transform.scale(self.mario_idle_right[0], (self.rect.width, self.rect.height))
            elif self.is_facing_left and self.is_idle and not self.moving_left:
                self.image = pygame.transform.scale(self.mario_idle_left[0], (self.rect.width, self.rect.height))

            if self.get_big:
                self.rect.width, self.rect.height = self.big_rect.width, self.big_rect.height
                if self.is_facing_right and self.is_idle and not self.moving_right:
                    self.image = pygame.transform.scale(self.big_mario_idle_right[0],
                                                        (self.rect.width, self.rect.height))
                elif self.is_facing_left and self.is_idle and not self.moving_left:
                    self.image = pygame.transform.scale(self.big_mario_idle_left[0],
                                                        (self.rect.width, self.rect.height))
            elif not self.get_big:
                self.rect.width, self.rect.height = self.rect.width, self.rect.height

            if self.moving_right and self.rect.right < self.screen_rect.right/2:
                self.image = self.run_right_animation()
                self.center += self.settings.mario_speed
                # add mario animation

                if self.settings.level == 6:
                    self.rect.y += self.settings.mario_speed/2
                    if self.get_big:
                        if self.count == 0:
                            self.image = pygame.transform.scale(self.big_mario_swim_right[0], (self.rect.width,
                                                                                               self.rect.height))
                            self.screen.blit(self.image, self.rect)
                        elif self.count == 1:
                            self.image = pygame.transform.scale(self.big_mario_swim_right[1], (self.rect.width,
                                                                                               self.rect.height))
                            self.screen.blit(self.image, self.rect)
                        elif self.count == 2:
                            self.image = pygame.transform.scale(self.big_mario_swim_right[2], (self.rect.width,
                                                                                               self.rect.height))
                            self.screen.blit(self.image, self.rect)
                        elif self.count == 3:
                            self.image = pygame.transform.scale(self.big_mario_swim_right[3], (self.rect.width,
                                                                                               self.rect.height))
                            self.screen.blit(self.image, self.rect)
                        elif self.count == 4:
                            self.image = pygame.transform.scale(self.big_mario_swim_right[4], (self.rect.width,
                                                                                               self.rect.height))
                            self.screen.blit(self.image, self.rect)
                        elif self.count == 5:
                            self.image = pygame.transform.scale(self.big_mario_swim_right[5], (self.rect.width,
                                                                                               self.rect.height))
                            self.screen.blit(self.image, self.rect)
                        elif self.count == 6:
                            self.image = pygame.transform.scale(self.big_mario_swim_right[6], (self.rect.width,
                                                                                               self.rect.height))
                            self.screen.blit(self.image, self.rect)
                        if self.count > 6:
                            self.count = 0
                    elif not self.get_big:
                        if self.count == 0:
                            self.image = pygame.transform.scale(self.mario_swim_right[0], (self.rect.width,
                                                                                           self.rect.height))
                            self.screen.blit(self.image, self.rect)
                        elif self.count == 1:
                            self.image = pygame.transform.scale(self.mario_swim_right[1], (self.rect.width,
                                                                                           self.rect.height))
                            self.screen.blit(self.image, self.rect)
                        elif self.count == 2:
                            self.image = pygame.transform.scale(self.mario_swim_right[2], (self.rect.width,
                                                                                           self.rect.height))
                            self.screen.blit(self.image, self.rect)
                        elif self.count == 3:
                            self.image = pygame.transform.scale(self.mario_swim_right[3], (self.rect.width,
                                                                                           self.rect.height))
                            self.screen.blit(self.image, self.rect)
                        elif self.count == 4:
                            self.image = pygame.transform.scale(self.mario_swim_right[4], (self.rect.width,
                                                                                           self.rect.height))
                            self.screen.blit(self.image, self.rect)
                        elif self.count == 5:
                            self.image = pygame.transform.scale(self.mario_swim_right[5], (self.rect.width,
                                                                                           self.rect.height))
                            self.screen.blit(self.image, self.rect)

                        if self.count > 5:
                            self.count = 0

            elif self.moving_right and self.rect.right == self.screen_rect.right/2:

                # continue his animation
                if self.settings.level == 6:
                    self.rect.y += self.settings.mario_speed/2
                    #add swimming animation
                    if self.get_big:
                        if self.count == 0:
                            self.image = pygame.transform.scale(self.big_mario_swim_right[0], (self.rect.width,
                                                                                               self.rect.height))
                        elif self.count == 1:
                            self.image = pygame.transform.scale(self.big_mario_swim_right[1], (self.rect.width,
                                                                                               self.rect.height))
                        elif self.count == 2:
                            self.image = pygame.transform.scale(self.big_mario_swim_right[2], (self.rect.width,
                                                                                               self.rect.height))
                        elif self.count == 3:
                            self.image = pygame.transform.scale(self.big_mario_swim_right[3], (self.rect.width,
                                                                                               self.rect.height))
                        elif self.count == 4:
                            self.image = pygame.transform.scale(self.big_mario_swim_right[4], (self.rect.width,
                                                                                               self.rect.height))
                        elif self.count == 5:
                            self.image = pygame.transform.scale(self.big_mario_swim_right[5], (self.rect.width,
                                                                                               self.rect.height))
                        elif self.count == 6:
                            self.image = pygame.transform.scale(self.big_mario_swim_right[6], (self.rect.width,
                                                                                               self.rect.height))
                        if self.count > 6:
                            self.count = 0
                    elif not self.get_big:
                        if self.count == 0:
                            self.image = pygame.transform.scale(self.mario_swim_right[0], (self.rect.width,
                                                                                           self.rect.height))
                        elif self.count == 1:
                            self.image = pygame.transform.scale(self.mario_swim_right[1], (self.rect.width,
                                                                                           self.rect.height))
                        elif self.count == 2:
                            self.image = pygame.transform.scale(self.mario_swim_right[2], (self.rect.width,
                                                                                           self.rect.height))
                        elif self.count == 3:
                            self.image = pygame.transform.scale(self.mario_swim_right[3], (self.rect.width,
                                                                                           self.rect.height))
                        elif self.count == 4:
                            self.image = pygame.transform.scale(self.mario_swim_right[4], (self.rect.width,
                                                                                           self.rect.height))
                        elif self.count == 5:
                            self.image = pygame.transform.scale(self.mario_swim_right[5], (self.rect.width,
                                                                                           self.rect.height))

                        if self.count > 5:
                            self.count = 0
            if self.get_big and self.go_down:
                # add crouch animation
                if self.is_facing_right:
                    self.image = pygame.transform.scale(self.big_mario_crouch_right[0], (self.rect.width,
                                                                                         self.rect.height))
                elif self.is_facing_left:
                    self.image = pygame.transform.scale(self.big_mario_crouch_left[0], (self.rect.width,
                                                                                        self.rect.height))

            if self.moving_left and self.rect.left > 0:
                self.image = self.run_left_animation()
                self.center -= self.settings.mario_speed
                # add mario animation

                if self.settings.level == 6:
                    self.rect.y += self.settings.mario_speed/2
                    #add swimming animation
                    if self.get_big:
                        if self.count == 0:
                            self.image = pygame.transform.scale(self.big_mario_swim_left[0], (self.rect.width,
                                                                                              self.rect.height))
                        elif self.count == 1:
                            self.image = pygame.transform.scale(self.big_mario_swim_left[1], (self.rect.width,
                                                                                              self.rect.height))
                        elif self.count == 2:
                            self.image = pygame.transform.scale(self.big_mario_swim_left[2], (self.rect.width,
                                                                                              self.rect.height))
                        elif self.count == 3:
                            self.image = pygame.transform.scale(self.big_mario_swim_left[3], (self.rect.width,
                                                                                              self.rect.height))
                        elif self.count == 4:
                            self.image = pygame.transform.scale(self.big_mario_swim_left[4], (self.rect.width,
                                                                                              self.rect.height))
                        elif self.count == 5:
                            self.image = pygame.transform.scale(self.big_mario_swim_left[5], (self.rect.width,
                                                                                              self.rect.height))
                        elif self.count == 6:
                            self.image = pygame.transform.scale(self.big_mario_swim_left[6], (self.rect.width,
                                                                                              self.rect.height))
                        if self.count > 6:
                            self.count = 0
                    elif not self.get_big:
                        if self.count == 0:
                            self.image = pygame.transform.scale(self.mario_swim_left[0], (self.rect.width,
                                                                                          self.rect.height))
                        elif self.count == 1:
                            self.image = pygame.transform.scale(self.mario_swim_left[1], (self.rect.width,
                                                                                          self.rect.height))
                        elif self.count == 2:
                            self.image = pygame.transform.scale(self.mario_swim_left[2], (self.rect.width,
                                                                                          self.rect.height))
                        elif self.count == 3:
                            self.image = pygame.transform.scale(self.mario_swim_left[3], (self.rect.width,
                                                                                          self.rect.height))
                        elif self.count == 4:
                            self.image = pygame.transform.scale(self.mario_swim_left[4], (self.rect.width,
                                                                                          self.rect.height))
                        elif self.count == 5:
                            self.image = pygame.transform.scale(self.mario_swim_left[5], (self.rect.width,
                                                                                          self.rect.height))
                        if self.count > 5:
                            self.count = 0
            # ill edit this part later
            if self.jump:
                self.velocity = -1
                self.rect.y += self.velocity
                if abs(self.rect.y - 385) >= 150:
                    self.jump = False
            if not self.jump and self.falling:
                self.velocity = 1
                self.rect.y += self.velocity
                if self.rect.y > 385:
                    self.rect.y = 385
                # self.rect.top -= self.settings.mario_jump_speed
                # add half of mario jump animation

                if self.settings.level == 6:
                    # add swimming animation
                    # self.rect.y += self.settings.mario_speed / 2
                    if self.is_facing_right:
                        if self.get_big:
                            if self.count == 0:
                                self.image = pygame.transform.scale(self.big_mario_swim_right[0], (self.rect.width,
                                                                                                   self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            elif self.count == 1:
                                self.image = pygame.transform.scale(self.big_mario_swim_right[1], (self.rect.width,
                                                                                                   self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            elif self.count == 2:
                                self.image = pygame.transform.scale(self.big_mario_swim_right[2], (self.rect.width,
                                                                                                   self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            elif self.count == 3:
                                self.image = pygame.transform.scale(self.big_mario_swim_right[3], (self.rect.width,
                                                                                                   self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            elif self.count == 4:
                                self.image = pygame.transform.scale(self.big_mario_swim_right[4], (self.rect.width,
                                                                                                   self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            elif self.count == 5:
                                self.image = pygame.transform.scale(self.big_mario_swim_right[5], (self.rect.width,
                                                                                                   self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            elif self.count == 6:
                                self.image = pygame.transform.scale(self.big_mario_swim_right[6], (self.rect.width,
                                                                                                   self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            if self.count > 6:
                                self.count = 0
                        elif not self.get_big:
                            if self.count == 0:
                                self.image = pygame.transform.scale(self.mario_swim_right[0], (self.rect.width,
                                                                                               self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            elif self.count == 1:
                                self.image = pygame.transform.scale(self.mario_swim_right[1], (self.rect.width,
                                                                                               self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            elif self.count == 2:
                                self.image = pygame.transform.scale(self.mario_swim_right[2], (self.rect.width,
                                                                                               self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            elif self.count == 3:
                                self.image = pygame.transform.scale(self.mario_swim_right[3], (self.rect.width,
                                                                                               self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            elif self.count == 4:
                                self.image = pygame.transform.scale(self.mario_swim_right[4], (self.rect.width,
                                                                                               self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            elif self.count == 5:
                                self.image = pygame.transform.scale(self.mario_swim_right[5], (self.rect.width,
                                                                                               self.rect.height))
                                self.screen.blit(self.image, self.rect)

                            if self.count > 5:
                                self.count = 0
                    elif not self.is_facing_left:
                        if self.get_big:
                            if self.count == 0:
                                self.image = pygame.transform.scale(self.big_mario_swim_left[0], (self.rect.width,
                                                                                                  self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            elif self.count == 1:
                                self.image = pygame.transform.scale(self.big_mario_swim_left[1], (self.rect.width,
                                                                                                  self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            elif self.count == 2:
                                self.image = pygame.transform.scale(self.big_mario_swim_left[2], (self.rect.width,
                                                                                                  self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            elif self.count == 3:
                                self.image = pygame.transform.scale(self.big_mario_swim_left[3], (self.rect.width,
                                                                                                  self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            elif self.count == 4:
                                self.image = pygame.transform.scale(self.big_mario_swim_left[4], (self.rect.width,
                                                                                                  self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            elif self.count == 5:
                                self.image = pygame.transform.scale(self.big_mario_swim_left[5], (self.rect.width,
                                                                                                  self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            elif self.count == 6:
                                self.image = pygame.transform.scale(self.big_mario_swim_left[6], (self.rect.width,
                                                                                                  self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            if self.count > 6:
                                self.count = 0
                        elif not self.get_big:
                            if self.count == 0:
                                self.image = pygame.transform.scale(self.mario_swim_left[0], (self.rect.width,
                                                                                              self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            elif self.count == 1:
                                self.image = pygame.transform.scale(self.mario_swim_left[1], (self.rect.width,
                                                                                              self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            elif self.count == 2:
                                self.image = pygame.transform.scale(self.mario_swim_left[2], (self.rect.width,
                                                                                              self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            elif self.count == 3:
                                self.image = pygame.transform.scale(self.mario_swim_left[3], (self.rect.width,
                                                                                              self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            elif self.count == 4:
                                self.image = pygame.transform.scale(self.mario_swim_left[4], (self.rect.width,
                                                                                              self.rect.height))
                                self.screen.blit(self.image, self.rect)
                            elif self.count == 5:
                                self.image = pygame.transform.scale(self.mario_swim_left[5], (self.rect.width,
                                                                                              self.rect.height))
                                self.screen.blit(self.image, self.rect)

                            if self.count > 5:
                                self.count = 0
                # if self.is_facing_right:
                #     self.rect.x += self.settings.mario_jump_speed
                # elif self.is_facing_left:
                #     self.rect.x -= self.settings.mario_jump_speed

            # honestly dont know if we need this part
            # elif not self.jump and not self.touch_ground and not self.touch_plat:
            #     self.rect.y += self.settings.mario_jump_speed
            #     # add falling half of mario jump animation
        else:
            self.dead()
        # self.count += 1
        # THIS BLIT WORKS FOR ANIMATION BUT NOT MOVEMENT
        # self.blitme()
        self.rect.centerx = self.center
        # THIS BLIT WORKS FOR MOVEMENT BUT NOT ANIMATION
        self.blitme()

        # self.rect.centery = self.ycenter

    # ill do this when the sprites are ready
    def dead(self):
        pass
    def blitme(self):
        self.screen.blit(self.image, self.rect)


