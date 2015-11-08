from pico2d import *
import random

class Monster:
    image = None
    LEFT_RUN, RIGHT_RUN, UP_MOVE, DOWN_MOVE = 0, 1, 2, 3

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


    def update(self):
        self.frame = (self.frame + 1) % 3
        self.handle_state[self.state](self)


    def __init__(self):
        self.x, self.y = random.randint(600, 800), random.randint(10, 150)
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.speed = 5
        self.state = self.LEFT_RUN
        if Monster.image == None:
            Monster.image = load_image('resource//Monster/Monster_1.png')
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 67, self.x, self.y)

