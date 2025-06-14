import pgzrun
import random

WIDTH = 500 
HEIGHT = 500 
allen = Actor("alien")

click = 0
def draw():
    screen.fill(color = (9,234,32))
    allen.draw()
    screen.draw.text("score:"+str(click),center = (450,20),fontsize = 30 )


def on_mouse_down(pos):
    global click
    if allen.collidepoint(pos):
        allen.pos = random.randint(100,400),random.randint(100,400)
        click+=1
        print(click)


pgzrun.go()