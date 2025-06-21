import pgzrun
import random

WIDTH = 500 
HIGHT = 500

alien  = Actor("alien")
alien.pos = (random,50)

def draw():
    screen.blit("background.png",(0,0))
    alien.draw()

def update():
    pass

animate(alien,duration = 10,y=HIGHT)

while True:
    if alien.ypos == (450):
        animate(alien,duration = 10,y=HIGHT)





pgzrun.go()