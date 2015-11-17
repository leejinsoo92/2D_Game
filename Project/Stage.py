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

    # 캐릭터 상태
    # hp_image = None
    # hpbar_image = None
    # exp_image = None
    # expbar_image = None

    def __init__(self):
        global my_character
        self.scroll = 0
        self.offSetX = 400
        self.x = 0
        my_character = Character()

        if self.image == None:
            self.image = load_image('resource/Map/Stage_1_1.bmp')

        # 캐릭터 hp,exp
        # if Character.hp_image == None:
        #     Character.hp_image = load_image('resource/UI/State/character_HpCell.png')
        # if Character.hpbar_image == None:
        #     Character.hpbar_image = load_image('resource/UI/State/character_HpBar.png')
        # if Character.exp_image == None:
        #     Character.exp_image = load_image('resource/UI/State/Exp_Cell.png')
        # if Character.expbar_image == None:
        #     Character.expbar_image = load_image('resource/UI/State/Exp_Bar.png')


    def update(self, frame_time):
        if my_character.get_x > self.offSetX:
            self.scroll -= 5
            self.offSetX += 5

        if my_character.get_x < self.offSetX:
            if self.scroll != 0:
                self.scroll += 5
                self.offSetX -= 5

    def draw(self):
        self.image.draw(850 + self.scroll, 350)
