import pgzrun

WIDTH = 500
HIGHT = 500 

r = Rect((20,20),(200,200))

def draw():
    screen.draw.filled_rect(r, color = "red")

pgzrun.go()