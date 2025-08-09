import pgzrun

WIDTH = 600
HEIGHT = 500


r_1 = Rect((20,20),(400,100))

def draw():
    screen.draw.filled_rect(r_1, color = "blue")

pgzrun.go()


