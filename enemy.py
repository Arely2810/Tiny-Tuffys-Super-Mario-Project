import pygame
import math
from math import *
from pygame.sprite import Sprite
import random


class Enemy(Sprite):
    def __init__(self, screen, pos, width, height, points, group_type):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.screen_height = self.screen_rect.height
        self.group_type = group_type
        self.points = points  # FIX ALL POINTS FOR ENEMIES AFTER
        self.total_score = 0
        self.count = 0
        self.vel_x = -1  # negative bc sprite will most likely be moving left
        self.vel_y = 2
        self.width = width  # width of sprite
        self.height = height  # height of sprite
        self.dead = False
        self.is_move = False
        self.killed_mario = False
        self.on_ground = False
        self.falling = True

        # default image...images can be overwrite in other classes...how do i do empty image here???
        self.images = [pygame.image.load('images/goomba_1.png'), pygame.image.load('images/goomba_2.png')]
        self.enemy, self.enemy_image = self.animation2()
        self.enemy_rect = self.enemy.get_rect()
        self.enemy_rect.x = pos[0]  # x
        self.enemy_rect.y = pos[1]  # y

        self.X = pos[0]
        self.Y = pos[1]

    def animation2(self, timer=80):  # constant 2 frame animation forward
        # if self.vel_x < 0:
        if self.count >= 80:
            self.count = 0
        if self.count < 40:
            self.enemy_image = self.images[0]
            self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
        elif 40 <= self.count <= 80:
            self.enemy_image = self.images[1]
            self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
        self.count += 1

        return self.enemy, self.enemy_image
    # NOTE: need two animations bc when goomba move to the right, there's no image 3 and 4

    def animation4(self, timer=80):    # constant 2 frame animation forward and backward images
        if self.vel_x < 0:
            if self.count >= timer:
                self.count = 0
            if self.count < timer/2:
                self.enemy_image = self.images[0]
                self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
            elif timer/2 <= self.count <= timer:
                self.enemy_image = self.images[1]
                self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
        elif self.vel_x > 0:
            if self.count >= timer:
                self.count = 0
            if self.count < timer/2:
                self.enemy_image = self.images[2]
                self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
            elif timer/2 <= self.count <= timer:
                self.enemy_image = self.images[3]
                self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))

        self.count += 1

    def dying_animation(self):
        self.enemy_image = self.images[0]
        self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
        self.enemy = pygame.transform.rotate(self.enemy, 180)

    def draw(self):  # all
        self.screen.blit(self.enemy, self.enemy_rect)

    def move(self):  # move left
        if self.count % 5 == 0:
            self.enemy_rect.x += self.vel_x

        # Add code for moving opposite direction when colliding with obstacles
        # Or maybe make move right a separate function..

    def move_path_x(self, left, right):  # koopa, flying koopa
        # left = furthest left x value of path
        # right = furthest right x value of path

        if self.count % 5 == 0:
            self.enemy_rect.x += self.vel_x
            if self.enemy_rect.x < left:
                self.vel_x *= -1
            elif self.enemy_rect.x > right:
                self.vel_x *= -1
        # doesn't need count bc animation has count

    def move_path_y(self, top, bot):  # flying koopa
        # left = furthest left x value of path
        # right = furthest right x value of path

        if self.count % 10 == 0:
            self.enemy_rect.y += self.vel_y
            if self.enemy_rect.y < bot:
                self.vel_y *= -1
            if self.enemy_rect.y > top:
                self.vel_y *= -1
        # doesn't need count bc animation has count

    def fall(self):
        if self.falling and not self.on_ground:
            self.enemy_rect.y += self.vel_y

    def dies(self):
        self.enemy_rect.y += self.vel_y

    def reset_position(self):
        if self.enemy_rect.y >= 385 and not self.dead:
            self.enemy_rect.y = 385
            self.vel_y = 0
            self.on_ground = True
            self.falling = False
        elif self.enemy_rect.y < 385:
            self.falling = True
            self.on_ground = False

    def grounded(self):
        self.fall()
        self.reset_position()


