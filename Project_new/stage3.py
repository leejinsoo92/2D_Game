__author__ = 'HP'
from character import Character
from pico2d import *

my_character = None

class Floor3:
    def __init__(self):
        self.image = load_image('resource/Map/Stage_1_3.bmp')
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
        self.image.clip_draw_to_origin(self.left,40,800 ,600,0,0)

    def update(self,frame_time):
        self.left = clamp(0,int(self.set_center_object.x ) - self.canvas_width//2, self.w - self.canvas_width)


    def handle_event(self, event):
        pass