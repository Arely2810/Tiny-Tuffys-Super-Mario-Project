import pygame


class Settings:
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 700

        # well deal with the background later
        # self.background = pygame.load['']
        self.mario_limit = 3
        self.fireball_width = 5
        self.fireball_height = 5
        self.fireballs_allowed = 3
        # deal with enemy settings later

    def initialize_dynamic_settings(self):
        self.mario_speed = 1.5
        self.mario_jump_speed = 2
        # deal with enemy later

    def dims(self):
        return self.screen_width, self.screen_height
