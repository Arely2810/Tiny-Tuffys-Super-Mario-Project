import pygame
# from pygame.sprite import Sprite


# Will make into sprite later...not sure how to add sprite to group (kept saying error)
class Enemy:
    def __init__(self, x, y, width, height, enemy_type):
        # super().__init__(Enemy)
        self.count = 0
        self.vel = -3
        self.width = width
        self.height = height
        self.enemy_type = enemy_type

        self.dead = False

        # NOTE: not sure if I should keep the images here or move it to enemy type classes
        #       or move it to settings if we have a settings..
        # Animation frames are based on enemy types
        if self.enemy_type == 1:
            self.images = [pygame.image.load("images/goomba_1.png"), pygame.image.load("images/goomba_2.png"),
                           pygame.image.load("images/goomba_3.png")]
        elif self.enemy_type == 2:
            self.images = [pygame.image.load("images/green_koopa_1.png"), pygame.image.load("images/green_koopa_2.png"),
                           pygame.image.load("images/green_koopa_3.png"), pygame.image.load("images/green_koopa_4.png")]
        # Insert other enemy type images here
        else:
            self.images = []

        self.enemy, self.enemy_image = self.animation()
        self.enemy_rect = self.enemy.get_rect()
        self.enemy_rect.x = x
        self.enemy_rect.y = y

    def animation(self):    # animation for enemies with 2 frame movements
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

    def dying_animation(self):
        pass
        # Will have different dying animations based on enemy type and how it died

    def draw(self, screen):
        self.animation()
        screen.blit(self.enemy, self.enemy_rect)

    def move(self):  # Only moves left for now
        if self.count % 120 == 0:
            if self.vel < 0:
                self.enemy_rect.x += self.vel

        # Add code for moving opposite direction when colliding with obstacles
        # Or maybe make move right a separate function..

    def move2(self):  # podoboo movement -> up and down
        pass

    def swim_cheep(self):  # Sprite movement for cheep cheep
        pass
        # some cheep cheep swims straight -> call self.move()
        # write code for wavy swim movement
        # move to cheep cheep class????

    def swim_blooper(self):  # Sprite movement for blooper
        pass
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
    """Type 1 Enemy"""
    def __init__(self, x, y):
        super().__init__(x, y, 20, 20, 1)

    def drawMe(self, screen):
        self.draw(screen)
        self.move()


class Koopa_Troopa(Enemy):
    """Type 2 Enemy"""
    def __init__(self, x, y):
        super().__init__(x, y, 25, 30, 2)

    def shell_move(self):
        pass
        # after it dies, animation goes to the shell and can destroy enemies

    def drawMe(self, screen):
        self.draw(screen)
        self.move()
        if self.dead:
            self.dying_animation()

# Add class Piranha plant -> type 3
# Add class Koopa Paratroopa -> type 4
# Add class Blooper -> type 5
# Add class Cheep Cheep -> type 6
# Add class Podoboo -> type 7
# Add class Fire Bar -> type 8
# Add class Fake Bowser -> type 9
    # dies as goomba 1-4 and koopa 2-4
