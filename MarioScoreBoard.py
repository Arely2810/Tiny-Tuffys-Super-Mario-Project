import pygame
import pygame.font


class ScoreBoard:

    def __init__(self, screen):
        self.score = 0
        self.time = 400
        self.lives = 3
        self.world = 1
        self.level = 1
        self.coins = 0
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # self.font_name = pygame.font.match_font('mario font 256')
        self.white = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.center_x = 250

        self.setup_score()

    ''' self.setup_time()
        self.setup_world()
        self.setup_coins()
        self.setup_lives()'''

    def enemy_killed(self, enemy_type):
        if enemy_type == 'turtle':
            self.score = self.score + 400
        elif enemy_type == 'brown_guy':
            self.score = self.score + 200

    def item_collected(self, item_type):
        if item_type == 'coin':
            self.score = self.score + 200
            self.coins = self.coins + 1
        elif item_type == 'mushroom':
            self.score = self.score + 1000

    def mario_killed(self, died):
        if died:
            self.lives = self.lives - 1
        elif not died:
            self.lives = self.lives

    def timer_countdown(self, mario_x):
        while mario_x != 14036:
            self.time = self.time - 1

    def setup_score(self):
        score = self.score
        score_str = "Score: {}".format(score)
        score_image = self.font.render(score_str, True, self.white)

        score_rect = score_image.get_rect()
        score_rect.center = self.screen_rect.center
        score_rect.top = score_rect.top

    '''def setup_time(self):
        time = self.time
        time_str = "Time: {}".format(time)
        self.screen.draw.text((190, 50), time_str, self.white)
        self.screen.update()

    def setup_world(self):
        world = self.world
        level = self.level
        world_str = "World: {}-{}".format(world, level)
        self.screen.draw.text((290, 50), world_str, self.white)
        self.screen.update()

    def setup_coins(self):
        coins = self.coins
        coins_str = "Coins: {}".format(coins)
        self.screen.draw.text((390, 50), coins_str, self.white)
        self.screen.update()

    def setup_lives(self):
        lives = self.lives
        lives_str = "Lives: {}".format(lives)
        self.screen.draw.text((490, 50), lives_str, self.white)
        self.screen.update()'''
