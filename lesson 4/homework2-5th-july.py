import pgzrun
import random
WIDTH = 500
HEIGHT = 500


empty = []


cat = Actor("cat")
cat.pos = random.randint(50,450),random.randint(50,450)

alien = Actor("alien")
alien.pos = random.randint(50,450),random.randint(50,450)

sat = Actor("satalite")
sat.pos = random.randint(50,450),random.randint(50,450)

jerry = Actor("jerry")
jerry.pos = random.randint(50,450),random.randint(50,450)




def draw ():
    screen.blit("background",(0,0))
    cat.draw()
    alien.draw()
    sat.draw()
    jerry.draw()
    screen.draw.line(cat.pos,alien.pos,(255,255,255))
    screen.draw.line(alien.pos,sat.pos,(255,255,255))
    screen.draw.line(sat.pos,jerry.pos,(255,255,255))



def update():
    pass
    

    

pgzrun.go()
