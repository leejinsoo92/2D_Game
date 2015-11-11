from pico2d import *
import random
import time

MON_MAX = 50

class Monster:
    image = None

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
        self.x, self.y = [900] * MON_MAX, [900] * MON_MAX
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

        if Monster.image == None:
            Monster.image = load_image('resource//Monster/Monster_1.png')


    def handle_left_run(self):
        self.x -= self.speed
        self.run_frames += 1
        if self.x <= random.randint(600, 700):
            if self.run_frames % 2 == 0:
                self.state = self.RIGHT_RUN
            elif self.run_frames % 2 == 1:
                self.state = self.UP_MOVE
                self.stand_frames = 0

    def handle_up_move(self):
        self.y += self.speed
        self.stand_frames += 1
        if  self.y >= random.randint(100, 150):
            if self.stand_frames % 2 == 0:
                self.state = self.LEFT_RUN
                self.run_frames = 0
            elif self.stand_frames % 2 == 1:
                self.state = self.RIGHT_RUN
                self.run_frames = 0

    def handle_right_run(self):
        self.x += self.speed
        self.run_frames += 1
        if self.x >= random.randint(700, 800):
            if self.run_frames % 2 == 0:
                self.state = self.LEFT_RUN
            elif self.run_frames % 2 == 1:
                self.state = self.DOWN_MOVE
                self.stand_frames = 0

    def handle_down_move(self):
        self.y -= self.speed
        self.stand_frames += 1
        # if self.stand_frames == random.randint(10, 30):
        if self.y <= random.randint(10, 50):
            if self.stand_frames % 2 == 0:
                self.state = self.LEFT_RUN
                self.run_frames = 0
            elif self.stand_frames % 2 == 1:
                self.state = self.RIGHT_RUN
                self.run_frames = 0



    handle_state = {
                LEFT_RUN : handle_left_run,
                RIGHT_RUN : handle_right_run,
                UP_MOVE : handle_up_move,
                DOWN_MOVE : handle_down_move
    }


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

            if self.end_respone_time - self.start_respone_time_MON_2 >= 5:
                self.create_Monster_Two()
                self.start_respone_time_MON_2 = self.end_respone_time

            if self.end_respone_time - self.start_respone_time_MON_3 >= 7:
                self.create_Monster_Three()
                self.start_respone_time_MON_3 = self.end_respone_time

    def create_Monster_Two(self):
        for num in range(3):
            for i in range(0, MON_MAX):
                if self.live_flag[i] == 0:
                    self.live_flag[i] = 1
                    self.x[i] = 800
                    self.y[i] = 70 * num + 30
                    break

    def create_Monster_Three(self):
        for num in range(3):
            for i in range(0, MON_MAX):
                if self.live_flag[i] == 0:
                    self.live_flag[i] = 1
                    self.x[i] = 800
                    self.y[i] = 70 * num + 30
                    break

    def draw(self):
        for i in range(0, MON_MAX):
            self.image.clip_draw(self.frame * 100, 0, 100, 67, self.x[i], self.y[i])

        self.draw_bb()

    def get_bb(self, num):
        return self.x[num] - 40, self.y[num] - 30, self.x[num] + 10, self.y[num] + 30

    def draw_bb(self):
        for num in range(0, MON_MAX):
            draw_rectangle(*self.get_bb(num))