# Not sure what I should do with enemy types of different colors yet...inherit from the enemy type class?
class Goomba(Enemy):
    def __init__(self, screen, pos, enemy_type):
        super().__init__(screen, pos, 32, 32, 20, 1)
        self.enemy_type = enemy_type  # overworld [1], cave [2], castle [3]

        if self.enemy_type == 1:
            self.images = [pygame.image.load("images/goomba_1.png"), pygame.image.load("images/goomba_2.png"),
                           pygame.image.load("images/goomba_3.png"), pygame.image.load("images/goomba_4.png")]
        elif self.enemy_type == 2:
            self.images = [pygame.image.load("images/dark_goomba_1.png"), pygame.image.load("images/dark_goomba_2.png"),
                           pygame.image.load("images/dark_goomba_3.png")]
        elif self.enemy_type == 3:
            self.images = [pygame.image.load("images/gray_goomba_1.png"), pygame.image.load("images/gray_goomba_2.png"),
                           pygame.image.load("images/gray_goomba_3.png")]

        self.rect = self.enemy_rect

    def update(self):
        self.draw()
        if self.is_move and not self.killed_mario:
            self.animation2()
            self.move()
            self.grounded()
        elif self.dead and not self.killed_mario:
            self.dying_animation()
            self.dies()


class KoopaTroopa(Enemy):
    def __init__(self, screen, pos, enemy_type, enemy_path=(0, 0)):
        super().__init__(screen, pos, 30, 35, 20, enemy_type)
        self.enemy_type = enemy_type  # green [1], red [2], dark [3]
        # path for red koopa
        self.path_left, self.path_right = enemy_path
        self.move_shell = False

        if self.enemy_type == 1:
            self.images = [pygame.image.load("images/green_koopa_1.png"), pygame.image.load("images/green_koopa_2.png"),
                           pygame.image.load("images/green_koopa_3.png"), pygame.image.load("images/green_koopa_4.png"),
                           pygame.image.load("images/green_koopa_5.png"), pygame.image.load("images/green_koopa_6.png")]
        elif self.enemy_type == 2:
            self.images = [pygame.image.load("images/red_koopa_1.png"), pygame.image.load("images/red_koopa_2.png"),
                           pygame.image.load("images/red_koopa_3.png"), pygame.image.load("images/red_koopa_4.png"),
                           pygame.image.load("images/red_koopa_5.png"), pygame.image.load("images/red_koopa_6.png")]
        elif self.enemy_type == 3:
            self.images = [pygame.image.load("images/dark_koopa_1.png"), pygame.image.load("images/dark_koopa_2.png"),
                           pygame.image.load("images/dark_koopa_3.png"), pygame.image.load("images/dark_koopa_4.png"),
                           pygame.image.load("images/dark_koopa_5.png"), pygame.image.load("images/dark_koopa_6.png")]

        self.rect = self.enemy_rect

    def shell_animation(self):
        if self.vel_x < 0:
            if self.count >= 80:
                self.count = 0
            if self.count < 40:
                self.enemy_image = self.images[4]
                self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
            elif 40 <= self.count <= 80:
                self.enemy_image = self.images[5]
                self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
        self.count += 1

    def shell_move(self):

        pass
        # after it dies, animation goes to the shell and can destroy enemies...how to do this..
        # movement is based on which direction mario pushes the shell

    def pickMovement(self):
        if (self.path_left and self.path_right) == 0:
            self.move()
        else:
            self.move_path_x(self.path_left, self.path_right)

    def update(self):
        # motion for green koopa
        self.draw()
        if self.is_move and not self.killed_mario:
            self.animation4()
            self.pickMovement()
        if self.dead and not self.killed_mario:
            self.dying_animation()
            self.fall()


class PiranhaPlant(Enemy):
    def __init__(self, screen, pos, enemy_type, enemy_path):  # TAKE IN MARIO AS PARAMETER
        super().__init__(screen, pos, 32, 32, 20, 1)
        self.top, self.bot = enemy_path  # change to path tuple
        self.enemy_type = enemy_type  # overworld [1], cave [2]

        if self.enemy_type == 1:
            self.images = [pygame.image.load("images/piranha_plant_1.png"),
                           pygame.image.load("images/piranha_plant_2.png")]
        elif self.enemy_type == 2:
            self.images = [pygame.image.load("images/dark_piranha_plant_1.png"),
                           pygame.image.load("images/dark_piranha_plant_2.png")]

        self.rect = self.enemy_rect

    def update(self):
        # HOW DO I MAKE IT NOT MOVE IF mario is adjacent(?) to pipe or on top(?) of the pipe??
        self.draw()
        # if self.is_move and not self.killed_mario:
        #     self.animation2()
        #     self.move_path_y(self.top, self.bot)
        # if self.dead and not self.killed_mario:
        #     self.dying_animation()
        #     self.fall()


