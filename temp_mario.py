import pygame
from pygame.sprite import Sprite

# TEST CODE


class TempMario(Sprite):
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
        self.is_moving = False
        self.moveRight = False
        self.moveLeft = False
        self.moveUp = False
        self.moveDown = False
        self.jump = False
        self.dead = False
        self.count = 0

        self.velocity = 0
        self.gravity = 1.2

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        # self.mario_rect = self.mario.get_rect()

    def move(self):
        if self.moveRight:
            self.vel_x = 1
        elif self.moveLeft:
            self.vel_x = -1
        else:
            self.vel_x = 0
            self.is_moving = False
        self.rect.x += self.vel_x
        if self.moveDown:
            self.vel_y = 1
        elif self.moveUp:
            self.vel_y = -1
        else:
            self.vel_y = 0
            self.is_moving = False
        self.rect.y += self.vel_y

        self.mario_jump()

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

    def mario_jump(self):
        if self.jump:
            self.vel_y = -1
            self.rect.y += self.vel_y
            if abs(self.rect.y - 385) >= 150:
                self.jump = False
        if not self.jump:
            self.vel_y = 1
            self.rect.y += self.vel_y
            if self.rect.y > 385:
                self.rect.y = 385

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        self.draw()
        self.move()
        if self.dead:
            self.fall()
