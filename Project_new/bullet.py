from pico2d import *
import json
import main_state

class Bullet:
    image = None

    PIXEL_PER_METER = (10.0 / 0.3 )         # 10 pixel 30cm
    BULLET_SPEED_KMPH = 20.0                   # km / Hour
    BULLET_SPEED_MPM = (BULLET_SPEED_KMPH * 1000.0 / 60.0)
    BULLET_SPEED_MPS = (BULLET_SPEED_MPM / 60.0)
    BULLET_SPEED_PPS = (BULLET_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 2
    BULLET_SPEED = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.flag = 0
        self.frame = 0
        self.total_frame = 0.0

        if Bullet.image == None:
            Bullet.image = load_image('resource/Character/Bow_ball.png')

    def update(self, frame_time):
        # if self.flag == 1:
        #     self.total_frame aaa+= Bullet.FRAMES_PER_ACTION  * Bullet.ACTION_PER_TIME * frame_time
        #     self.frame = int(self.total_frame) % 2
        #     self.x += Bullet.BULLET_SPEED_PPS * frame_time * Bullet.BULLET_SPEED
        #
        # self.delete_bullet()
        pass
    def create_bullet(self, xDot , yDot ):
        if self.flag == 0:
            self.flag = 1
            self.x = xDot
            self.y = yDot
            self.total_frame = 0

    def delete_bullet(self):
        if self.flag == 1:
            if self.x > 1000:
                self.flag = 0
            elif self.x < -50:
                self.flag = 0

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 21, self.x + 10, self.y)
        self.x += 20
        self.draw_bb()

    def get_bb(self):
        return self.x - 40, self.y - 5, self.x + 30, self.y + 5

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
