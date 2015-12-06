from character import Character
from pico2d import *
import random
import time
import json
import main_state

my_character = None

class Mushroom:
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

    REGEN_TIME = 0

    LEFT_RUN, RIGHT_RUN, UP_MOVE, DOWN_MOVE = 0, 1, 2, 3

    def __init__(self):
        global my_character
        my_character = Character()
        self.x, self.y = 900, random.randint(100,300)
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.speed = 5
        self.state = self.LEFT_RUN
        self.total_frame = 0
        self.pattern_type = 0
        self.mushroom_exp = 1

        self.attack_time = 5

        self.dir = -1

        self.draw_hp = 100

        self.Mushroom_maxhp = 10
        self.Mushroom_nowhp = self.Mushroom_maxhp
        self.Mushroom_attack = 5

        Mushroom.REGEN_TIME = 3

        if Mushroom.image == None:
            Mushroom.image = load_image('resource//Monster/Mushroom.png')
        if Mushroom.hp_image == None:
            Mushroom.hp_image = load_image('resource/UI/Monster_HpBar.png')
        if Mushroom.hpcell_image == None:
            Mushroom.hpcell_image = load_image('resource/UI/Monster_HpCell_1.png')

    def update(self,frame_time):
        self.distance = Mushroom.RUN_SPEED_PPS * frame_time
        self.total_frame += Mushroom.FRAMES_PER_ACTION * Mushroom.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frame) % 3

        if self.dir == -1:
            self.state = self.LEFT_RUN
            self.x -= self.distance
            if self.x < 10:
                self.dir = 1

        elif self.dir == 1:
            self.state = self.RIGHT_RUN
            self.x += self.distance
            if self.x > 800:
                self.dir = -1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 67, self.x, self.y)
        self.hp_image.clip_draw(0, 0, 104, 12, self.x - 20, self.y - 40)
        for num in range(0, self.draw_hp):
            self.hpcell_image.clip_draw(0, 0, 1, 10, self.x - 70 + (num), self.y - 40)
            self.draw_hp = self.Mushroom_nowhp * 10


        # self.draw_bb()

    def get_bb(self):
        return self.x - 40, self.y - 30, self.x + 10, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())



