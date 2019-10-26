import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, screen, x, y, width, height):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.count = 0
        self.count2 = 0
        self.vel = -3  # negative bc sprite will most likely be moving left
        self.velY = 2
        self.width = width  # width of sprite
        self.height = height  # height of sprite
        self.dead = False
        self.moveleft = True

        # default image...images can be overwrite in other classes
        self.images = [pygame.image.load('images/goomba_1.png')]
        self.enemy, self.enemy_image = self.animation()
        self.enemy_rect = self.enemy.get_rect()
        self.enemy_rect.x = x
        self.enemy_rect.y = y

        self.Y = y

    def animation(self):
        if self.vel < 0:
            if self.count >= 480:
                self.count = 0
            if self.count < 240:
                self.enemy_image = self.images[0]
                self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
            elif 240 <= self.count <= 480:
                self.enemy_image = self.images[1]
                self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
        self.count += 1

        return self.enemy, self.enemy_image

    def animation_4(self):    # animation for enemies with 2 frame movements
        if self.vel < 0:
            if self.count >= 480:
                self.count = 0
            if self.count < 240:
                self.enemy_image = self.images[0]
                self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
            elif 240 <= self.count <= 480:
                self.enemy_image = self.images[1]
                self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
        elif self.vel > 0:
            if self.count >= 480:
                self.count = 0
            if self.count < 240:
                self.enemy_image = self.images[2]
                self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
            elif 240 <= self.count <= 480:
                self.enemy_image = self.images[3]
                self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))

        self.count += 1

    def animation_up_down1(self):  # podoboo
        if self.vel < 0:
            self.enemy_image = self.images[0]
            self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
        elif self.vel > 0:
            self.enemy_image = self.images[1]
            self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))

    def animation_up_down2(self):  # blooper
        if self.velY > 0:
            self.enemy_image = self.images[0]
            self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height))
        elif self.velY < 0:
            self.enemy_image = self.images[1]
            self.enemy = pygame.transform.scale(self.enemy_image, (self.width, self.height - 10))

    def dying_animation(self):
        pass
        # Will have different dying animations based how they die..

    def draw(self): # all
        self.screen.blit(self.enemy, self.enemy_rect)

    def move(self):  # Only moves left
        if self.count % 120 == 0:
            self.enemy_rect.x += self.vel

        # Add code for moving opposite direction when colliding with obstacles
        # Or maybe make move right a separate function..

    def move_left_right(self, left, right):  # IS THERE A BETTER WAY TO DO THIS??
        # red koopa -> stays on path without falling down edge
        # first moves towards the left
        # left = furthest left x value of path
        # right = furthest right x value of path

        if self.count % 120 == 0:
            self.enemy_rect.x += self.vel
            if self.enemy_rect.x < left:
                self.vel *= -1
            elif self.enemy_rect.x > right:
                self.vel *= -1

    def move_up_down(self, top, bot):
        # podoboo movement -> up and down
        # top = highest point it will reach
        # bot = lowest point it will reach
        if self.count % 80 == 0:
            self.enemy_rect.y += self.vel
            if self.enemy_rect.y < bot:  # These numbers are temporary, bc not sure how to decide when it should fall
                self.vel *= -1
            if self.enemy_rect.y > top:  # These numbers are temporary, bc not sure how to decide when it should fall
                self.vel *= -1
        self.count += 1

    def swim_wavy(self):  # Sprite movement for cheep cheep
        if self.count % 160 == 0:
            self.enemy_rect.y += self.velY
            if abs(self.enemy_rect.y - self.Y) > 16:
                self.velY *= -1
        self.move()

    def swim_after_mario(self):  # Sprite movement for blooper
        if self.count == 480:
            self.count = 0
        if self.count % 20 == 0:
            self.enemy_rect.y -= self.velY
            if self.count % 60 == 0 and self.velY > 0:
                self.enemy_rect.x += self.vel
            if abs(self.Y - self.enemy_rect.y) == 60:
                self.velY = self.velY * -1
        self.count += 1
        # follows Mario
        # swims diagonally up
        # drops straight down
        # move to blooper class???
        # requires different animation style..

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
    def __init__(self, screen, x, y, enemy_type):
        super().__init__(screen, x, y, 20, 20)
        self.enemy_type = enemy_type  # overworld [1], cave [2], castle [3]

        if self.enemy_type == 1:
            self.images = [pygame.image.load("images/goomba_1.png"), pygame.image.load("images/goomba_2.png"),
                           pygame.image.load("images/goomba_3.png")]
        elif self.enemy_type == 2:
            self.images = [pygame.image.load("images/dark_goomba_1.png"), pygame.image.load("images/dark_goomba_2.png"),
                           pygame.image.load("images/dark_goomba_3.png")]
        elif self.enemy_type == 3:
            self.images = [pygame.image.load("images/gray_goomba_1.png"), pygame.image.load("images/gray_goomba_2.png"),
                           pygame.image.load("images/gray_goomba_3.png")]

    def update(self):
        self.draw()
        self.animation()
        self.move()


