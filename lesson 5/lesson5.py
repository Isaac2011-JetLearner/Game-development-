import pgzrun

WIDTH = 800
HEIGHT = 500

stars = ["red-star.png","green-star.png"]
actor_stars = [ ]


gap = WIDTH/3

for i in range(len(stars)):
    star = Actor(stars[i])
    actor_stars.append(star)
    star.pos = gap*(i+1),20

for star in actor_stars:
    animate(star,duration = 7,y = HEIGHT+15)


def draw():
    screen.blit("space.png",(0,0))
    for star in actor_stars:
        star.draw()


def on_mouse_down(pos):
    for i in range(len(actor_stars)):
        if actor_stars[i].collidepoint(pos):
            actor_stars[i].y = 20
        

def update():
    pass




pgzrun.go()