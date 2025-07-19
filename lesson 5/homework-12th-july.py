import pgzrun

WIDTH = 800
HEIGHT = 500

blue_slab = Actor("blue-slab")
blue_slab.pos = (500,300)



def draw():
    screen.blit("grassland.png",(0,0))
    blue_slab.draw()

def update():

    if keyboard.left:
        blue_slab.x-=5

    elif keyboard.right:
        blue_slab.x+=5

    if blue_slab.x == WIDTH:
        blue_slab.pos = (600,300)

    elif blue_slab.x < 0:
        blue_slab.pos = (100,300)






pgzrun.go()