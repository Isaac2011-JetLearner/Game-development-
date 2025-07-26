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



def draw():
    screen.blit("grassland.png",(0,0))
    blue_slab.draw()
    green_ball.draw()

def update():
    global change_y,change_x

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

    if green_ball.y > HEIGHT or green_ball.y < 0 :
        change_y*=-1

    if green_ball.x > WIDTH or green_ball.x < 0:
        change_x*=-1

    


    # animate(green_ball,duration = 20, y= 400)

    # if green_ball.pos >= (400,250):
    #     green_ball.x-=6
    #     green_ball.y-=6
    #     animate(green_ball,duration = 5, y= 50)

        






pgzrun.go()