class KoopaParatroopa(Enemy):
    def __init__(self, screen, pos, enemy_type, enemy_path):
        super().__init__(screen, pos, 25, 30, 20, 1)
        self.start, self.end = enemy_path  # change to path tuple
        self.enemy_type = enemy_type  # green [1], red [2]

        if self.enemy_type == 1:
            self.images = [pygame.image.load("images/green_koopa_patroopa_1.png"),
                           pygame.image.load("images/green_koopa_patroopa_2.png"),
                           pygame.image.load("images/green_koopa_7.png")]
        elif enemy_type == 2:
            self.images = [pygame.image.load("images/red_koopa_patroopa_1.png"),
                           pygame.image.load("images/red_koopa_patroopa_2.png"),
                           pygame.image.load("images/red_koopa_7.png")]

        self.rect = self.enemy_rect

    def dying_animation(self):
        self.enemy_image = self.images[2]
        self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
        # check if this works

    def update(self):
        self.draw()
        # if self.is_move and not self.killed_mario:
        #     self.animation2()
        #     self.move_path_y(self.start, self.end)
        # if self.dead and not self.killed_mario:
        #     self.dying_animation()
        #     self.fall()


class Blooper(Enemy):
    def __init__(self, screen, pos):
        super().__init__(screen, pos, 20, 30, 20, 1)  # group type may change

        self.images = [pygame.image.load("images/blooper_1.png"), pygame.image.load("images/blooper_2.png")]

        self.rect = self.enemy_rect

    def swim_after_mario(self):
        if self.count == 80:
            self.count = 0
        if self.count % 2 == 0:
            self.enemy_rect.y -= self.velY
            if self.count % 2 == 0 and self.velY > 0:
                self.enemy_rect.x += self.vel_x
            if abs(self.Y - self.enemy_rect.y) == 60:
                self.velY = self.velY * -1
        self.count += 1
        # MAKE IT FOLLOW MARIO

    def animation2(self, timer=480):  # blooper
        if self.velY > 0:
            self.enemy_image = self.images[0]
            self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
        elif self.velY < 0:
            self.enemy_image = self.images[1]
            self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height - 10))
        return self.enemy, self.enemy_image

    def update(self):
        self.draw()
        # if self.is_move and not self.killed_mario:
        #     self.animation2()
        #     self.swim_after_mario()
        # if self.dead and not self.killed_mario:
        #     self.dying_animation()
        #     self.fall()


class CheepCheep(Enemy):
    def __init__(self, screen, pos):
        super().__init__(screen, pos, 20, 20, 20, 1)
        self.move_type = random.choice[1, 2]  # straight [1], wavy [2]

        self.images = [pygame.image.load("images/red_cheep_cheep_1.png"),
                       pygame.image.load("images/red_cheep_cheep_2.png")]

        self.rect = self.enemy_rect

    def swim_wavy(self):  # cheep cheep
        if self.count % 15 == 0:
            self.enemy_rect.y += self.vel_y
            if abs(self.enemy_rect.y - self.Y) > 10:
                self.vel_y *= -1
        self.move()

    def pickMovement(self):
        if self.move_type == 1:
            self.move()
        if self.move_type == 2:
            self.swim_wavy()

    def update(self):
        self.draw()
        # if self.is_move and not self.killed_mario:
        #     self.animation2()
        #     self.pickMovement()
        # if self.dead and not self.killed_mario:
        #     self.dying_animation()
        #     self.fall()


