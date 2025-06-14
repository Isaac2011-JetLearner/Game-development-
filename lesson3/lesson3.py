import pgzrun
import random

WIDTH = 500
HEIGHT = 500

duration = 10
jerry = Actor("jerry")
jerry.pos = (250,250)

cheese = Actor("cheese")
# cheese.pos = random.randint(50,450),random.randint(50,450)
cheese.pos = (250,10)
def draw():
    screen.blit("background",(0,0))
    jerry.draw()
    cheese.draw()

def update():
    global duration
    if keyboard.left:
        jerry.x-=5

    elif keyboard.right:
        jerry.x+=5

    elif keyboard.up:
        jerry.y-=5

    elif keyboard.down:
        jerry.y+=5

    if jerry.colliderect(cheese):
        cheese.pos = random.randint(50,450),10
        duration-=2
        animate(cheese,duration = duration,y=HEIGHT)

animate(cheese,duration = 10,y=HEIGHT)

    



pgzrun.go()