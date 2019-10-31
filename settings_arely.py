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
        self.fireballs_allowed = 2
        self.fireball_speed = 4
        # deal with enemy settings later
        self.mario_speed = 3
        self.mario_jump_speed = 5
        self.level = 1        #Sounds
        self.one_up = pygame.mixer.Sound('Audio/Sounds/1up.wav')
        self.big_jump = pygame.mixer.Sound('Audio/Sounds/BigJump.wav')
        self.bump = pygame.mixer.Sound('Audio/Sounds/Bump.wav')
        self.destroy_brick = pygame.mixer.Sound('Audio/Sounds/DestroyBrick.wav')
        self.fireball = pygame.mixer.Sound('Audio/Sounds/Fireball.wav')
        self.fireworks = pygame.mixer.Sound('Audio/Sounds/Fireworks.wav')
        self.flagpole = pygame.mixer.Sound('Audio/Sounds/Flagpole.wav')
        self.got_coin = pygame.mixer.Sound('Audio/Sounds/GotCoin.wav')
        self.grow_vine = pygame.mixer.Sound('Audio/Sounds/GrowVine.wav')
        self.kick = pygame.mixer.Sound('Audio/Sounds/Kick.wav')
        self.pause = pygame.mixer.Sound('Audio/Sounds/Pause.wav')
        self.power_up = pygame.mixer.Sound('Audio/Sounds/PowerUp.wav')
        self.small_jump = pygame.mixer.Sound('Audio/Sounds/SmallJump.wav')
        self.spawn_power_up = pygame.mixer.Sound('Audio/Sounds/SpawnPowerUp.wav')
        self.stomp = pygame.mixer.Sound('Audio/Sounds/Stomp.wav')
        self.travel_pipe = pygame.mixer.Sound('Audio/Sounds/TravelPipe.wav')
        
        #Entity positions and types

        #Level 1
        block_position1 = [(512,288),(640,288),(672,288), (704, 288), (736, 288),(768, 288),(704, 160)]
        block_type1 = [3, 1, 3, 1, 3, 1, 3]
        block_items1 = [1, 0, 2, 0, 1, 0, 1]
        pipe_position1 = [(896, 352),(1184,320)]
        pipe_size1 = [0,1]
        #Level 2
        block_position2 = [(50,50), (100, 50,),(400, 50)]
        block_type2 = [3, 3, 4]
        block_items2 = [2, 1, 1]

        #index variables
        self.current_level = 0
        self.current_block = 0
        self.current_pipe = 0

        self.number_of_blocks = [7, 3]
        self.number_of_pipes = [2]
        self.pipe_positions = [pipe_position1]
        self.pipe_sizes = [pipe_size1]
        self.block_types = [block_type1,block_type2]
        self.block_positions = [block_position1, block_position2]
        self.block_items = [block_items1, block_items2]
        

    def initialize_dynamic_settings(self):
        self.mario_speed = 1.5
        self.mario_jump_speed = 1.5
        # deal with enemy later

    def dims(self):
        return self.screen_width, self.screen_height
   
