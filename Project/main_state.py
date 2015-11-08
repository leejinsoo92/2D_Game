import random
import json
import os

from monster import *
from stage import *
from character import *
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


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
        else:
            character.handle_event(event)


def update(frame_time):
    character.update(frame_time)
    monster.update(frame_time)
    bullet.update(frame_time)
    stage.update(frame_time)

    delay(0.05)

def draw():
   clear_canvas()

   stage.draw()
   character.draw()
   monster.draw()
   bullet.draw()

   update_canvas()



