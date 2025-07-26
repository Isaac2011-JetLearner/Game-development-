import pgzrun
import random

WIDTH = 800
HEIGHT = 500

stars = ["red-star.png","green-star.png","orange-star.png","purple-star.png","yellow-star.png","blue-star.png"]
actor_stars = [ ]
animation = [ ]

level = 1
gap = WIDTH/(level+2)

for i in range(level):
    chosen_star = random.choice(stars)
    star = Actor(chosen_star)
    actor_stars.append(star)

green_star = Actor("green-star.png")   

actor_stars.append(green_star)

random.shuffle(actor_stars)

for i in range(len(actor_stars)):
    actor_stars[i].pos = gap*(i+1),20

def animate_star():
    for i in range(len(actor_stars)):
        ani = animate(actor_stars[i],duration = 7,y = HEIGHT+15)
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
            for i in range(len(actor_stars)):
                actor_stars[i].pos = gap*(i+1),20
            animate_star()
            
        

def update():
    pass




pgzrun.go()