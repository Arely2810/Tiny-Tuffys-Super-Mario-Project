import pygame


class Settings:
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 480

        # well deal with the background later
         #Sounds
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
        block_position1 = [(512,288), (640,288), (672,288), (704, 288), (736, 288), (768, 288), (704, 160), (2048, 256), (2464, 288), (2496, 288), (2528, 288), (2560,288), (2592, 160), (2624, 160), (2656, 160), (2688, 160), (2720, 160), (2752, 160), (2782, 160), (2910, 160) ,(2942, 160), (2974,160), (3006, 160), (3006, 288), (3198, 288), (3230, 288) ,(3390, 288), (3486, 288), (3486, 160), (3582, 288), (3774, 288),(3870, 160), (3902, 160), (3934, 160), (4094, 160), (4126, 160), (4158, 160), (4190, 160), (4126, 288), (4158, 288), (4286, 384), (4318, 384), (4350, 384), (4382, 384), (4318, 352),(4350, 352),(4382, 352), (4350, 320), (4382, 320), (4382, 288), (4478, 288), (4478, 320), (4478, 352), (4478, 384), (4510, 320) ,(4510, 352), (4510, 384), (4542, 352), (4542, 384), (4574, 384), (4734, 384), (4768, 352), (4768, 384), (4800, 320), (4800, 352), (4800, 384), (4832, 288), (4832, 320), (4832, 352), (4832, 384), (4864, 288),(4864, 320),(4864, 352), (4864, 384), (4960, 288), (4960, 320),(4960, 352),(4960, 384), (4992, 320),(4992, 352), (4992, 384), (5024, 352), (5024, 384), (5056, 384), (5376, 288), (5408, 288), (5440, 288), (5472, 288), (5792, 384), (5824, 352), (5824, 384), (5856, 320), (5856, 352), (5856, 384), (5888, 288), (5888, 320) , (5888, 352), (5888, 384), (5920, 256), (5920, 288), (5920, 320), (5920, 352), (5920, 384), (5952, 224) ,(5952, 256), (5952, 288), (5952, 320), (5952, 352), (5952, 384) ,(5984, 192), (5984, 224), (5984, 256), (5984, 288), (5984, 320), (5984, 352), (5984, 384), (6016, 160), (6016,192), (6016, 224), (6016, 256), (6016, 288), (6016, 320), (6016, 352), (6016, 384), (6048, 160), (6048, 192), (6048, 224), (6048, 256), (6048, 288), (6048, 320), (6048, 352), (6048, 384)]
        block_type1 = [3, 1, 3, 1, 3, 1, 3, 8, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 3, 3, 3, 3, 1 ,1, 1, 1, 1, 3, 3, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5,5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,5,5,5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,5,5,5,5,5,5,5,5,5,5, 1, 1, 3, 1, 5, 5,5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,5, 5, 5, 5, 5, 5, 5, 5]
        block_items1 = [1, 0, 2, 0, 1, 0, 1, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,1, 5, 1, 4 ,1, 1, 2, 1, 0, 0, 0, 0,0, 1, 1,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0, 0, 1, 0, 0,0 ,0 ,0 ,0 ,0,0 ,0 ,0 ,0, 0,0 ,0 ,0, 0, 0 ,0 ,0 ,0 ,0 ,0, 0, 0, 0, 0, 0 ,0 ,0,0,0 ,0 ,0 ,0 ,0 ,0 ,0,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0]
        pipe_position1 = [(896, 352), (1216,320), (1472, 288), (1824, 288), (5216, 352), (5728, 352)]
        pipe_size1 = [0,1,2,2,0, 0]
        pole_position1 = (6304, 80)
        flag_position1 = (6287, 96)
        ground_position1 = ((0, 416), (2272,416) , (2848, 416), (4896, 416))
        ground_size1 = ((2208, 100), (480, 100), (2048, 100), (2272, 100))
        #Level 2
        block_position2 = [(50,50), (100, 50,),(400, 50)]
        block_type2 = [3, 3, 4]
        block_items2 = [2, 1, 1]

        #index variables
        self.current_level = 0
        self.current_block = 0
        self.current_pipe = 0

        self.number_of_blocks = [len(block_position1), len(block_position2)]
        self.number_of_pipes = [len(pipe_position1)]
        self.pipe_positions = [pipe_position1]
        self.pipe_sizes = [pipe_size1]
        self.block_types = [block_type1,block_type2]
        self.block_positions = [block_position1, block_position2]
        self.block_items = [block_items1, block_items2]
        self.flag_positions = [flag_position1]
        self.pole_positions = [pole_position1]
        self.ground_positions = [ground_position1]
        self.ground_sizes = [ground_size1]
        

        self.mario_limit = 3
        self.fireball_width = 5
        self.fireball_height = 5
        self.fireballs_allowed = 2
        self.fireball_speed = 4
        # deal with enemy settings later
        self.mario_speed = 3
        self.mario_jump_speed = 1.5

    def dims(self):
        return self.screen_width, self.screen_height
   
