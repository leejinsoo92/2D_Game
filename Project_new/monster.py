from character import Character
from pico2d import *
import random
import time
import json
import main_state

my_character = None

class Monster:
    image = None
    hp_image = None
    hpcell_image = None

    PIXEL_PER_METER = (10.0 / 0.8 )         # 10 pixel 30cm
    RUN_SPEED_KMPH = 20.0                   # km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 3


    LEFT_RUN, RIGHT_RUN, UP_MOVE, DOWN_MOVE = 0, 1, 2, 3

    MON_2, MON_3 = 0, 1

    def __init__(self,x, y):
        global my_character
        my_character = Character()
        self.x, self.y = x, y
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.speed = 5
        self.state = self.LEFT_RUN
        self.total_frame = 0
        self.start_respone_time_MON = time.time()
        self.start_respone_time_MON_3 = time.time()
        self.live_flag = 0
        self.pattern_type = 0

        self.draw_hp = 100

        self.Mushroom_maxhp = 10
        self.Mushroom_nowhp = self.Mushroom_maxhp
        self.Mushroom_attack = 5

        if Monster.image == None:
            Monster.image = load_image('resource//Monster/Mushroom.png')
        if Monster.hp_image == None:
            Monster.hp_image = load_image('resource/UI/State/Monster_HpBar.png')
        if Monster.hpcell_image == None:
            Monster.hpcell_image = load_image('resource/UI/State/Monster_HpCell_1.png')

    def update(self,frame_time):
        self.distance = Monster.RUN_SPEED_PPS * frame_time
        self.total_frame += Monster.FRAMES_PER_ACTION * Monster.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frame) % 3

        if self.x >= 450:
            self.x -= self.distance

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 67, self.x, self.y)
        self.hp_image.clip_draw(0, 0, 104, 12, self.x - 20, self.y - 40)
        for num in range(0, self.draw_hp):
            self.hpcell_image.clip_draw(0, 0, 1, 10, self.x - 70 + (num), self.y - 40)
            self.draw_hp = self.Mushroom_nowhp * 10


        self.draw_bb()

    def get_bb(self):
        return self.x - 40, self.y - 30, self.x + 10, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())