import pygame
import math
from math import *
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, screen, pos, width, height):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.count = 0
        self.count2 = 0
        self.vel = -1  # negative bc sprite will most likely be moving left
        self.velY = 2
        self.width = width  # width of sprite
        self.height = height  # height of sprite
        self.dead = False

        # default image...images can be overwrite in other classes...how do i do empty image here???
        self.images = [pygame.image.load('images/goomba_1.png'), pygame.image.load('images/goomba_2.png')]
        self.enemy, self.enemy_image = self.animation2()
        self.enemy_rect = self.enemy.get_rect()
        self.enemy_rect.x = pos[0]  # x
        self.enemy_rect.y = pos[1]  # y

        self.X = pos[0]
        self.Y = pos[1]

    def animation2(self, timer=80):  # constant 2 frame animation forward
        if self.vel < 0:
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
    # NOTE: need two animation bc when goomba move to the right, there's no image 3 and 4

    def animation4(self, timer=80):    # constant 2 frame animation forward and backward images
        if self.vel < 0:
            if self.count >= timer:
                self.count = 0
            if self.count < timer/2:
                self.enemy_image = self.images[0]
                self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
            elif timer/2 <= self.count <= timer:
                self.enemy_image = self.images[1]
                self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
        elif self.vel > 0:
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
        # if self.dead:
        self.enemy_image = self.images[0]
        self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
        self.enemy = pygame.transform.rotate(self.enemy, 180)

    def draw(self):  # all
        self.screen.blit(self.enemy, self.enemy_rect)

    def move(self):  # move left
        if self.count % 5 == 0:
            self.enemy_rect.x += self.vel

        # Add code for moving opposite direction when colliding with obstacles
        # Or maybe make move right a separate function..

    def move_path_x(self, left, right):  # koopa, flying koopa
        # left = furthest left x value of path
        # right = furthest right x value of path

        if self.count % 5 == 0:
            self.enemy_rect.x += self.vel
            if self.enemy_rect.x < left:
                self.vel *= -1
            elif self.enemy_rect.x > right:
                self.vel *= -1
        # doesn't need count bc animation has count

    def move_path_y(self, top, bot):  # flying koopa
        # left = furthest left x value of path
        # right = furthest right x value of path

        if self.count % 10 == 0:
            self.enemy_rect.y += self.velY
            if self.enemy_rect.y < bot:
                self.velY *= -1
            if self.enemy_rect.y > top:
                self.velY *= -1
        # doesn't need count bc animation has count

    def fall(self):  # if hit by fire ball
        if self.count > 80:
            self.count = 0
        if self.count % 2 == 0:
            self.enemy_rect.y += self.velY
        self.count += 1

    def is_grounded(self):
        pass
        # will not apply for underwater level and koopa paratroopas
        # Will try to implement when ground sprite is made
        # Use sprite collision to check
        # if enemy sprite is not on ground then make it fall down

    def hit_mario(self):
        pass
        # checks for side of sprite collision with mario

    def is_dead(self):
        pass
        # checks for top of sprite collision with bottom of mario
        # checks for collision with fire ball
        # return self.dead


# Not sure what I should do with enemy types of different colors yet...inherit from the enemy type class?
class Goomba(Enemy):
    def __init__(self, screen, pos, enemy_type):
        super().__init__(screen, pos, 32, 32)
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

    def update(self):
        self.draw()
        self.animation2()
        self.move()
        if self.dead:
            self.dying_animation()
            self.fall()


class KoopaTroopa(Enemy):
    def __init__(self, screen, pos, enemy_type, left=0, right=0):
        super().__init__(screen, pos, 30, 35)
        self.enemy_type = enemy_type  # green [1], red [2], dark [3]
        # path for red koopa
        self.path_left = left
        self.path_right = right

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

    def shell_animation(self):
        if self.vel < 0:
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
        self.animation4()
        self.pickMovement()
        if self.dead:
            self.dying_animation()


class PiranhaPlant(Enemy):
    def __init__(self, screen, pos, enemy_type, top, bot):  # TAKE IN MARIO AS PARAMETER
        super().__init__(screen, pos, 32, 32)
        self.top, self.bot = top, bot  # change to path tuple
        self.enemy_type = enemy_type  # overworld [1], cave [2]

        if self.enemy_type == 1:
            self.images = [pygame.image.load("images/piranha_plant_1.png"),
                           pygame.image.load("images/piranha_plant_2.png")]
        elif self.enemy_type == 2:
            self.images = [pygame.image.load("images/dark_piranha_plant_1.png"),
                           pygame.image.load("images/dark_piranha_plant_2.png")]

    def update(self):
        self.draw()
        self.animation2()
        self.move_path_y(self.top, self.bot)
        # HOW DO I MAKE IT NOT MOVE IF mario is adjacent(?) to pipe or on top(?) of the pipe??


