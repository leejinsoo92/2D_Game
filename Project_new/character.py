from pico2d import *

class Character:

    PIXEL_PER_METER = (10.0 / 0.3 )         # 10 pixel 30cm
    RUN_SPEED_KMPH = 20.0                   # km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    HOLLY_FRAMES_PER_ACTION = 1
    HOLLY_ACTION_PER_TIME = 3.0 / TIME_PER_ACTION

    image = None
    attack_image = None
    stand_image = None
    state = None
    die_image = None

    character_hp_image = None
    hpbar_image = None
    exp_image = None
    expbar_image = None
    skill_bar = None
    skill_cell = None

    #스킬 이미지
    skill_holly = [None] * 14

    get_x = 0

    DIE_STATE, LEFT_STATE, RIGHT_STATE, UP_STATE, DOWN_STATE, ATTACK_STATE ,STAND_STATE = 0 ,1 ,2, 3, 4, 5, 6

    SKILL_HOLLY_STATE = 7

    def __init__(self):
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.x, self.y = 100, 150
        self.frame = 0
        self.speed = 0
        self.attack_frame = 0
        self.attack_time = 0
        self.stand_frame = 0
        self.state = self.STAND_STATE
        self.total_frame = 0.0
        self.skill_holly_frame = 0.0
        self.draw_hp = 100

        self.attack = False
        self.levelup_type = False
        #캐릭터 상태
        self.level = 1
        self.damage = 1
        self.max_hp = 100
        self.now_hp = self.max_hp

        self.get_exp = 1
        self.level_1_max_exp = 10
        self.now_exp = 0
        self.dir = 0

        #스킬
        self.skill_gauge = 0
        self.timer = 0
        self.skill_frame = 0
        self.skill_holly_type = False
        self.skill_holly_damage = 10

        if Character.stand_image == None:
            Character.stand_image = load_image('resource/Character/Bow_Stand.png')
        if Character.attack_image == None:
            Character.attack_image = load_image('resource/Character/Bow_attack_right.png')
        if Character.image == None:
            Character.image = load_image('resource/Character/Bow_walk_Right.png')
        if Character.die_image == None:
            Character.die_image = load_image('resource/Character/Grave.png')

        # 캐릭터 hp,exp
        if Character.character_hp_image == None:
            Character.character_hp_image = load_image('resource/UI/State/character_HpCell.png')
        if Character.hpbar_image == None:
            Character.hpbar_image = load_image('resource/UI/State/character_HpBar.png')
        if Character.exp_image == None:
            Character.exp_image = load_image('resource/UI/State/Exp_Cell.png')
        if Character.expbar_image == None:
            Character.expbar_image = load_image('resource/UI/State/Exp_Bar.png')
        # skill 게이지
        if Character.skill_bar == None:
            Character.skill_bar = load_image('resource/UI/State/Skill_Bar.png')
        if Character.skill_cell == None:
            Character.skill_cell = load_image('resource/UI/State/Skill_Cell.png')


        # skill_Holly
        # for i in range(0,14):
        #     if Character.skill_holly[i] == None:
        #         if i == 0: Character.skill_holly[0] = load_image('resource/Skill/Skill_Holly/Skill_Holly_1.png')
        #         if i == 1: Character.skill_holly[1] = load_image('resource/Skill/Skill_Holly/Skill_Holly_2.png')
        #         if i == 2: Character.skill_holly[2] = load_image('resource/Skill/Skill_Holly/Skill_Holly_3.png')
        #         if i == 3: Character.skill_holly[3] = load_image('resource/Skill/Skill_Holly/Skill_Holly_4.png')
        #         if i == 4: Character.skill_holly[4] = load_image('resource/Skill/Skill_Holly/Skill_Holly_5.png')
        #         if i == 5: Character.skill_holly[5] = load_image('resource/Skill/Skill_Holly/Skill_Holly_6.png')
        #         if i == 6: Character.skill_holly[6] = load_image('resource/Skill/Skill_Holly/Skill_Holly_7.png')
        #         if i == 7: Character.skill_holly[7] = load_image('resource/Skill/Skill_Holly/Skill_Holly_8.png')
        #         if i == 8: Character.skill_holly[8] = load_image('resource/Skill/Skill_Holly/Skill_Holly_9.png')
        #         if i == 9: Character.skill_holly[9] = load_image('resource/Skill/Skill_Holly/Skill_Holly_10.png')
        #         if i == 10: Character.skill_holly[10] = load_image('resource/Skill/Skill_Holly/Skill_Holly_11.png')
        #         if i == 11: Character.skill_holly[11] = load_image('resource/Skill/Skill_Holly/Skill_Holly_12.png')
        #         if i == 12: Character.skill_holly[12] = load_image('resource/Skill/Skill_Holly/Skill_Holly_13.png')
        #         if i == 13: Character.skill_holly[13] = load_image('resource/Skill/Skill_Holly/Skill_Holly_14.png')


        if Character.skill_holly[0] == None:
            Character.skill_holly[0] = load_image('resource/Skill/Skill_Holly/Skill_Holly_1.png')
            Character.skill_holly[1] = load_image('resource/Skill/Skill_Holly/Skill_Holly_2.png')
            Character.skill_holly[2] = load_image('resource/Skill/Skill_Holly/Skill_Holly_3.png')
            Character.skill_holly[3] = load_image('resource/Skill/Skill_Holly/Skill_Holly_4.png')
            Character.skill_holly[4] = load_image('resource/Skill/Skill_Holly/Skill_Holly_5.png')
            Character.skill_holly[5] = load_image('resource/Skill/Skill_Holly/Skill_Holly_6.png')
            Character.skill_holly[6] = load_image('resource/Skill/Skill_Holly/Skill_Holly_7.png')
            Character.skill_holly[7] = load_image('resource/Skill/Skill_Holly/Skill_Holly_8.png')
            Character.skill_holly[8] = load_image('resource/Skill/Skill_Holly/Skill_Holly_9.png')
            Character.skill_holly[9] = load_image('resource/Skill/Skill_Holly/Skill_Holly_10.png')
            Character.skill_holly[10] = load_image('resource/Skill/Skill_Holly/Skill_Holly_11.png')
            Character.skill_holly[11] = load_image('resource/Skill/Skill_Holly/Skill_Holly_12.png')
            Character.skill_holly[12] = load_image('resource/Skill/Skill_Holly/Skill_Holly_13.png')
            Character.skill_holly[13] = load_image('resource/Skill/Skill_Holly/Skill_Holly_14.png')

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.UP_STATE, self.DOWN_STATE, self.LEFT_STATE, self.ATTACK_STATE, self.STAND_STATE):
                self.state = self.RIGHT_STATE
                self.dir = 1
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_STATE,):
                self.state = self.STAND_STATE
                self.dir = 0

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.UP_STATE, self.DOWN_STATE, self.RIGHT_STATE, self.ATTACK_STATE, self.STAND_STATE):
                self.state = self.LEFT_STATE
                self.dir = -1
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_STATE,):
                self.state = self.STAND_STATE
                self.dir = 0

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.state in (self.RIGHT_STATE, self.DOWN_STATE, self.LEFT_STATE, self.ATTACK_STATE, self.STAND_STATE):
                self.state = self.UP_STATE
                self.dir = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            if self.state in (self.UP_STATE,):
                self.state = self.STAND_STATE

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.state in (self.UP_STATE, self.RIGHT_STATE, self.LEFT_STATE, self.ATTACK_STATE, self.STAND_STATE):
                self.state = self.DOWN_STATE
                self.dir = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            if self.state in (self.DOWN_STATE,):
                self.state = self.STAND_STATE

        # 일반 공격
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            if self.state in (self.UP_STATE, self.DOWN_STATE, self.LEFT_STATE, self.RIGHT_STATE, self.STAND_STATE):
                self.state = self.ATTACK_STATE
                self.attack = True
                self.dir = 0

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_a):
            if self.state in (self.ATTACK_STATE,):
                self.state = self.STAND_STATE
                self.attack = False

        #skill_holly
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
            if (self.skill_gauge >= 10):
                if self.state in (self.UP_STATE, self.DOWN_STATE, self.LEFT_STATE, self.RIGHT_STATE, self.STAND_STATE, self.ATTACK_STATE):
                    self.state = self.SKILL_HOLLY_STATE
                    self.skill_holly_type = True
                    self.skill_gauge -= 10

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_q):
            if self.state in (self.SKILL_HOLLY_STATE,):
                self.state = self.STAND_STATE


    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.distance = Character.RUN_SPEED_PPS * frame_time
        self.total_frame += Character.FRAMES_PER_ACTION * Character.ACTION_PER_TIME * frame_time
        self.skill_holly_frame += Character.HOLLY_FRAMES_PER_ACTION * Character.HOLLY_ACTION_PER_TIME * frame_time

        Character.get_x = self.x

        self.speed = Character.RUN_SPEED_PPS * frame_time
        self.x += (self.dir * self.speed)
        self.x = clamp(0, self.x, self.fl.w)

        if self.attack == True:
            self.attack_frame = int(self.total_frame) % 3
        else:
            if self.state == self.STAND_STATE:
                self.stand_frame = int(self.total_frame) % 3
            else:
                self.frame = int(self.total_frame) % 4

            if self.state == self.UP_STATE and self.y < 280:
                self.y += self.distance
            elif self.state == self.DOWN_STATE and self.y > 100:
                self.y -= self.distance

        if self.skill_holly_type == True:
            self.skill_frame = int(self.skill_holly_frame) % 14
            if self.skill_frame == 13:
                self.skill_holly_type = False
                self.skill_frame = 0

        if self.attack == True:
            self.attack_time += 0.5
            if self.attack_time >= 9:
                self.attack_time = 0
                self.attack = False
                self.state = self.STAND_STATE

        # 캐릭터 상태
        if self.level == 2 and self.levelup_type == True:
            self.max_hp = 150
            self.now_hp = self.max_hp
            self.damage = 2
            self.levelup_type = False

        elif self.level == 3 and self.levelup_type == True:
            self.max_hp = 200
            self.now_hp = self.max_hp
            self.damage = 3
            self.levelup_type = False

        elif self.level == 4 and self.levelup_type == True:
            self.max_hp = 250
            self.now_hp = self.max_hp
            self.damage = 4
            self.levelup_type = False

        elif self.level == 5 and self.levelup_type == True:
            self.max_hp = 300
            self.now_hp = self.max_hp
            self.damage = 5
            self.levelup_type = False

        elif self.level == 6 and self.levelup_type == True:
            self.max_hp = 350
            self.now_hp = self.max_hp
            self.damage = 6
            self.levelup_type = False

        elif self.level == 7 and self.levelup_type == True:
            self.max_hp = 400
            self.now_hp = self.max_hp
            self.damage = 7
            self.levelup_type = False

        elif self.level == 8 and self.levelup_type == True:
            self.max_hp = 450
            self.now_hp = self.max_hp
            self.damage = 8
            self.levelup_type = False

        elif self.level == 9 and self.levelup_type == True:
            self.max_hp = 500
            self.now_hp = self.max_hp
            self.damage = 9
            self.levelup_type = False

        elif self.level == 10 and self.levelup_type == True:
            self.max_hp = 550
            self.now_hp = self.max_hp
            self.damage = 10
            self.levelup_type = False

        #스킬 게이지 타이머
        if(self.timer != 11):
            self.timer += 1
            if self.timer == 10 and self.skill_gauge != 100:
                self.skill_gauge += 1
            if(self.timer == 11):
                self.timer = 0

    def draw(self):
        self.temp = 0
        x_left_offset = min(0,self.x-self.canvas_width//2)
        x_right_offset = max(0,self.x - self.fl.w + self.canvas_width//2)
        x_offset = x_left_offset + x_right_offset

        if self.state == Character.DIE_STATE:
            self.die_image.clip_draw(0, 0, 101, 47, self.canvas_width//2+x_offset , self.y)

        if self.attack == False:
            if self.state == self.STAND_STATE:
                self.stand_image.clip_draw(self.stand_frame * 99, 0, 100, 77, self.canvas_width//2+x_offset , self.y)
            else:
                self.image.clip_draw(self.frame * 100, 0, 100, 77, self.canvas_width//2+x_offset, self.y)
        elif self.attack == True:
            self.attack_image.clip_draw(self.attack_frame * 99, 0, 99, 77, self.canvas_width//2+x_offset, self.y)

        if self.skill_holly_type == True:
            self.skill_holly[self.skill_frame].clip_draw(0,0, 410,222, self.canvas_width//2+x_offset + 220, self.y + 30)
            self.draw_bb_Holly()

        #self.skill_holly[10].clip_draw(0,0, 410, 222, self.x, self.y)
        self.hpbar_image.clip_draw( 0, 0, 206, 36, 350, 25)
        self.expbar_image.clip_draw(0, 0, 206, 36, 600, 25)
        self.skill_bar.clip_draw(0, 0, 104, 12, self.canvas_width//2+x_offset - 15, self.y - 50)

        #스킬 게이지
        for i in range(0,self.skill_gauge):
            self.skill_cell.clip_draw( 0, 0, 1, 10, self.canvas_width//2+x_offset - 65 + i, self.y - 50)
        # 레벨
        if self.level == 1:
            for i in range(0, self.now_hp) :
                self.character_hp_image.clip_draw( 0, 0, 2, 30, 350 - 99 + (i * 2), 25)

            for i in range(0, self.now_exp) :
                self.exp_image.clip_draw( 0, 0, 20, 30, 600 - 90 + (i * 20), 25)
                if self.now_exp >= self.level_1_max_exp:
                    self.now_exp = 0
                    self.level = 2
                    self.levelup_type = True

        if self.level == 2:
            for i in range(0, self.draw_hp) :
                self.character_hp_image.clip_draw( 0, 0, 2, 30, 350 - 99 + (i * 2), 25)
                self.draw_hp = int(self.now_hp * (100 / self.max_hp))
            for i in range(0, self.now_exp) :
                self.exp_image.clip_draw( 0, 0, 20, 30, 600 - 90 + (i * 20), 25)
                if self.now_exp >= self.level_1_max_exp:
                    self.now_exp = 0
                    self.level = 3
                    self.levelup_type = True

        if self.level == 3:
            for i in range(0, self.draw_hp) :
                self.character_hp_image.clip_draw( 0, 0, 2, 30, 350 - 99 + (i * 2), 25)
                self.draw_hp = int(self.now_hp * (100 / self.max_hp))
            for i in range(0, self.now_exp) :
                self.exp_image.clip_draw( 0, 0, 20, 30, 600 - 90 + (i * 20), 25)
                if self.now_exp >= self.level_1_max_exp:
                    self.now_exp = 0
                    self.level = 4
                    self.levelup_type = True

        if self.level == 4:
            for i in range(0, self.draw_hp) :
                self.character_hp_image.clip_draw( 0, 0, 2, 30, 350 - 99 + (i * 2), 25)
                self.draw_hp = int(self.now_hp * (100 / self.max_hp))
            for i in range(0, self.now_exp) :
                self.exp_image.clip_draw( 0, 0, 20, 30, 600 - 90 + (i * 20), 25)
                if self.now_exp >= self.level_1_max_exp:
                    self.now_exp = 0
                    self.level = 5
                    self.levelup_type = True

        if self.level == 5:
            for i in range(0, self.draw_hp) :
                self.character_hp_image.clip_draw( 0, 0, 2, 30, 350 - 99 + (i * 2), 25)
                self.draw_hp = int(self.now_hp * (100 / self.max_hp))
            for i in range(0, self.now_exp) :
                self.exp_image.clip_draw( 0, 0, 20, 30, 600 - 90 + (i * 20), 25)
                if self.now_exp >= self.level_1_max_exp:
                    self.now_exp = 0
                    self.level = 6
                    self.levelup_type = True

        if self.level == 6:
            for i in range(0, self.draw_hp) :
                self.character_hp_image.clip_draw( 0, 0, 2, 30, 350 - 99 + (i * 2), 25)
                self.draw_hp = int(self.now_hp * (100 / self.max_hp))
            for i in range(0, self.now_exp) :
                self.exp_image.clip_draw( 0, 0, 20, 30, 600 - 90 + (i * 20), 25)
                if self.now_exp >= self.level_1_max_exp:
                    self.now_exp = 0
                    self.level = 7
                    self.levelup_type = True

        if self.level == 7:
            for i in range(0, self.draw_hp) :
                self.character_hp_image.clip_draw( 0, 0, 2, 30, 350 - 99 + (i * 2), 25)
                self.draw_hp = int(self.now_hp * (100 / self.max_hp))
            for i in range(0, self.now_exp) :
                self.exp_image.clip_draw( 0, 0, 20, 30, 600 - 90 + (i * 20), 25)
                if self.now_exp >= self.level_1_max_exp:
                    self.now_exp = 0
                    self.level = 8
                    self.levelup_type = True

        if self.level == 8:
            for i in range(0, self.draw_hp) :
                self.character_hp_image.clip_draw( 0, 0, 2, 30, 350 - 99 + (i * 2), 25)
                self.draw_hp = int(self.now_hp * (100 / self.max_hp))
            for i in range(0, self.now_exp) :
                self.exp_image.clip_draw( 0, 0, 20, 30, 600 - 90 + (i * 20), 25)
                if self.now_exp >= self.level_1_max_exp:
                    self.now_exp = 0
                    self.level = 9
                    self.levelup_type = True

        if self.level == 9:
            for i in range(0, self.draw_hp) :
                self.character_hp_image.clip_draw( 0, 0, 2, 30, 350 - 99 + (i * 2), 25)
                self.draw_hp = int(self.now_hp * (100 / self.max_hp))
            for i in range(0, self.now_exp) :
                self.exp_image.clip_draw( 0, 0, 20, 30, 600 - 90 + (i * 20), 25)
                if self.now_exp >= self.level_1_max_exp:
                    self.now_exp = 0
                    self.level = 10
                    self.levelup_type = True

        if self.level == 10:
            for i in range(0, self.draw_hp) :
                self.character_hp_image.clip_draw( 0, 0, 2, 30, 350 - 99 + (i * 2), 25)
                self.draw_hp = int(self.now_hp * (100 / self.max_hp))

        # self.draw_bb()

    def get_bb(self):
        x_left_offset = min(0,self.x-self.canvas_width//2)
        x_right_offset = max(0,self.x - self.fl.w + self.canvas_width//2)
        x_offset = x_left_offset + x_right_offset
        return self.canvas_width//2+x_offset - 50, self.y - 40, self.canvas_width//2+x_offset + 10, self.y + 40

    def get_bb_Holly(self):
        x_left_offset = min(0,self.x-self.canvas_width//2)
        x_right_offset = max(0,self.x - self.fl.w + self.canvas_width//2)
        x_offset = x_left_offset + x_right_offset
        return self.canvas_width//2+x_offset + 50, self.y - 60, self.canvas_width//2+x_offset + 430, self.y + 80

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw_bb_Holly(self):
        draw_rectangle(*self.get_bb_Holly())

    def getHp(self):
        return self.now_hp

    def getLevel(self):
        return self.level

    def set_floor(self,fl):
        self.fl = fl