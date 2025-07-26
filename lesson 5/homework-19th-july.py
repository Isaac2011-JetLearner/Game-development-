import pgzrun

import random

WIDTH = 800
HEIGHT = 500

empty = 0

blue_slab = Actor("blue-slab")
blue_slab.pos = (400,350)

green_ball = Actor("green-ball")
green_ball.pos = (0,0)
# random.randint(50,450),30

change_x = 2
change_y = 2

score = 0



def draw():
    screen.blit("grassland.png",(0,0))
    blue_slab.draw()
    green_ball.draw()

def update():
    global change_y,change_x,score

    if keyboard.left:
        blue_slab.x-=5

    elif keyboard.right:
        blue_slab.x+=5

    if blue_slab.x == WIDTH:
        blue_slab.pos = (600,300)

    elif blue_slab.x < 0:
        blue_slab.pos = (100,300)
    
    green_ball.x+=change_x
    green_ball.y+=change_y
    
    if green_ball.colliderect(blue_slab):
        change_y*=-1
        change_x*=-1
        score+=1

 
    if green_ball.y > HEIGHT :
        


pgzrun.go()