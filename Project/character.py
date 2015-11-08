from bullet import *
from pico2d import *

bullet = None

class Character:

    PIXEL_PER_METER = (10.0 / 0.3 )         # 10 pixel 30cm
    RUN_SPEED_KMPH = 20.0                   # km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    image = None
    attack_image = None
    state = None

    LEFT_STATE, RIGHT_STATE, UP_STATE, DOWN_STATE, ATTACK_STATE ,STAND_STATE = 0 ,1 ,2, 3, 4, 5

    def __init__(self):
        self.x, self.y = 100, 90
        self.frame = 0
        self.speed = 5
        self.attack_frame = 0
        self.attack_time = 0
        self.attack = False
        self.total_frame = 0.0

        if Character.attack_image == None:
            Character.attack_image = load_image('resource/Character/Bow_attack_right.png')
        if Character.image == None:
            Character.image = load_image('resource/Character/Bow_walk_Right.png')

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            self.state = self.RIGHT_STATE
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            self.state = self.STAND_STATE

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            self.state = self.LEFT_STATE
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            self.state = self.STAND_STATE

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            self.state = self.UP_STATE
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            self.state = self.STAND_STATE

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            self.state = self.DOWN_STATE
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            self.state = self.STAND_STATE

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            self.state = self.ATTACK_STATE
            self.attack = True
            Bullet.createshot(0, self.x, self.y - 10)

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            self.state = self.STAND_STATE
            self.attack = False


    def update(self, frame_time):
        self.distance = Character.RUN_SPEED_PPS * frame_time
        self.total_frame += Character.FRAMES_PER_ACTION * Character.ACTION_PER_TIME * frame_time


        if self.attack == True:
            self.attack_frame = (self.attack_frame + 1) % 3
        else:
            self.frame = (self.frame + 1) % 4
            if self.state == self.RIGHT_STATE:
                self.x += self.speed
            elif self.state == self.LEFT_STATE:
                self.x -= self.speed
            elif self.state == self.UP_STATE:
                self.y += self.speed
            elif self.state == self.DOWN_STATE:
                self.y -= self.speed

        if self.attack == True:
            self.attack_time += 0.5
            if self.attack_time >= 2:
                self.attack_time = 0
                self.attack = False

    def draw(self):
        if self.attack == False:
            self.image.clip_draw(self.frame * 100, 0, 100, 77, self.x, self.y)
        elif self.attack == True:
            self.attack_image.clip_draw(self.attack_frame * 99, 0, 99, 77, self.x, self.y)

