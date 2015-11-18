from character import Character
from pico2d import *

my_character = None

class Stage:

    PIXEL_PER_METER = (10.0 / 0.3 )         # 10 pixel 30cm
    SCROLL_SPEED_KMPH = 20.0                   # km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    image = None

    def __init__(self, w, h):
        global my_character
        self.scroll = 0
        self.offSetX = 400
        self.x = 0
        self.speed = 0
        self.speed_y = 0
        self.left = 0
        self.up = 0
        self.screen_width = w
        self.screen_height = h

        my_character = Character()

        if self.image == None:
            self.image = load_image('resource/Map/Stage_1_1.bmp')


    def update(self, frame_time):
        # if my_character.get_x > self.offSetX:
        #     self.scroll -= 5
        #     self.offSetX += 5
        #
        # if my_character.get_x < self.offSetX:
        #     if self.scroll != 0:
        #         self.scroll += 5
        #         self.offSetX -= 5
        self.left = (self.left + frame_time * self.speed) % self.image.w

    def draw(self):
        # self.image.draw(850 + self.scroll, 350)
        x = int(self.left)

        w = min(self.image.w - x, self.screen_width)

        self.image.clip_draw_to_origin(x, 0, w, self.screen_height, 0 ,0)
        self.image.clip_draw_to_origin(0, 0 , self.screen_width - w, self.screen_height ,w ,0)


    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                self.speed -= Stage.SCROLL_SPEED_PPS
            elif event.key == SDLK_RIGHT:
                self.speed += Stage.SCROLL_SPEED_PPS

        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT: self.speed += Stage.SCROLL_SPEED_PPS
            elif event.key == SDLK_RIGHT: self.speed -= Stage.SCROLL_SPEED_PPS
