import random
import json
import os

from monster import *
from stage import *
from character import *
from bullet import *
from pico2d import *

import converter
import game_framework
import title_state
import main_state2

# from monster import Mushroom

name = "MainState"

character = None
mushroom = None
bullet = None
stage = None
font = None

monster_list = []

current_time = 0.0
regen_time = 0.0
death_time = 0.0

monster_count = 30

def enter():
    global character, background, bullets, font, floor
    global current_time

    current_time = get_time()

    character = Character()
    # character.now_hp = converter.character_hp
    # character.now_exp = converter.character_exp
    # character.level = converter.character_level

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

def get_frame_time():
    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif character.x > 1200 :
            converter.character_hp = character.now_hp
            converter.character_exp = character.now_exp
            converter.character_maxexp = character.level_max_exp
            converter.character_drawexp = int(character.now_exp * (100 / character.level_max_exp))
            converter.character_level = character.level
            converter.character_nowhp = character.now_hp
            converter.character_maxhp = character.max_hp
            converter.character_drawhp = int(character.now_hp * (100 / character.max_hp))
            converter.chracter_damage = character.damage
            game_framework.change_state(main_state2)
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
    global regen_time, monster_count, death_time
    frame_time += get_frame_time()

    character.update(frame_time)
    background.update(frame_time)
    floor.update(frame_time)

    regen_time += frame_time

    if monster_count != 0:
        if regen_time > Mushroom.REGEN_TIME:
            mushroom = Mushroom()
            monster_list.append(mushroom)
            regen_time = 0
            monster_count -= 1

    for mushroom in monster_list:
        mushroom.update(frame_time)
        if mushroom.attack_time == 5:
            if collision(character,mushroom):
                character.now_hp -= mushroom.Mushroom_attack
                mushroom.attack_time -= 1
        if mushroom.attack_time != 5:
            mushroom.attack_time -= 1
            if mushroom.attack_time == 0:
                mushroom.attack_time = 5

        if character.state == character.SKILL_HOLLY_STATE:
                if collision_skill(character, mushroom):
                        mushroom.Mushroom_nowhp -= character.skill_holly_damage

        if mushroom.Mushroom_nowhp <= 0:
            death_time += frame_time
            if monster_list.count(mushroom) > 0 and death_time > 0.5:
                monster_list.remove(mushroom)
                death_time = 0
                character.now_exp += mushroom.mushroom_exp


    for bullet in bullets:
        bullet.update(frame_time)
        for mushroom in monster_list:
            if collision(mushroom, bullet):
                mushroom.Mushroom_nowhp -= character.damage
                if bullets.count(bullet) > 0:
                    bullets.remove(bullet)
        if bullet.sx > 1000:
            bullets.remove(bullet)

def draw(frame_time):
    clear_canvas()

    background.draw()
    floor.draw()
    character.draw()

    for mushroom in monster_list:
        mushroom.draw()
    for bullet in bullets:
        bullet.draw()

    font.draw(250,60,'HP:%d'%(character.getHp()))
    font.draw(20,30,'LEVEL:%d'%(character.getLevel()))

    update_canvas()


