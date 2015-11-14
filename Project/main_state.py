import random
import json
import os

from monster import *
from stage import *
from character import *
from bullet import *
from pico2d import *

import game_framework
import title_state


name = "MainState"

character = None
monster = None
bullet = None
stage = None
font = None


def enter():
    global character, stage, monster, bullet

    character = Character()
    monster = Monster()
    stage = Stage()
    bullet = Bullet();

def exit():
    global character, stage,monster, bullet

    del(character)
    del(monster)
    del(stage)
    del(bullet)

def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
        else:
            character.handle_event(event, bullet)

def collision(a, b, a_num, b_num):
    left_a, bottom_a, right_a, top_a = a.get_bb(a_num)
    left_b, bottom_b, right_b, top_b = b.get_bb(b_num)

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True


def update(frame_time):
    global character, monster, bullet, stage

    character.update(frame_time, bullet)
    monster.update(frame_time)
    bullet.update(frame_time)
    stage.update(frame_time)

    for i in range(0, 200):
        if bullet.flag[i] ==0:
            continue

    for num in range(50):
        if monster.live_flag[num] == 0:
            continue

        if collision(monster, bullet, num, 0):
            bullet.flag[num] = 0
            if bullet.flag[num] == 0:
                bullet.x[num] = -100
                bullet.y[num] = -100
            monster.monster_1_nowhp[num] -= character.damage
            if monster.monster_1_nowhp[num] <= 0:
                monster.live_flag[num] = 0
                monster.x[num] = -100
                monster.y[num] = -100


def draw(frame_time):
   clear_canvas()

   stage.draw()
   character.draw()
   monster.draw()
   bullet.draw()

   update_canvas()



