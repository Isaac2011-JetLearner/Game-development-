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
    screen.draw.line((10,34),(90,64),(255,255,255))

    for i in range(8):
        satalites[i].draw()
        screen.draw.text(str(i+1),(satalites[i].x,satalites[i].y+15),fontsize = 20, color = (255,255,255),)

def update():
    pass  



pgzrun.go() 