import game_framework

import logo2_state
from pico2d import *


name = "TitleState"
image = None
title_time = 0

def enter():
    global  image, title_sound
    image = load_image('resource/title/Logo_1.jpg')
    
def exit():
    global image
    del(image)


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if( event.type , event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(logo2_state)


def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def update(frame_time):
    pass

def pause():
    pass
def resume():
    pass






