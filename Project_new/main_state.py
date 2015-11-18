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
monster_1 = None
bullet = None
stage = None
font = None

MON_MAX = 2
BULLET_MAX = 200

def enter():
    global character, stage, monsters_1, bullets

    character = Character()
    monsters_1 = [Monster() for i in range(MON_MAX)]
    stage = Stage(850, 700)
    bullets = []

def exit():
    global character, stage,monsters_1

    del(character)
    del(monsters_1)
    del(stage)

def pause():
    pass

def resume():
    pass

def fire():
    global bullets
    bullets.append(Bullet(character.x, character.y))

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
        else:
            character.handle_event(event)
            if character.state == character.ATTACK_STATE:
                fire()
            stage.handle_event(event)

# def collision(a, b, a_num, b_num):
#     left_a, bottom_a, right_a, top_a = a.get_bb(a_num)
#     left_b, bottom_b, right_b, top_b = b.get_bb(b_num)
#
#     if left_a > right_b : return False
#     if right_a < left_b : return False
#     if top_a < bottom_b : return False
#     if bottom_a > top_b : return False
#
#     return Truea

def collision(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def update(frame_time):
    global character, monster_1, bullet, stage
    character.update(frame_time)
    # for bullet in bullets:
    for monster_1 in monsters_1:
        monster_1.update(frame_time)
        for bullet in bullets:
            if collision(monster_1, bullet):
                monster_1.monster_1_nowhp -= character.damage
                bullets.remove(bullet)

            if monster_1.monster_1_nowhp <= 0:
                monster_1.live_flag = 0
                monsters_1.remove(monster_1)

    stage.update(frame_time)

def draw(frame_time):
   clear_canvas()

   stage.draw()
   character.draw()
   for monster_1 in monsters_1:
       monster_1.draw()
   for bullet in bullets:
       bullet.draw()

   update_canvas()



