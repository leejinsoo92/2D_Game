from character import Character
from pico2d import *
import random
import time

MON_MAX = 50
my_character = None

class Monster:
    image = None
    hp_image = None
    hpcell_1_image = None

    PIXEL_PER_METER = (10.0 / 0.3 )         # 10 pixel 30cm
    RUN_SPEED_KMPH = 20.0                   # km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 3


    LEFT_RUN, RIGHT_RUN, UP_MOVE, DOWN_MOVE = 0, 1, 2, 3

    MON_2, MON_3 = 0, 1

    def __init__(self):
        global my_character
        my_character = Character()
        self.x, self.y = [900] * MON_MAX, [300] * MON_MAX
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.speed = 5
        self.state = self.LEFT_RUN
        self.total_frame = 0
        self.start_respone_time_MON_2 = time.time()
        self.start_respone_time_MON_3 = time.time()
        self.live_flag = [0] * MON_MAX
        self.pattern_type = [0] * MON_MAX

        self.monster_1_maxhp = [10] * MON_MAX
        self.monster_1_nowhp = self.monster_1_maxhp
        self.monster_1_attack = 5

        if Monster.image == None:
            Monster.image = load_image('resource//Monster/Monster_1.png')
        if Monster.hp_image == None:
            Monster.hp_image = load_image('resource/UI/State/Monster_HpBar.png')
        if Monster.hpcell_1_image == None:
            Monster.hpcell_1_image = load_image('resource/UI/State/Monster_1_HpCell.png')

    def update(self,frame_time):
        self.distance = Monster.RUN_SPEED_PPS * frame_time
        self.total_frame += Monster.FRAMES_PER_ACTION * Monster.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frame) % 3
        # self.frame = (self.frame + 1) % 3
        # self.handle_state[self.state](self)
        self.end_respone_time = time.time()


        for i in range(0, MON_MAX):
            if self.live_flag[i] == 1:
                self.x[i] -= self.distance

            if self.end_respone_time - self.start_respone_time_MON_2 >= 2:
                self.create_Monster_Two()
                self.start_respone_time_MON_2 = self.end_respone_time

            if self.end_respone_time - self.start_respone_time_MON_3 >= 7:
                self.create_Monster_Three()
                self.start_respone_time_MON_3 = self.end_respone_time

    def create_Monster_Two(self):
        for num in range(2):
            for i in range(0, MON_MAX):
                if self.live_flag[i] == 0:
                    self.live_flag[i] = 1
                    self.x[i] = 800
                    self.y[i] = 70 * num + 100
                    break

    def create_Monster_Three(self):
        for num in range(3):
            for i in range(0, MON_MAX):
                if self.live_flag[i] == 0:
                    self.live_flag[i] = 1
                    self.x[i] = 800
                    self.y[i] = 70 * num + 100
                    break

    def draw(self):
        for i in range(0, MON_MAX):
            self.image.clip_draw(self.frame * 100, 0, 100, 67, self.x[i], self.y[i])
            self.hp_image.clip_draw(0, 0, 104, 12, self.x[i] - 20, self.y[i] - 40)
            for num in range(0, self.monster_1_nowhp[i]):
                self.hpcell_1_image.clip_draw(0, 0, 10, 10, self.x[i] - 65 + (num * 10), self.y[i] - 40)


        self.draw_bb()

    def get_bb(self, num):
        return self.x[num] - 40, self.y[num] - 30, self.x[num] + 10, self.y[num] + 30

    def draw_bb(self):
        for num in range(0, MON_MAX):
            draw_rectangle(*self.get_bb(num))