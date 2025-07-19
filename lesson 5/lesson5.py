import pgzrun

WIDTH = 800
HEIGHT = 500

stars = ["red-star.png","green-star.png"]
actor_stars = [ ]
animation = [ ]


gap = WIDTH/3

for i in range(len(stars)):
    star = Actor(stars[i])
    actor_stars.append(star)
    star.pos = gap*(i+1),20

def animate_star():
    for star in actor_stars:
        ani = animate(star,duration = 7,y = HEIGHT+15)
        animation.append(ani)

def stop_animation():
    for ani in animation:
        ani.stop()

animate_star()

def draw():
    screen.blit("space.png",(0,0))
    for star in actor_stars:
        star.draw()


def on_mouse_down(pos):
    global animation
    for i in range(len(actor_stars)):
        if actor_stars[i].collidepoint(pos):
            stop_animation()
            animation = [ ]
            animate_star()
            
        

def update():
    pass




pgzrun.go()