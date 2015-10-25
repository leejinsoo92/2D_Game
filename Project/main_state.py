import random
import json
import os

from pico2d import *

import game_framework
import title_state


name = "MainState"

Character = None
Monster = None
Bullet = None
Stage = None
font = None



class Stage:
    def __init__(self):
        self.image = load_image('resource/Map/Stage_1_1.bmp')

    def draw(self):
        self.image.draw(0, 300)



class Character:

    image = None
    attack_image = None
    state = None

    LEFT_STATE, RIGHT_STATE, UP_STATE, DOWN_STATE, ATTACK_STATE ,STAND_STATE = 0 ,1 ,2, 3, 4, 5


    def __init__(self):
        self.x, self.y = 100, 90
        self.frame = 0
        self.attack_frame = 0
        self.attack_time = 0
        self.attack = False

        if Character.attack_image == None:
            Character.attack_image = load_image('resource/Character/Bow_attack_right.png')
        if Character.image == None:
            Character.image = load_image('resource/Character/Bow_walk_Right.png')

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            self.state = self.RIGHT_STATE
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            self.state = self.STAND_STATE

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            self.state = self.LEFT_STATE
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            self.state = self.STAND_STATE

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            self.state = self.UP_STATE
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            self.state = self.STAND_STATE

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            self.state = self.DOWN_STATE
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            self.state = self.STAND_STATE

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            self.state = self.ATTACK_STATE
            self.attack = True
            Bullet.createshot(0, self.x, self.y - 10)

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            self.state = self.STAND_STATE
            self.attack = False


    def update(self):
        if self.attack == True:
            self.attack_frame = (self.attack_frame + 1) % 3
        else:
            self.frame = (self.frame + 1) % 4
            if self.state == self.RIGHT_STATE:
                self.x += 5
            elif self.state == self.LEFT_STATE:
                self.x -= 5
            elif self.state == self.UP_STATE:
                self.y += 5
            elif self.state == self.DOWN_STATE:
                self.y -= 5

        if self.attack == True:
            self.attack_time += 0.5
            if self.attack_time >= 2:
                self.attack_time = 0
                self.attack = False

    def draw(self):
        if self.attack == False:
            self.image.clip_draw(self.frame * 100, 0, 100, 77, self.x, self.y)
        elif self.attack == True:
            self.attack_image.clip_draw(self.attack_frame * 99, 0, 99, 77, self.x, self.y)


BULLET_MAX = 200
class Bullet:
    image = None

    def createshot(self, type, xDot , yDot ):
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
            if self.flag[i] ==1:
                self.x[i] += 10
            i += 1

    def draw(self):
        i = 0
        while(i < BULLET_MAX):
            self.image.clip_draw(self.frame * 100, 0, 100, 21, self.x[i], self.y[i])
            i += 1




class Monster:
    image = None
    LEFT_RUN, RIGHT_RUN, UP_MOVE, DOWN_MOVE = 0, 1, 2, 3

    def handle_left_run(self):
        self.x -= self.speed
        self.run_frames += 1
        if self.x <= random.randint(600, 700):
            if self.run_frames % 2 == 0:
                self.state = self.RIGHT_RUN
            elif self.run_frames % 2 == 1:
                self.state = self.UP_MOVE
                self.stand_frames = 0

    def handle_up_move(self):
        self.y += self.speed
        self.stand_frames += 1
        if  self.y >= random.randint(100, 150):
            if self.stand_frames % 2 == 0:
                self.state = self.LEFT_RUN
                self.run_frames = 0
            elif self.stand_frames % 2 == 1:
                self.state = self.RIGHT_RUN
                self.run_frames = 0

    def handle_right_run(self):
        self.x += self.speed
        self.run_frames += 1
        if self.x >= random.randint(700, 800):
            if self.run_frames % 2 == 0:
                self.state = self.LEFT_RUN
            elif self.run_frames % 2 == 1:
                self.state = self.DOWN_MOVE
                self.stand_frames = 0

    def handle_down_move(self):
        self.y -= self.speed
        self.stand_frames += 1
        # if self.stand_frames == random.randint(10, 30):
        if self.y <= random.randint(10, 50):
            if self.stand_frames % 2 == 0:
                self.state = self.LEFT_RUN
                self.run_frames = 0
            elif self.stand_frames % 2 == 1:
                self.state = self.RIGHT_RUN
                self.run_frames = 0



    handle_state = {
                LEFT_RUN : handle_left_run,
                RIGHT_RUN : handle_right_run,
                UP_MOVE : handle_up_move,
                DOWN_MOVE : handle_down_move
    }


    def update(self):
        self.frame = (self.frame + 1) % 3
        self.handle_state[self.state](self)


    def __init__(self):
        self.x, self.y = random.randint(600, 800), random.randint(10, 150)
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.speed = 5
        self.state = self.LEFT_RUN
        if Monster.image == None:
            Monster.image = load_image('resource//Monster/Monster_1.png')
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 67, self.x, self.y)



def enter():
    global Character, Stage, Monster, Bullet
    Character = Character()
    Monster = Monster()
    Stage = Stage()
    Bullet = Bullet();

def exit():
    global Character, Stage, Monster, Bullet
    del(Character)
    del(Monster)
    del(Stage)
    del(Bullet)

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
        else:
            Character.handle_event(event)


def update():
    Character.update()
    Monster.update()
    Bullet.update()

    delay(0.05)

def draw():
   clear_canvas()

   Stage.draw()
   Character.draw()
   Monster.draw()
   Bullet.draw()

   update_canvas()