class Podoboo(Enemy):  # NO DYING ANIMATION??
    def __init__(self, screen, pos, enemy_path):  # change to path tuple
        super().__init__(screen, pos, 20, 20, 20, 1)
        self.top, self.bot = enemy_path
        self.images = [pygame.image.load("images/podoboo_1.png"), pygame.image.load("images/podoboo_2.png")]

        self.rect = self.enemy_rect

    def move(self):  # podoboo
        # podoboo movement -> up and down
        # top = highest point it will reach
        # bot = lowest point it will reach
        if self.count == 80:
            self.count = 0
        if self.count % 2 == 0:
            self.enemy_rect.y += self.vel_y
            if self.enemy_rect.y < self.bot:
                self.vel_y *= -1
            if self.enemy_rect.y > self.top:
                self.vel_y *= -1
        self.count += 1  # needs count bc animation is based on velocity

    def animation2(self, timer=480):  # podoboo
        if self.vel_y < 0:
            self.enemy_image = self.images[0]
            self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
        elif self.vel_y > 0:
            self.enemy_image = self.images[1]
            self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
        return self.enemy, self.enemy_image

    def update(self):
        self.draw()
        # if self.is_move and not self.killed_mario:
        #     self.animation2()
        #     self.move()
        # if self.dead and not self.killed_mario:
        #     self.dying_animation()
        #     self.fall()


class FireBar(Enemy):  # NO DYING ANIMATION???
    def __init__(self, screen,  pos, radius):
        super().__init__(screen, pos, 13, 13, 20, 3)
        self.degree = 0
        self.center_rot_x = pos[0]
        self.center_rot_y = pos[1]
        self.angle = radians(5)
        self.radius = radius
        self.omega = 0.1  # angular velocity
        self.x = 0
        self.y = 0

        self.image = pygame.image.load("images/firebar_1.png")

        self.rect = self.enemy_rect  # FIX .-. doesn't work for collision
        # self.rect.x = self.x
        # self.rect.y = self.y

    def animation(self, timer=80):
        if self.degree <= -360:
            self.degree = 0
        if self.count >= timer:
            self.count = 0
        if self.count % 2 == 0:
            self.enemy_image = self.image
            self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
            self.enemy = pygame.transform.rotate(self.enemy, self.degree)
        self.count += 1
        self.degree -= 3
        return self.enemy, self.enemy_image

    def rotate(self):
        if self.angle > radians(360):
            self.angle = 0
        if self.count % 10 == 0:
            self.x = self.center_rot_x + self.radius * math.cos(self.angle)  # centerX + radius_Xcomp
            self.y = self.center_rot_y + self.radius * math.sin(self.angle)  # centerY + radius_Ycomp
        self.angle -= radians(0.4)  # rotates counterclockwise

        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.enemy, (self.x, self.y))

    def update(self):
        self.draw()
        # if self.is_move and not self.killed_mario:
        #     self.animation()
        #     self.rotate()
        # if self.dead and not self.killed_mario:
        #     self.dying_animation()
        #     self.fall()


class FakeBowser(Enemy):
    def __init__(self, screen, pos, enemy_type):
        super().__init__(screen, pos, 20, 20, 20, 1)  # group type may change
        # dies as goomba 1-4 and koopa 2-4
        self.enemy_type = enemy_type

        self.images = [pygame.image.load("images/bowser_1.png"), pygame.image.load("images/bowser_2.png"),
                       pygame.image.load("images/gray_goomba_4.png"), pygame.image.load("images/green_koopa_7.png")]

        self.rect = self.enemy_rect

    def fire_attack(self):
        pass
        # bowser jumps and shoots fire
        # fire goes to mario's Y position and goes towards him

    def jump(self):
        pass

    def dying_animation(self):
        pass

    def update(self):
        pass


class Fire(Sprite):
    def __init__(self):
        super().__init__()
        self.images = [pygame.image.load("images/fire_atk_1.png"), pygame.image.load("images/fire_atk_2.png"),
                       pygame.image.load("images/fire_atk_3.png"), pygame.image.load("images/fire_atk_4.png")]

        self.vel = 2
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.width = 16
        self.height = 8
        self.count = 0
        self.fire = self.animation()

    def animation(self):
        if self.vel < 0:
            if self.count >= 80:
                self.count = 0
            if self.count < 40:
                self.image = self.images[0]
                self.fire = pygame.transform.scale(self.image, (self.width, self.height))
            elif 40 <= self.count <= 80:
                self.image = self.images[1]
                self.fire = pygame.transform.scale(self.image, (self.width, self.height))
        elif self.vel > 0:
            if self.count >= 80:
                self.count = 0
            if self.count < 40:
                self.image = self.images[2]
                self.fire = pygame.transform.scale(self.image, (self.width, self.height))
            elif 40 <= self.count <= 80:
                self.image = self.images[3]
                self.fire = pygame.transform.scale(self.image, (self.width, self.height))
        self.count += 1
        return self.fire

    def update(self):
        pass
