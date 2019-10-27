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
        # deal with enemy settings later
        #Sounds
        one_up = pygame.mixer.Sound('Audio/Sounds/1up.wav')
        big_jump = pygame.mixer.Sound('Audio/Sounds/BigJump.wav')
        bump = pygame.mixer.Sound('Audio/Sounds/Bump.wav')
        destroy_brick = pygame.mixer.Sound('Audio/Sounds/DestroyBrick.wav')
        fireball = pygame.mixer.Sound('Audio/Sounds/Fireball.wav')
        fireworks = pygame.mixer.Sound('Audio/Sounds/Fireworks.wav')
        flagpole = pygame.mixer.Sound('Audio/Sounds/Flagpole.wav')
        got_coin = pygame.mixer.Sound('Audio/Sounds/GotCoin.wav')
        grow_vine = pygame.mixer.Sound('Audio/Sounds/GrowVine.wav')
        kick = pygame.mixer.Sound('Audio/Sounds/Kick.wav')
        pause = pygame.mixer.Sound('Audio/Sounds/Pause.wav')
        power_up = pygame.mixer.Sound('Audio/Sounds/PowerUp.wav')
        small_jump = pygame.mixer.Sound('Audio/Sounds/SmallJump.wav')
        spawn_power_up = pygame.mixer.Sound('Audio/Sounds/SpawnPowerUp.wav')
        stomp = pygame.mixer.Sound('Audio/Sounds/Stomp.wav')
        travel_pipe = pygame.mixer.Sound('Audio/Sounds/TravelPipe.wav')
        

    def initialize_dynamic_settings(self):
        self.mario_speed = 1.5
        self.mario_jump_speed = 1.5
        # deal with enemy later

    def dims(self):
        return self.screen_width, self.screen_height
