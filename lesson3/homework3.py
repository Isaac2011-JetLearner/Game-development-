import pgzrun
import random

score = 0
duration = 12

WIDTH = 500
HEIGHT = 500

cat = Actor("cat")
cat.pos = (300,350)

flower = Actor("flower")

flower.pos = (250,30)
def draw():
    screen.blit("background",(0,0))
    cat.draw()
    flower.draw()

def update():
    global duration
    global score
    if keyboard.left:
        cat.x-=5

    elif keyboard.right:
        cat.x+=5

    if cat.colliderect(flower):
        flower.pos = random.randint(50,450),30
        duration-=1
        score+=1
        print(score)
        animate(flower,duration = duration,y=HEIGHT)



animate(flower,duration = 12,y=HEIGHT)





pgzrun.go()
