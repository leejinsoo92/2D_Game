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
mushroom = None
bullet = None
stage = None
font = None


count = 0

Timer = SDL_GetTicks()
MON_MAX = 2

def enter():
    global character, stage, mushrooms, bullets, font

    character = Character()
    mushrooms = create_mushroom()
    stage = Stage(850, 700)
    bullets = []

    font = load_font('resource/UI/ENCR10B.TTF',40)

def exit():
    global character, stage,font

    del(character)
    del(stage)
    del(font)

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

def collision(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def update(frame_time):
    #global character, Mushroom, bullet, stage, count, Timer
    character.update(frame_time)
    stage.update(frame_time)

    for mushroom in mushrooms:
        mushroom.update(frame_time)
        if collision(character,mushroom):
            if character.state == character.SKILL_HOLLY_STATE:
                mushroom.Mushroom_nowhp -= character.skill_holly_damage

        for bullet in bullets:
            if collision(mushroom, bullet):
                mushroom.Mushroom_nowhp -= character.damage
                bullets.remove(bullet)

            if mushroom.Mushroom_nowhp <= 0:
                character.now_exp += mushroom.mushroom_exp
                #mushroom.live_flag = 0
                if mushrooms.count(mushroom) > 0:
                    mushrooms.remove(mushroom)
                if mushrooms.count(mushroom) == 0:
                    create_mushroom()

def draw(frame_time):
    #global Mushroom
    clear_canvas()

    stage.draw()
    character.draw()
    for mushroom in mushrooms:
        mushroom.draw()
    for bullet in bullets:
        bullet.draw()

    font.draw(250,60,'HP:%d'%(character.getHp()))
    font.draw(20,30,'LEVEL:%d'%(character.getLevel()))

    update_canvas()



