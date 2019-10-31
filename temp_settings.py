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

        # blocks
        # Level 1
        block_position1 = [(512, 288), (640, 288), (672, 288), (704, 288), (736, 288), (768, 288), (704, 160)]
        block_type1 = [3, 1, 3, 1, 3, 1, 3]
        block_items1 = [1, 0, 2, 0, 1, 0, 1]
        pipe_position1 = [(896, 352), (1184, 320)]
        pipe_size1 = [0, 1]
        # Level 2
        block_position2 = [(50, 50), (100, 50,), (400, 50)]
        block_type2 = [3, 3, 4]
        block_items2 = [2, 1, 1]

        # index variables
        self.current_level = 0
        self.current_block = 0
        self.current_pipe = 0

        self.number_of_blocks = [7, 3]
        self.number_of_pipes = [2]
        self.pipe_positions = [pipe_position1]
        self.pipe_sizes = [pipe_size1]
        self.block_types = [block_type1, block_type2]
        self.block_positions = [block_position1, block_position2]
        self.block_items = [block_items1, block_items2]

    def bg_position(self):
        return self.bg_x, self.bg_y

    def screen_dims(self):
        return self.screen_width, self.screen_height
