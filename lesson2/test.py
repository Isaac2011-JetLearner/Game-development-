import pgzrun
import random

WIDTH = 500 
HIEGHT = 500 
allen = Actor("alien")

def draw():
    screen.fill(color = (9,234,32))
    allen.draw()

def on_mouse_down(pos):
    if allen.collidepoint(pos):
        allen.pos = random.randint(100,400),random.randint(100,400)



pgzrun.go()