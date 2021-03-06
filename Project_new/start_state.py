import game_framework
import title_state
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0
title_sound = None

def enter():
    global image, title_sound
    open_canvas()
    game_framework.reset_time()
    image = load_image('resource/title/kpu_credit.png')
    title_sound = load_music('resource/Sound/title.mp3')
    title_sound.play()
def exit():
    global image
    del(image)
    # close_canvas()


def update(frame_time):
    global logo_time

    if(logo_time > 1.0):
        logo_time = 0
        #game_framework.quit()
        game_framework.push_state(title_state)
    delay(0.01)
    logo_time += 0.01


def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400.0,300.0)
    update_canvas()


def handle_events(frame_time):
    events = get_events()
    pass


def pause(): pass
def resume(): pass




