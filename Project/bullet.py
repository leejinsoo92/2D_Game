from character import *
from pico2d import *

BULLET_MAX = 200
class Bullet:
    image = None

    def createshot(self, xDot , yDot ):
        i = 0
        while(i < BULLET_MAX):
            if self.flag[i] == 0:
                self.flag[i] = 1
                self.x[i] = xDot
                self.y[i] = yDot
                return
            i += 1

    def __init__(self):
        self.frame = 0
        self.x = [0] * BULLET_MAX
        self.y = [0] * BULLET_MAX
        self.flag = [0] * BULLET_MAX

        if Bullet.image == None:
            Bullet.image = load_image('resource/Character/Bow_ball.png')

    def update(self):
        self.frame = (self.frame + 1) % 3

        i = 0
        while(i<BULLET_MAX):
            if self.flag[i] == 1:
                self.x[i] += 10
            i += 1

    def draw(self):
        i = 0
        while(i < BULLET_MAX):
            self.image.clip_draw(self.frame * 100, 0, 100, 21, self.x[i], self.y[i])
            i += 1
