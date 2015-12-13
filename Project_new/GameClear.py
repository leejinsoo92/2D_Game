import game_framework

import main_state
import main_state3
from pico2d import *


name = "TitleState"
image = None
title_time = 0
sound = None

def enter():
    global  image, sound
    image = load_image('resource/title/GameClear.png')
    sound = load_wav('resource/Sound/clear.wav')
    sound.play()
    
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






