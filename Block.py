import pygame
from pygame.sprite import Sprite


class Block(Sprite):
    normal_block_image = pygame.image.load('images/normal_block.png')
    underground_block_image = pygame.image.load('images/underground_block.png')
    normal_question_image = [pygame.image.load('images/normal_question1.png'), pygame.image.load('images/normal_question2.png'), pygame.image.load('images/normal_question3.png')]
    underground_question_image = [pygame.image.load('images/underground_question1.png'), pygame.image.load('images/underground_question2.png'), pygame.image.load('images/underground_question3.png')]
    empty_block_image = [pygame.image.load('images/empty_block.png'), pygame.image.load('images/underground_empty_block.png')]
    invisible_block_image = pygame.image.load('images/invisible_block.png')
    hard_block_image = pygame.image.load('images/hard_block.png')
    underground_hard_block_image = pygame.image.load('images/underground_hard_block.png')
    broken_block_image = [pygame.image.load('images/broken1.png'), pygame.image.load('images/broken2.png'), pygame.image.load('images/broken3.png'), pygame.image.load('images/broken4.png')]
    broken_block_image2 = [pygame.image.load('images/ubroken1.png'), pygame.image.load('images/ubroken2.png'), pygame.image.load('images/ubroken3.png'), pygame.image.load('images/ubroken4.png')]

    def __init__(self, pos, screen, type=1, item=0):
        super(Block, self).__init__()
        self.type = type
        self.item = item
        self.pos = pos
        self.screen = screen
        self.timer = 0
        self.broken = False      #Default False, True when block is hit by big mario and contains no item
        self.emptied = False     #Default False, True when no more items/coins are available
        self.breaking = 0
        self.image = self.normal_block_image
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

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
            if (self.type == 3 and (self.timer >= 60 and self.timer < 80)) or (self.type == 3 and  (self.timer >= 100 and self.timer < 120)) and not self.emptied:
                self.image = self.normal_question_image[1]
            if self.type == 3 and (self.timer >= 80 and self.timer <100) and not self.emptied:
                self.image = self.normal_question_image[2]
            if self.type == 4 and self.timer < 120 and not self.emptied:
                self.image = self.underground_question_image[0]
            if (self.type == 4 and (self.timer >= 120 and self.timer < 150)) or (self.type == 4 and (self.timer >= 210 and self.timer < 240)) and not self.emptied:
                self.image = self.underground_question_image[1]
            if self.type == 4 and (self.timer >= 150 and self.timer < 210) and not self.emptied:
                self.image = self.underground_question_image[2]
            if self.type == 5:
                self.image = self.hard_block_image
            if self.type == 6:
                self.image = self.underground_hard_block_image
            if self.type == 7:
                self.image = self.invisible_block_image
            elif self.emptied:
                self.image = self.empty_block_image
        elif self.broken:
            self.destroy()

        self.timer += 1

    def destroy(self):
        #play animation of brick getting destroyed when big mario jumps into it
        if breaking < 20:
            self.image = broken_block_image[0]
        if breaking >= 20 and breaking < 40:
            self.iamge = broken_block_image[1]
        if breaking >= 40 and breaking < 60:
            self.image = broken_block_image[2]
        else:
            self.kill()
        self.breaking += 1

    def bumped(self):
        #play animation of brick getting hit if small mario jumps into it
        counter = 0
        while counter < 5:
            self.rect.y += 1
            counter += 1
        while counter > 0:
            self.rect.y -= 1




