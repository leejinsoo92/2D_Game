from pico2d import *

BULLET_MAX = 200

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

    def __init__(self):
        self.x = [0] * BULLET_MAX
        self.y = [0] * BULLET_MAX
        self.flag = [0] * BULLET_MAX
        self.frame = [0] * BULLET_MAX
        self.total_frame = [0.0] * BULLET_MAX

        if Bullet.image == None:
            Bullet.image = load_image('resource/Character/Bow_ball.png')

    def update(self, frame_time):
        for i in range (0, BULLET_MAX):
            if self.flag[i] == 0:
                continue
            if self.flag[i] == 1:
                self.total_frame[i] += Bullet.FRAMES_PER_ACTION  * Bullet.ACTION_PER_TIME * frame_time
                self.frame[i] = int(self.total_frame[i]) % 2
                self.x[i] += Bullet.BULLET_SPEED_PPS * frame_time * Bullet.BULLET_SPEED

        self.delete_bullet()

    def create_bullet(self, xDot , yDot ):
        for i in range(0, BULLET_MAX):
            if self.flag[i] == 0:
                self.flag[i] = 1
                self.x[i] = xDot
                self.y[i] = yDot
                self.total_frame[i] = 0
                break

    def delete_bullet(self):
        for i in range(0, BULLET_MAX):
            if self.flag[i] == 1:
                if self.x[i] > 1000:
                    self.flag[i] = 0
                elif self.x[i] < -50:
                    self.flag[i] = 0

    def draw(self):
        for i in range(0, BULLET_MAX):
            self.image.clip_draw(self.frame[i] * 100, 0, 100, 21, self.x[i], self.y[i])
        self.draw_bb()

    def get_bb(self, num):
        return self.x[num] - 40, self.y[num] - 5, self.x[num] + 30, self.y[num] + 5

    def draw_bb(self):
        for num in range(0, BULLET_MAX):
            draw_rectangle(*self.get_bb(num))
