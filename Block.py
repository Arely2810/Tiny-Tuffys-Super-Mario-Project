import pygame
from pygame.sprite import Sprite


class Block(Sprite):
    normal_block_image = pygame.image.load('images/normal_block.png')
    underground_block_image = pygame.image.load('images/underground_block.png')
    normal_question_image = [pygame.image.load('images/normal_question1.png'),
                             pygame.image.load('images/normal_question2.png'),
                             pygame.image.load('images/normal_question3.png')]
    underground_question_image = [pygame.image.load('images/underground_question1.png'),
                                  pygame.image.load('images/underground_question2.png'),
                                  pygame.image.load('images/underground_question3.png')]
    empty_block_image = [pygame.image.load('images/empty_block.png'),
                         pygame.image.load('images/underground_empty_block.png')]
    invisible_block_image = pygame.image.load('images/invisible_block.png')
    hard_block_image = pygame.image.load('images/hard_block.png')
    underground_hard_block_image = pygame.image.load('images/underground_hard_block.png')
    broken_block_image = [pygame.image.load('images/broken1.png'), pygame.image.load('images/broken2.png'),
                          pygame.image.load('images/broken3.png'), pygame.image.load('images/broken4.png')]
    broken_block_image2 = [pygame.image.load('images/ubroken1.png'), pygame.image.load('images/ubroken2.png'),
                           pygame.image.load('images/ubroken3.png'), pygame.image.load('images/ubroken4.png')]

    def __init__(self, pos, screen, type_=1, item=0):
        super(Block, self).__init__()
        self.type = type_
        # 0 = nothing, 1 = coin, 2 = mushroom/fireflower, 3 = one up shroom, 4 = star, # 5 = lots of coins
        self.item = item
        self.pos = pos
        self.screen = screen
        self.timer = 0
        self.broken = False  # Default False, True when block is hit by big mario and contains no item
        self.emptied = False  # Default False, True when no more items/coins are available
        self.breaking = 0
        self.image = self.normal_block_image
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.bump = False
        self.counter = 0
        self.y_original = self.pos[1]

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

        if self.timer == 120:
            self.timer = 0

        if not self.broken and not self.emptied:
            if self.type == 1:
                self.image = self.normal_block_image
            if self.type == 2:
                self.image = self.underground_block_image
            if self.type == 3 and self.timer < 60 and not self.emptied:
                self.image = self.normal_question_image[0]
            if (self.type == 3 and (60 <= self.timer < 80)) or (self.type == 3 and (100 <= self.timer < 120)) \
                    and not self.emptied:
                self.image = self.normal_question_image[1]
            if self.type == 3 and (80 <= self.timer < 100) and not self.emptied:
                self.image = self.normal_question_image[2]
            if self.type == 4 and self.timer < 120 and not self.emptied:
                self.image = self.underground_question_image[0]
            if (self.type == 4 and (120 <= self.timer < 150)) or (self.type == 4 and (210 <= self.timer < 240)) \
                    and not self.emptied:
                self.image = self.underground_question_image[1]
            if self.type == 4 and (150 <= self.timer < 210) and not self.emptied:
                self.image = self.underground_question_image[2]
            if self.type == 5:
                self.image = self.hard_block_image
            if self.type == 6:
                self.image = self.underground_hard_block_image
            if self.type == 7:
                self.image = self.invisible_block_image
            if self.type == 8:
                self.image = self.empty_block_image[0]
        elif self.emptied:
            self.image = self.empty_block_image[0]

        elif self.broken:
            self.destroy()

        if self.bump:
            self.bumped()

        self.timer += 1

    def destroy(self):
        # play animation of brick getting destroyed when big mario jumps into it
        if self.breaking < 20:
            self.image = self.broken_block_image[0]
        if 20 <= self.breaking < 40:
            self.image = self.broken_block_image[1]
        if 40 <= self.breaking < 60:
            self.image = self.broken_block_image[2]
        else:
            self.kill()
        self.breaking += 1

    def bumped(self):
        # play animation of brick getting hit if small mario jumps into it
        # counter = 0
        # while counter < 5:
        #     self.rect.y += 1
        #     counter += 1
        # while counter > 0:
        #     self.rect.y -= 1

        # while counter < 10:
        if self.counter < 10:
            self.y -= 2
        elif 5 < self.counter <= 20:
            self.y += 2
            if self.y > self.y_original:
                self.bump = False
                self.y = self.y_original
        # self.rect.y = self.y
        self.counter += 1

        if self.counter > 20:
            self.counter = 0

        #     print(self.rect.y)
        #     print(counter)
