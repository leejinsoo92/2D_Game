import game_framework
import character
import main_state
from pico2d import *

init = None
character_hp = 0
character_exp = 0
character_level = 0
character_drawhp = 0

def enter():
    global character_hp, character_exp, character_level, character_drawhp
    if init == None:
        character_hp = 0
        character_exp = 0
        character_level = 0
        character_drawhp = 0

def exit():
    pass


def handle_events():
    pass


def draw():
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass







