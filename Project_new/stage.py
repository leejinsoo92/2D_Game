from character import Character
from pico2d import *

my_character = None

class Background:

    PIXEL_PER_METER = (10.0 / 0.3 )         # 10 pixel 30cm
    SCROLL_SPEED_KMPH = 20.0                   # km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    image = None

    def __init__(self, w, h):
        global my_character
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
                self.speed -= Background.SCROLL_SPEED_PPS
            elif event.key == SDLK_RIGHT:
                self.speed += Background.SCROLL_SPEED_PPS

        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT: self.speed += Background.SCROLL_SPEED_PPS
            elif event.key == SDLK_RIGHT: self.speed -= Background.SCROLL_SPEED_PPS


class Floor:

    PIXEL_PER_METER = (10.0 / 0.3 )         # 10 pixel 30cm
    RUN_SPEED_KMPH = 20.0                   # km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    def __init__(self):
        self.image = load_image('resource/Map/Floor_1.png')
        self.image_next = load_image('resource/UI/Next_Move.jpg')
        self.frame = 0
        self.total_frame = 0.0
        self.speed = 0
        self.left = 0
        self.x = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.height = 95

    def set_center_object(self, character):
        self.set_center_object = character

    def draw(self):
        self.image.clip_draw_to_origin(self.left,0,800 ,235,0,0)
        self.image_next.clip_draw(self.frame * 100, 0, 100, 44, 800, 200)
    def update(self,frame_time):
        self.left = clamp(0,int(self.set_center_object.x ) - self.canvas_width//2, self.w - self.canvas_width)
        self.total_frame += Floor.FRAMES_PER_ACTION * Floor.ACTION_PER_TIME * frame_time

        self.frame = int(self.total_frame) % 3

    def handle_event(self, event):
        pass