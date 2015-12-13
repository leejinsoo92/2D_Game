import game_framework
import character
import main_state
from pico2d import *

init = None
character_hp = 0
character_exp = 0
character_maxexp = 0
character_drawexp = 0
character_level = 0
character_drawhp = 0
character_nowhp = 0
character_maxhp = 0
chracter_damage = 0
skill_gauge = 0

def enter():
    global character_exp, character_level, character_drawhp, chracter_damage,chracter_nowhp, character_maxhp, character_maxexp, character_drawexp,skill_gauge
    if init == None:
        character_exp = 0
        character_level = 0
        character_drawhp = 0
        chracter_nowhp = 0
        character_maxhp = 0
        chracter_damage = 0
        character_maxexp = 0
        character_drawexp = 0
        skill_gauge = 0
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







