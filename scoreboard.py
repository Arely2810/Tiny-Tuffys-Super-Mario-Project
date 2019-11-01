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
        self.white = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 25)
        self.center = (90, 50)

        self.setup_score()
        self.setup_time()
        self.setup_world()
        self.setup_coins()
        self.setup_lives()

        self.update_screen()

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
        self.score_image = self.font.render(score_str, True, self.white)

        self.score_rect = (10, 10)

    def setup_time(self):
        time = self.time
        time_str = "Time: {}".format(time)
        self.time_image = self.font.render(time_str, True, self.white)

        self.time_rect = (110, 10)

    def setup_world(self):
        world = self.world
        level = self.level
        world_str = "World: {}-{}".format(world, level)
        self.world_image = self.font.render(world_str, True, self.white)

        self.world_rect = (220, 10)

    def setup_coins(self):
        coins = self.coins
        coins_str = "Coins: {}".format(coins)
        self.coin_image = self.font.render(coins_str, True, self.white)

        self.coin_rect = (330, 10)

    def setup_lives(self):
        lives = self.lives
        lives_str = "Lives: {}".format(lives)
        self.lives_image = self.font.render(lives_str, True, self.white)

        self.lives_rect = (425, 10)

    def update_screen(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.time_image, self.time_rect)
        self.screen.blit(self.world_image, self.world_rect)
        self.screen.blit(self.coin_image, self.coin_rect)
        self.screen.blit(self.lives_image, self.lives_rect)
