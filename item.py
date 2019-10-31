import pygame
from pygame.sprite import Sprite

class Item(Sprite):
    def __init__(self):
        self.count = 0
        self.vel = 5
        self.yvel = 5
        self.popout_delay = 0

        #placeholder image
        self.image = pygame.image.load('images/super_mushroom.png')

class Coin(Item):
    coin_image = [pygame.image.load('images/coin1.png'), pygame.image.load('images/coin2.png'), pygame.image.load('images/coin3')]
    def __init__(self, pos, screen):
        super().__init__(pos, screen)
        self.image = coin_image
        self.pos = pos
        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def update(self):
        #movement
        self.rect.x = self.x
        self.rect.y = self.y

        if popout_delay < 30:
            self.y -= self.yvel
            self.popout_delay += 1
        elif popout_delay == 30:
            self.y += self.yvel
        elif self.y == self.pos[1]:
            self.kill()

        #animation
        if self.count == 60:
            self.count = 0
        if self.count < 20:
            self.image = self.coin_image[0]
        if (self.count >= 20 and self.count < 30) or (self.count >= 50 and self.count < 60):
            self.image = self.coin_image[1]
        if self.count >= 30 and self.count < 50:
            self.image = self.coin_image[3]




class Mushroom(Item):
    mushroom_image = pygame.image.load('images/super_mushroom.png')
    def __init__(self, pos, screen):
        super().__init__(pos, screen)
        self.image = mushroom_image
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.falling = False

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        if popout_delay < 32:
            self.y -= 1
        else:
            self.normal_movement()
        if self.y > 600:
            self.kill()

    def normal_movement(self):
        self.x += self.vel
        if falling:
            self.y += self.yvel

    def bumped(self):
        self.vel *= -1
        timer = 0
        while timer < 32:
            self.y +=1
            timer += 1
        self.falling = True

class OneUp(Item):
    one_up_image = pygame.image.load('images/one_up_shroom.png')
    def __init__(self, pos, screen):
        super().__init__(pos, screen)
        self.image = one_up_image
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.falling = False

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        if popout_delay < 32:
            self.y -= 1
        else:
            self.normal_movement()
        if self.y > 600:
            self.kill()

    def normal_movement(self):
        self.x += self.vel
        if falling:
            self.y += self.yvel

    def bumped(self):
        self.vel *= -1
        timer = 0
        while timer < 32:
            self.y += 1
            timer += 1
        self.falling = True

class FireFlower(Item):
    fire_flower_image = [pygame.image.load('images/fire_flower1.png'), pygame.image.load('images/fire_flower2.png'),pygame.image.load('images/fire_flower3.png'), pygame.image.load('images,fire_flower4.png')]
    def __init__(self, pos, screen):
        super(FireFlower, self).__init__()
        self.image = fire_flower_image
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

        #animation
        if self.counter == 60:
            self.counter = 0
        if self.count < 15:
            self.image = self.fire_flower_image[0]
        if self.count >= 15 and self.count < 30:
            self.image = self.fire_flower_image[1]
        if self.count >= 30 and self.count < 45:
            self.image = self.fire_flower_image[2]
        if self.count >= 45 and self.count < 60:
            self.image = self.fire_flower_image[3]


class Star(Item):
    star_image = [pygame.image.load('images/star1.png'), pygame.image.load('images/star2.png'),pygame.image.load('images/star3.png'), pygame.image.load('images/star4.png')]
    def __init__(self, pos, screen):
        super(Star, self).__init__()
        self.image = star_image
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        if popout_delay < 32:
            self.y -= 1
        else:
            self.normal_movement()

        if self.y > 600:
            self.kill()

        #animations
        if self.count == 60:
            self.count = 0
        if self.count < 15:
            self.image = self.star_image[0]
        if self.count >= 15 and self.count < 30:
            self.image = self.star_image[1]
        if self.count >= 30 and self.count < 45:
            self.image = self.star_image[2]
        if self.count >= 45 and self.count < 60:
            self.image = self.star_image[3]


    def normal_movement(self):
        self.x += self.vel
        self.y += self.yvel

