import pygame
from pygame.sprite import Sprite

class Block(Sprite):
    normal_block_image = pygame.image.load('images/normal_block.png')
    alternate_block_image = pygame.image.load('images/alternate_block.png')
    normal_question_image = [pygame.image.load('images/normal_question1.png'), pygame.image.load('images/normal_question2.png'), pygame.image.load('images/normal_question3.png')]
    alternate_question_image = [pygame.image.load('images/alternate_question.png'), pygame.image.load('images/alternate_question2.png'), pygame.image.load('images/alternate_question3.png')]
    empty_block_image = pygame.image.load('images/empty_block.png')
    invisible_block_image = pygame.image.load('images/invisible_block.png')
    broken_brick_image = [pygame.image.load('images/broken1.png'), pygame.image.load('images/broken2.png'), pygame.image.load('images/broken3.png')]

    def __init__(self, pos, background, type=0):
        super(Block, self).__init__()
        self.type = type
        self.pos = pos
        self.background = background
        timer = 0
        broken = False      #Default False, True when block is hit by big mario and contains no item
        emptied = False     #Default False, True when no more items/coins are available
        breaking = 0
        self.image = invisible_block_image
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def update(self):
        if background.scrolling:
            self.x -= 1
            self.rect.x = self.x
        if self.timer == 240:
            self.timer = 0

        if not self.broken and not self.emptied:
            if self.type == 1:
                self.image = normal_block_image
            if self.type == 2:
                self.image = alternate_block_image
            if self.type == 3 and self.timer < 120:
                self.image = self.normal_question_image[0]
            if self.type == 3 and (self.timer >= 120 and self.timer < 150) or (self.timer >= 210 and self.timer < 240):
                self.image = self.normal_question_image[1]
            if self.type == 3 and (self.timer >= 150 and self.timer <210):
                self.image = self.normal_question_image[2]
            if self.type == 4 and self.timer < 120:
                self.image = self.alternate_question_image[0]
            if self.type == 4 and (self.timer >= 120 and self.timer < 150) or (self.timer >= 210 and self.timer < 240):
                self.image = self.alternate_question_image[1]
            if self.type == 4 and (self.timer >= 150 and self.timer < 210):
                self.image = self.alternate_question_image[2]
            elif self.emptied:
                self.image = self.empty_block_image
        elif self.broken:
            self.destroy()

        self.timer += 1

    def destroy(self):
        #play animation of brick getting destroyed when big mario jumps into it
        if breaking < 30:
            self.image = broken_brick_image[0]
        if breaking < 60:
            self.iamge = broken_brick_image[1]
        if breaking < 90:
            self.image = broken_brick_image[2]
        else:
            self.kill()
        self.breaking += 1




