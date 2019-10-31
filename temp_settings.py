# TEST CODE
import pygame


class Settings:
    def __init__(self):
        # display screen settings
        self.screen_width = 1000
        self.screen_height = 480
        self.display_screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.start_scrolling_pos_x = self.screen_width // 2  # half of the display screen

        self.FPS = 500  # frames per second

        # background settings
        self.bg_image = pygame.image.load("SuperMarioBrosMap.png").convert()
        self.bg_width, self.bg_height = self.bg_image.get_rect().size
        self.bg_x = 0
        self.bg_y = 0

    def bg_position(self):
        return self.bg_x, self.bg_y

    def screen_dims(self):
        return self.screen_width, self.screen_height
