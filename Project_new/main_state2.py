__author__ = 'HP'
import random
import json
import os

# from monster import *
from stage2 import *
from character import *
from bullet import *
from pico2d import *
from monster import Pig

import converter
import game_framework
import title_state
import stage2
import main_state3

name = "Second_State"

character = None
pig = None
bullet = None
stage_2 = None
font = None

monster_list = []

current_time = 0.0
regen_time = 0.0

monster_count = 30

def enter():
    global character, bullets, font,state_2
    global current_time

    current_time = get_time()

    character = Character()
    character.now_hp = converter.character_hp
    character.now_exp = converter.character_exp
    character.level = converter.character_level
    character.draw_hp = converter.character_drawhp

    state_2 = Floor2()
    bullets = list()

    state_2.set_center_object(character)
    character.set_floor(state_2)
    font = load_font('resource/UI/ENCR10B.TTF',40)

def exit():
    global character, state_2,font

    del(character)
    del(state_2)
    del(font)

def pause():
    pass

def resume():
    pass

def fire():
    global bullets
    bullets.append(Bullet(character.x, character.y,state_2))

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
        elif character.x > 800 :
            converter.character_hp = character.now_hp
            converter.character_exp = character.now_exp
            converter.character_level = character.level
            converter.character_drawhp = int(character.now_hp * (100 / character.max_hp))
            game_framework.change_state(main_state3)
        else:
            character.handle_event(event)
            if character.state == character.ATTACK_STATE:
                fire()
            state_2.handle_event(event)

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
    global regen_time, monster_count
    frame_time += get_frame_time()

    regen_time += frame_time

    character.update(frame_time)
    state_2.update(frame_time)

    if monster_count != 0:
        if regen_time > Pig.REGEN_TIME:
            pig = Pig()
            monster_list.append(pig)
            regen_time = 0
            monster_count -= 1

    for pig in monster_list:
        pig.update(frame_time)
        if pig.attack_time == 4:
            if collision(character,pig):
                character.now_hp -= pig.pig_attack
                pig.attack_time -= 1
        if pig.attack_time != 4:
            pig.attack_time -= 1
            if pig.attack_time == 0:
                pig.attack_time = 4

        if character.state == character.SKILL_HOLLY_STATE:
            if collision_skill(character, pig):
                pig.pig_nowhp -= character.skill_holly_damage

        if pig.pig_nowhp <= 0:
            character.now_exp += pig.pig_exp
            if monster_list.count(pig) > 0:
                monster_list.remove(pig)

    for bullet in bullets:
        bullet.update(frame_time)
        for pig in monster_list:
            if collision(pig, bullet):
                pig.pig_nowhp -= character.damage
                if bullets.count(bullet) > 0:
                    bullets.remove(bullet)
        if bullet.sx > 900:
            bullets.remove(bullet)

def draw(frame_time):
    clear_canvas()

    state_2.draw()
    character.draw()
    for pig in monster_list:
        pig.draw()
    for bullet in bullets:
        bullet.draw()

    font.draw(250,60,'HP:%d'%(character.getHp()))
    font.draw(20,30,'LEVEL:%d'%(character.getLevel()))

    update_canvas()



