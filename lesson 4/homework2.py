import pgzrun
import random

WIDTH = 500 
HIGHT = 500

alien  = Actor("alien")
alien.pos = (random.randint(50,450),50)

def draw():
    screen.blit("background.png",(0,0))
    alien.draw()

def update():
    if alien.ycor == (450):
        alien.pos = (random.randint(50,450),50)
        animate(alien,duration = 10,y=HIGHT)

animate(alien,duration = 10,y=HIGHT)



pgzrun.go()