from pico2d import *
import json
import main_state

class Bullet:
    image = None

    PIXEL_PER_METER = (10.0 / 0.1 )         # 10 pixel 30cm
    BULLET_SPEED_KMPH = 20.0                   # km / Hour
    BULLET_SPEED_MPM = (BULLET_SPEED_KMPH * 1000.0 / 60.0)
    BULLET_SPEED_MPS = (BULLET_SPEED_MPM / 60.0)
    BULLET_SPEED_PPS = (BULLET_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 2
    BULLET_SPEED = 5

    def __init__(self, x, y, bg):
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.x = x
        self.y = y
        self.flag = 0
        self.frame = 0
        self.total_frame = 0.0
        self.sx = 0
        self.bg = bg

        if Bullet.image == None:
            Bullet.image = load_image('resource/Character/Bow_ball.png')

    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))
        speed = Bullet.BULLET_SPEED_PPS * frame_time
        self.x += speed
        self.total_frame += Bullet.FRAMES_PER_ACTION * Bullet.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frame) % 2
        self.x = clamp(0, self.x, self.bg.w + 100)

    def draw(self):
        self.sx = self.x - self.bg.left
        self.image.clip_draw(self.frame * 100, 0, 100, 21, self.sx, self.y)
        # self.draw_bb()

    def get_bb(self):
        sx = self.x - self.bg.left
        return sx - 40, self.y - 5, sx + 30, self.y + 5

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
