import pgzrun
import random

WIDHT = 500
HIGHT = 500
satalites = []

def create_satalites():
    for i in range(8):
        sat = Actor("satalite")
        satalites.append(sat)
        sat.pos = random.randint(50,450),random.randint(50,450)

create_satalites()

def draw():
    screen.blit("background",(0,0))

    for i in range(8):
        satalites[i].draw()

def update():
    pass






pgzrun.go()