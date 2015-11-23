__author__ = 'HP'
import random
import json
import os

from monster import *
from stage2 import *
from character import *
from bullet import *
from pico2d import *

import game_framework
import title_state
import stage2


name = "Second_State"

character = None
pig = None
bullet = None
stage_2 = None
font = None


count = 0

Timer = SDL_GetTicks()

def enter():
    global character, pigs, bullets, font,state_2

    character = Character()
    pigs = create_pig()
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

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
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
    #global character, Mushroom, bullet, stage, count, Timer
    character.update(frame_time)
    state_2.update(frame_time)

    print(character.skill_holly_damage)

    for pig in pigs:
        pig.update(frame_time)
        if collision(character,pig):
            character.now_hp -= pig.pig_attack

        if character.state == character.SKILL_HOLLY_STATE:
            if collision_skill(character, pig):
                pig.pig_nowhp -= character.skill_holly_damage

        if pig.pig_nowhp <= 0:
            character.now_exp += pig.pig_exp
            if pigs.count(pig) > 0:
                pigs.remove(pig)
            if pigs.count(pig) == 0:
                create_pig()

    for bullet in bullets:
        bullet.update(frame_time)
        for pig in pigs:
            if collision(pig, bullet):
                pig.pig_nowhp -= character.damage
                if bullets.count(bullet) > 0:
                    bullets.remove(bullet)

def draw(frame_time):
    #global Mushroom
    clear_canvas()

    state_2.draw()
    character.draw()
    for pig in pigs:
        pig.draw()
    for bullet in bullets:
        bullet.draw()

    font.draw(250,60,'HP:%d'%(character.getHp()))
    font.draw(20,30,'LEVEL:%d'%(character.getLevel()))

    update_canvas()