class KoopaParatroopa(Enemy):
    def __init__(self, screen, pos, enemy_type, start, end):
        super().__init__(screen, pos, 25, 30)
        self.start, self.end = start, end  # change to path tuple
        self.enemy_type = enemy_type  # green [1], red [2]

        if enemy_type == 1:
            self.images = [pygame.image.load("images/green_koopa_patroopa_1.png"),
                           pygame.image.load("images/green_koopa_patroopa_2.png"),
                           pygame.image.load("images/green_koopa_patroopa_3.png"),
                           pygame.image.load("images/green_koopa_patroopa_4.png")]  # check if we need image 3 and 4
        elif enemy_type == 2:
            self.images = [pygame.image.load("images/red_koopa_patroopa_1.png"),
                           pygame.image.load("images/red_koopa_patroopa_2.png"),
                           pygame.image.load("images/red_koopa_patroopa_3.png"),
                           pygame.image.load("images/red_koopa_patroopa_4.png")]

    def dying_animation(self):
        pass

    def update(self):
        self.draw()
        self.animation2()
        self.move_path_y(self.start, self.end)  # DO THESE MOVE UP AND DOWN. CHECK.


class Blooper(Enemy):
    def __init__(self, screen, pos):
        super().__init__(screen, pos, 20, 30)

        self.images = [pygame.image.load("images/blooper_1.png"), pygame.image.load("images/blooper_2.png")]

    def swim_after_mario(self):
        if self.count == 80:
            self.count = 0
        if self.count % 2 == 0:
            self.enemy_rect.y -= self.velY
            if self.count % 2 == 0 and self.velY > 0:
                self.enemy_rect.x += self.vel
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
        self.swim_after_mario()
        self.animation2()


class CheepCheep(Enemy):
    def __init__(self, screen, pos, move_type):
        super().__init__(screen, pos, 20, 20)
        self.move_type = move_type  # straight [1], wavy [2]

        self.images = [pygame.image.load("images/red_cheep_cheep_1.png"),
                       pygame.image.load("images/red_cheep_cheep_2.png")]

    def swim_wavy(self):  # cheep cheep
        if self.count % 15 == 0:
            self.enemy_rect.y += self.velY
            if abs(self.enemy_rect.y - self.Y) > 10:
                self.velY *= -1
        self.move()

    def pickMovement(self):
        if self.move_type == 1:
            self.move()
        if self.move_type == 2:
            self.swim_wavy()

    def update(self):
        self.draw()
        self.animation2()
        self.pickMovement()


class Podoboo(Enemy):  # NO DYING ANIMATION??
    def __init__(self, screen, pos, top, bot):  # change to path tuple
        super().__init__(screen, pos, 20, 20)
        self.top, self.bot = top, bot
        self.images = [pygame.image.load("images/podoboo_1.png"), pygame.image.load("images/podoboo_2.png")]

    def move(self):  # podoboo
        # podoboo movement -> up and down
        # top = highest point it will reach
        # bot = lowest point it will reach
        if self.count == 80:
            self.count = 0
        if self.count % 2 == 0:
            self.enemy_rect.y += self.velY
            if self.enemy_rect.y < self.bot:
                self.velY *= -1
            if self.enemy_rect.y > self.top:
                self.velY *= -1
        self.count += 1  # needs count bc animation is based on velocity

    def animation2(self, timer=480):  # podoboo
        if self.velY < 0:
            self.enemy_image = self.images[0]
            self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
        elif self.velY > 0:
            self.enemy_image = self.images[1]
            self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
        return self.enemy, self.enemy_image

    def update(self):
        self.draw()
        self.animation2()
        self.move()


class FireBar(Enemy):  # NO DYING ANIMATION???
    def __init__(self, screen,  pos, radius):
        super().__init__(screen, pos, 13, 13)
        self.degree = 0
        self.center_rot_x = pos[0]
        self.center_rot_y = pos[1]
        self.angle = radians(5)
        self.radius = radius
        self.omega = 0.1  # angular velocity
        self.x = 0
        self.y = 0

        self.image = pygame.image.load("images/firebar_1.png")

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

    def draw(self):
        self.screen.blit(self.enemy, (self.x, self.y))

    def update(self):
        self.draw()
        self.animation()
        self.rotate()


class FakeBowser(Enemy):
    def __init__(self, screen, pos, enemy_type):
        super().__init__(screen, pos, 20, 20)
        # dies as goomba 1-4 and koopa 2-4
        self.enemy_type = enemy_type

        self.images = [pygame.image.load("images/bowser_1.png"), pygame.image.load("images/bowser_2.png"),
                       pygame.image.load("images/gray_goomba_4.png"), pygame.image.load("images/green_koopa_7.png")]

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
