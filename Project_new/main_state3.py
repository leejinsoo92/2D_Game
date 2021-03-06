__author__ = 'HP'
import random
import json
import os

# from monster import *
from stage3 import *
from character import *
from bullet import *
from pico2d import *
from monster import Stone
from monster import Boss
import GameOver
import GameClear

import converter
import game_framework
import title_state
import stage3
import main_state3

name = "Second_State"

character = None
boss = None
stone = None
bullet = None
boss_ball = None
stage_2 = None
font = None
sound = None

monster_list = []

current_time = 0.0
regen_time = 0.0
death_time = 0.0

monster_count = 30

def enter():
    global character, bullets, font,state_3, boss, boss_balls, sound
    global current_time

    current_time = get_time()

    character = Character()
    character.now_exp = converter.character_exp
    character.level_max_exp = converter.character_maxexp
    character.draw_exp = int(character.now_exp * (100 / character.level_max_exp))
    character.level = converter.character_level
    character.now_hp = converter.character_nowhp
    character.max_hp = converter.character_maxhp
    character.draw_hp = int(converter.character_nowhp * (100 / converter.character_maxhp))
    character.damage = converter.chracter_damage
    character.skill_gauge = converter.skill_gauge

    boss = Boss()
    state_3 = Floor3()
    bullets = list()
    boss_balls = list()

    #사운드
    sound = load_music('resource/Sound/stage_3.mp3')
    sound.set_volume(64)
    sound.repeat_play()

    state_3.set_center_object(character)
    character.set_floor(state_3)
    font = load_font('resource/UI/ENCR10B.TTF',40)

def exit():
    global character, state_3, font#, boss

    #del(character)
    del(state_3)
    del(font)
    #del(boss)

def pause():
    pass

def resume():
    pass

def fire():
    global bullets
    bullets.append(Bullet(character.x, character.y,state_3))

def boss_fire():
    global boss_balls
    boss_balls.append(BossBullet(boss.x, boss.y, state_3))

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
        else:
            character.handle_event(event)
            if character.state == character.ATTACK_STATE:
                fire()
            state_3.handle_event(event)

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

def collision_skill_last(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb_Last()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def update(frame_time):
    global regen_time, monster_count, death_time, boss, character
    frame_time += get_frame_time()

    regen_time += frame_time

    character.update(frame_time)
    state_3.update(frame_time)

    if monster_count != 0:
        if regen_time > Stone.REGEN_TIME:
            stone = Stone()
            monster_list.append(stone)
            regen_time = 0
            monster_count -= 1

    for stone in monster_list:
        stone.update(frame_time)
        if stone.attack_time == 4:
            if collision(character,stone) and character.state != character.DIE_STATE:
                character.now_hp -= stone.stone_attack
                stone.attack_time -= 1
        if stone.attack_time != 4:
            stone.attack_time -= 1
            if stone.attack_time == 0:
                stone.attack_time = 4

        if character.state == character.SKILL_HOLLY_STATE:
            if collision_skill(character, stone):
                stone.hit(character.skill_holly_damage)

        if character.state == character.SKILL_LAST_STATE:
            if collision_skill_last(character, stone):
                stone.hit(character.skill_last_damage)

        if stone.stone_nowhp <= 0 or boss.boss_nowhp <= 0:
            death_time += frame_time
            if monster_list.count(stone) > 0 and death_time > 0.4:
                monster_list.remove(stone)
                death_time = 0
                character.now_exp += stone.stone_exp

    # 보스
    if boss.death == False:
        boss.update(frame_time)

    if character.state == character.SKILL_HOLLY_STATE:
        if collision_skill(character, boss):
            boss.hit(int(character.skill_holly_damage/4))

    if character.state == character.SKILL_LAST_STATE:
        if collision_skill_last(character, boss):
            boss.hit(int(character.skill_last_damage/4))

    if boss.boss_nowhp <= 0:
        death_time += frame_time
        if death_time > 1.0:
            death_time = 0
            sound.stop()
            game_framework.change_state(GameClear)

    if boss.state == boss.ATTACK_STATE and boss.death == False:
        boss_fire()

    for boss_ball in boss_balls:
        boss_ball.update(frame_time)
        if collision(character, boss_ball):
            character.now_hp -= boss.boss_attack
            boss_balls.remove(boss_ball)

    # 총알
    for bullet in bullets:
        bullet.update(frame_time)
        if collision(boss, bullet):
            boss.hit(character.damage)
            bullets.remove(bullet)

        for stone in monster_list:
            if collision(stone, bullet):
                stone.hit(character.damage)
                if bullets.count(bullet) > 0:
                    bullets.remove(bullet)
        if collision(boss, bullet):
            boss.boss_nowhp -= int(character.damage / 4)

    if character.now_hp <= 0:
        sound.stop()
        game_framework.change_state(GameOver)


def draw(frame_time):
    clear_canvas()

    state_3.draw()
    character.draw()
    boss.draw()
    for stone in monster_list:
        stone.draw()
    for bullet in bullets:
        bullet.draw()

    if boss.death == False:
        for boss_ball in boss_balls:
            boss_ball.draw()

    font.draw(250,60,'HP:%d'%(character.getHp()))
    font.draw(20,30,'LEVEL:%d'%(character.getLevel()))

    update_canvas()



