from character import Character
from pico2d import *

character = None

class Stage:
    image = None

    def __init__(self):
        global character
        self.scroll = 0
        self.offSetX = 400
        self.x = 0
        character = Character()

        if self.image == None:
            self.image = load_image('resource/Map/Stage_1_1.bmp')

    def update(self):
        if character.x > self.offSetX:
            self.scroll -= 5
            self.offSetX += 5

        if character.x < self.offSetX:
            if self.scroll != 0:
                self.scroll += 5
                self.offSetX -= 5

    def draw(self):
        self.image.draw(850 + self.scroll, 300)
