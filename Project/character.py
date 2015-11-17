from pico2d import *

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
    stand_image = None
    state = None

    level_1_hp_image = None
    hpbar_image = None
    exp_image = None
    expbar_image = None

    get_x = 0

    LEFT_STATE, RIGHT_STATE, UP_STATE, DOWN_STATE, ATTACK_STATE ,STAND_STATE = 0 ,1 ,2, 3, 4, 5

    def __init__(self):
        self.x, self.y = 100, 150
        self.frame = 0
        self.speed = 5
        self.attack_frame = 0
        self.attack_time = 0
        self.stand_frame = 0
        self.state = self.STAND_STATE
        self.total_frame = 0.0

        self.attack = False

        self.damage = 1
        self.max_hp = 100
        self.now_hp = self.max_hp

        self.get_exp = 1
        self.max_exp = 10
        self.now_exp = 0

        if Character.stand_image == None:
            Character.stand_image = load_image('resource/Character/Bow_Stand.png')
        if Character.attack_image == None:
            Character.attack_image = load_image('resource/Character/Bow_attack_right.png')
        if Character.image == None:
            Character.image = load_image('resource/Character/Bow_walk_Right.png')

        # 캐릭터 hp,exp
        if Character.level_1_hp_image == None:
            Character.level_1_hp_image = load_image('resource/UI/State/Level_1_HpCell.png')
        if Character.hpbar_image == None:
            Character.hpbar_image = load_image('resource/UI/State/character_HpBar.png')
        if Character.exp_image == None:
            Character.exp_image = load_image('resource/UI/State/Exp_Cell.png')
        if Character.expbar_image == None:
            Character.expbar_image = load_image('resource/UI/State/Exp_Bar.png')

    def handle_event(self, event, bullet):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.UP_STATE, self.DOWN_STATE, self.LEFT_STATE, self.ATTACK_STATE, self.STAND_STATE):
                self.state = self.RIGHT_STATE
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_STATE,):
                self.state = self.STAND_STATE

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.UP_STATE, self.DOWN_STATE, self.RIGHT_STATE, self.ATTACK_STATE, self.STAND_STATE):
                self.state = self.LEFT_STATE
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_STATE,):
                self.state = self.STAND_STATE

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.state in (self.RIGHT_STATE, self.DOWN_STATE, self.LEFT_STATE, self.ATTACK_STATE, self.STAND_STATE):
                self.state = self.UP_STATE
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            if self.state in (self.UP_STATE,):
                self.state = self.STAND_STATE

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.state in (self.UP_STATE, self.RIGHT_STATE, self.LEFT_STATE, self.ATTACK_STATE, self.STAND_STATE):
                self.state = self.DOWN_STATE
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            if self.state in (self.DOWN_STATE,):
                self.state = self.STAND_STATE

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            if self.state in (self.UP_STATE, self.DOWN_STATE, self.LEFT_STATE, self.RIGHT_STATE, self.STAND_STATE):
                self.state = self.ATTACK_STATE
                self.attack = True
                bullet.create_bullet(self.x, self.y - 10)

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_a):
            if self.state in (self.ATTACK_STATE,):
                self.state = self.STAND_STATE
                self.attack = False


    def update(self, frame_time, bullet):
        self.distance = Character.RUN_SPEED_PPS * frame_time
        self.total_frame += Character.FRAMES_PER_ACTION * Character.ACTION_PER_TIME * frame_time

        Character.get_x = self.x

        if self.attack == True:
            self.attack_frame = int(self.total_frame) % 3
        else:
            if self.state == self.STAND_STATE:
                self.stand_frame = int(self.total_frame) % 3
            else:
                self.frame = int(self.total_frame) % 4

            if self.state == self.RIGHT_STATE:
                self.x += self.distance
            elif self.state == self.LEFT_STATE:
                self.x -= self.distance
            elif self.state == self.UP_STATE and self.y < 280:
                self.y += self.distance
            elif self.state == self.DOWN_STATE and self.y > 100:
                self.y -= self.distance

        if self.attack == True:
            self.attack_time += 0.5
            if self.attack_time >= 9:
                self.attack_time = 0
                self.attack = False
                self.state = self.STAND_STATE

    def draw(self):
        if self.attack == False:
            if self.state == self.STAND_STATE:
                self.stand_image.clip_draw(self.stand_frame * 99, 0, 100, 77, self.x , self.y)
            else:
                self.image.clip_draw(self.frame * 100, 0, 100, 77, self.x, self.y)
        elif self.attack == True:
            self.attack_image.clip_draw(self.attack_frame * 99, 0, 99, 77, self.x, self.y)

        self.hpbar_image.clip_draw( 0, 0, 206, 36, 300, 25)
        for i in range(0, self.now_hp) :
            self.level_1_hp_image.clip_draw( 0, 0, 2, 30, 300 - 99 + (i * 2), 25)

        self.expbar_image.clip_draw(0, 0, 206, 36, 600, 25)
        for i in range(0, self.now_exp) :
            self.exp_image.clip_draw( 0, 0, 6, 30, 600 - 94 + (i * 6), 25)

        self.draw_bb()

    def get_bb(self):
        return self.x - 50, self.y - 40, self.x + 10, self.y + 40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())