class KoopaTroopa(Enemy):
    def __init__(self, screen, x, y, enemy_type, left=0, right=0):
        super().__init__(screen, x, y, 25, 30)
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

    def shell_move(self):
        pass
        # after it dies, animation goes to the shell and can destroy enemies

    def pickMovement(self):
        if (self.path_left and self.path_right) == 0:
            self.move()
        else:
            self.move_left_right(self.path_left, self.path_right)

    def update(self):
        # motion for green koopa
        self.draw()
        self.animation_4()
        self.pickMovement()
        if self.dead:
            self.dying_animation()


class PiranhaPlant(Enemy):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y, 20, 20)

        self.images = [pygame.image.load("images/piranha_plant_1.png"),
                       pygame.image.load("images/piranha_plant_2.png")]

    def update(self):
        pass


class KoopaParatroopa(Enemy):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y, 20, 20)

        self.images = [pygame.image.load("images/green_koopa_patroopa_1.png"),
                       pygame.image.load("images/green_koopa_patroopa_2.png")]

    def update(self):
        pass


class Blooper(Enemy):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y, 20, 30)

        self.images = [pygame.image.load("images/blooper_1.png"), pygame.image.load("images/blooper_2.png")]

    def update(self):
        self.draw()
        self.swim_after_mario()
        self.animation_up_down2()


class CheepCheep(Enemy):
    def __init__(self, screen, x, y, move_type):
        super().__init__(screen, x, y, 20, 20)
        self.move_type = move_type  # straight [1], wavy [2]

        self.images = [pygame.image.load("images/red_cheep_cheep_1.png"),
                       pygame.image.load("images/red_cheep_cheep_2.png")]

    def pickMovement(self):
        if self.move_type == 1:
            self.move()
        if self.move_type == 2:
            self.swim_wavy()

    def update(self):
        self.draw()
        self.animation()
        self.pickMovement()


class Podoboo(Enemy):
    def __init__(self, screen, x, y, top, bot):
        super().__init__(screen, x, y, 20, 20)
        self.top, self.bot = top, bot
        self.images = [pygame.image.load("images/podoboo_1.png"), pygame.image.load("images/podoboo_2.png")]

    def update(self):
        self.draw()
        self.animation_up_down1()
        self.move_up_down(self.top, self.bot)


class FireBar(Enemy):
    def __init__(self, screen,  x, y):
        super().__init__(screen, x, y, 20, 20)

        self.images = [pygame.image.load("images/fire_bar_1.png")]

    def update(self):
        pass


class FakeBowser(Enemy):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y, 20, 20)
    # dies as goomba 1-4 and koopa 2-4

        self.images = [pygame.image.load("images/bowser_1.png"), pygame.image.load("images/bowser_2.png")]

    def update(self):
        pass