class Pig:
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

    REGEN_TIME = 0

    def __init__(self):
        global my_character
        my_character = Character()
        self.x, self.y = 900, random.randint(100,300)
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.speed = 5
        self.state = self.LEFT_RUN
        self.total_frame = 0
        self.live_flag = 0
        self.pattern_type = 0
        self.pig_exp = 2

        self.dir = -1

        self.draw_hp = 100

        self.attack_time = 4

        self.pig_maxhp = 30
        self.pig_nowhp = self.pig_maxhp
        self.pig_attack = 5

        Pig.REGEN_TIME = 5

        if Pig.image == None:
            Pig.image = load_image('resource//Monster/Pig.png')
        if Pig.hp_image == None:
            Pig.hp_image = load_image('resource/UI/Monster_HpBar.png')
        if Pig.hpcell_image == None:
            Pig.hpcell_image = load_image('resource/UI/Monster_HpCell_1.png')

    def update(self,frame_time):
        self.distance = Pig.RUN_SPEED_PPS * frame_time
        self.total_frame += Pig.FRAMES_PER_ACTION * Pig.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frame) % 3

        if self.dir == -1:
            self.state = self.LEFT_RUN
            self.x -= self.distance
            if self.x < 10:
                self.dir = 1

        elif self.dir == 1:
            self.state = self.RIGHT_RUN
            self.x += self.distance
            if self.x > 800:
                self.dir = -1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 50, self.x, self.y)
        self.hp_image.clip_draw(0, 0, 104, 12, self.x - 20, self.y - 40)
        for num in range(0, self.draw_hp):
            self.hpcell_image.clip_draw(0, 0, 1, 10, self.x - 70 + (num), self.y - 40)
            self.draw_hp = int(self.pig_nowhp * 10 / 3 )


        # self.draw_bb()

    def get_bb(self):
        return self.x - 40, self.y - 30, self.x + 10, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class Stone:
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

    REGEN_TIME = 0

    def __init__(self):
        global my_character
        my_character = Character()
        self.x, self.y = 900, random.randint(100,300)
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.speed = 5
        self.state = self.LEFT_RUN
        self.total_frame = 0
        self.live_flag = 0
        self.pattern_type = 0
        self.stone_exp = 3

        self.dir = -1

        self.draw_hp = 100

        self.attack_time = 4

        self.stone_maxhp = 60
        self.stone_nowhp = self.stone_maxhp
        self.stone_attack = 15

        Stone.REGEN_TIME = 5

        if Stone.image == None:
            Stone.image = load_image('resource/Monster/Stone.png')
        if Stone.hp_image == None:
            Stone.hp_image = load_image('resource/UI/Monster_HpBar.png')
        if Stone.hpcell_image == None:
            Stone.hpcell_image = load_image('resource/UI/Monster_HpCell_1.png')

    def update(self,frame_time):
        self.distance = Stone.RUN_SPEED_PPS * frame_time
        self.total_frame += Stone.FRAMES_PER_ACTION * Stone.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frame) % 3

        if self.dir == -1:
            self.state = self.LEFT_RUN
            self.x -= self.distance
            if self.x < 10:
                self.dir = 1

        elif self.dir == 1:
            self.state = self.RIGHT_RUN
            self.x += self.distance
            if self.x > 800:
                self.dir = -1

    def draw(self):
        self.image.clip_draw(self.frame * 200, 0, 200, 153, self.x, self.y)
        self.hp_image.clip_draw(0, 0, 104, 12, self.x - 20, self.y - 40)
        for num in range(0, self.draw_hp):
            self.hpcell_image.clip_draw(0, 0, 1, 10, self.x - 70 + (num), self.y - 40)
            self.draw_hp = int( self.stone_nowhp * 10 / 6)


        self.draw_bb()

    def get_bb(self):
        return self.x - 60, self.y - 40, self.x + 30, self.y + 40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Boss:
    image = None
    hp_image = None
    hpcell_image = None
    attack_image = None

    PIXEL_PER_METER = (10.0 / 0.8 )         # 10 pixel 30cm
    RUN_SPEED_KMPH = 20.0                   # km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 3


    LEFT_RUN, RIGHT_RUN, UP_MOVE, DOWN_MOVE = 0, 1, 2, 3

    REGEN_TIME = 0
    CURRENT_TIME = 0.0

    def __init__(self):
        global my_character
        my_character = Character()
        self.x, self.y = 800, random.randint(100,300)
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.speed = 5
        self.state = self.LEFT_RUN
        self.total_frame = 0
        self.live_flag = 0
        self.pattern_type = 0
        self.boss_exp = 2
        self.pattern_type = 1

        self.dir = -1

        self.draw_hp = 100

        self.attack_time = 50

        self.boss_maxhp = 400
        self.boss_nowhp = self.boss_maxhp
        self.boss_attack = 5

        Boss.CURRENT_TIME = get_time()

        if Boss.image == None:
            Boss.image = load_image('resource/Boss/Boss_1.png')
        if Boss.attack_image == None:
            Boss.attack_image = load_image('resource/Boss/Boss_1_Attack.png')
        if Boss.hp_image == None:
            Boss.hp_image = load_image('resource/UI/Boss_HpBar.png')
        if Boss.hpcell_image == None:
            Boss.hpcell_image = load_image('resource/UI/Boss_HpCell.png')

    def update(self,frame_time):
        self.distance = Boss.RUN_SPEED_PPS * frame_time
        self.total_frame += Boss.FRAMES_PER_ACTION * Boss.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frame) % 3

        if self.dir == -1:
            self.state = self.LEFT_RUN
            self.x -= self.distance
            if self.x < 500:
                self.dir = 1

        elif self.dir == 1:
            self.state = self.RIGHT_RUN
            self.x += self.distance
            if self.x > 800:
                self.dir = -1

        if self.attack_time == 50:
            self.pattern_type *= -1
            self.attack_time -= self.pattern_type
        if self.attack_time != 50:
            self.attack_time -= self.pattern_type
            if self.attack_time == 0:
                self.pattern_type *= -1

        print(self.attack_time)

    def draw(self):
        self.hp_image.clip_draw(0, 0, 406, 36, 400, 500)
        for num in range(0, self.boss_nowhp):
            self.hpcell_image.clip_draw(0, 0, 1, 30, 202 + (num), 500)

        if self.attack_time != 0:
            self.attack_image.clip_draw(self.frame * 200, 0, 200, 171, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 190, 0, 190, 170, self.x, self.y)

        self.draw_bb()


    def get_frame_time(self):
        frame_time = get_time() - Boss.CURRENT_TIME
        Boss.CURRENT_TIME += frame_time
        return frame_time

    def get_bb(self):
        return self.x - 40, self.y - 30, self.x + 10, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
