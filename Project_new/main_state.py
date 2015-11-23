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
import second_state


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
    global character, background, mushrooms, bullets, font, floor

    character = Character()
    mushrooms = create_mushroom()
    background = Background(850, 700)
    floor = Floor()
    bullets = list()
    floor.set_center_object(character)
    character.set_floor(floor)

    font = load_font('resource/UI/ENCR10B.TTF',40)

def exit():
    global character, floor,font

    del(character)
    del(floor)
    del(font)

def pause():
    pass

def resume():
    pass

def fire():
    global bullets
    bullets.append(Bullet(character.x, character.y,floor))

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif character.x > 1000:
            game_framework.change_state(second_state)
        else:
            character.handle_event(event)
            if character.state == character.ATTACK_STATE:
                fire()
            background.handle_event(event)
            floor.handle_event(event)

def collision(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def collision_skill(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb_Holly()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def update(frame_time):
    character.update(frame_time)
    background.update(frame_time)
    floor.update(frame_time)

    for mushroom in mushrooms:
        mushroom.update(frame_time)
        if collision(character,mushroom):
            character.now_hp -= mushroom.Mushroom_attack

        if character.state == character.SKILL_HOLLY_STATE:
            if collision_skill(character, mushroom):
                mushroom.Mushroom_nowhp -= character.skill_holly_damage

        if mushroom.Mushroom_nowhp <= 0:
            character.now_exp += mushroom.mushroom_exp
            if mushrooms.count(mushroom) > 0:
                mushrooms.remove(mushroom)
            if mushrooms.count(mushroom) == 0:
                create_mushroom()

    for bullet in bullets:
        bullet.update(frame_time)
        for mushroom in mushrooms:
            if collision(mushroom, bullet):
                mushroom.Mushroom_nowhp -= character.damage
                if bullets.count(bullet) > 0:
                    bullets.remove(bullet)


def draw(frame_time):
    clear_canvas()

    background.draw()
    floor.draw()
    character.draw()

    for mushroom in mushrooms:
        mushroom.draw()
    for bullet in bullets:
        bullet.draw()

    font.draw(250,60,'HP:%d'%(character.getHp()))
    font.draw(20,30,'LEVEL:%d'%(character.getLevel()))

    update_canvas()


