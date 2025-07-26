import pgzrun
import random

WIDTH = 800
HEIGHT = 500

gameOver = False

stars = ["red-star.png","orange-star.png","purple-star.png","yellow-star.png","blue-star.png"]
actor_stars = [ ]
animation = [ ]
selected_stars = []
level = 1

def makestars():
    gap = WIDTH/(level+2)

    for i in range(level):
       chosen_star = random.choice(stars)
       selected_stars.append(chosen_star)

    selected_stars.append("green-star.png")

    random.shuffle(selected_stars)

    for i in range(len(selected_stars)):
        star = Actor(selected_stars[i])
        actor_stars.append(star)
        star.pos = gap*(i+1),20

    animate_star()




def animate_star():
    for i in range(len(actor_stars)):
        ani = animate(actor_stars[i],duration = 7,y = HEIGHT+15)
        animation.append(ani)
        

def stop_animation():
    for ani in animation:
        ani.stop()

makestars()

def draw():
    if not gameOver:
        screen.blit("space.png",(0,0))
        for star in actor_stars:
            star.draw()
    else:
        screen.fill("blue")
        screen.draw.text("Game Over",center = (WIDTH//2 ,HEIGHT//2),fontsize = 20,color = "white")


def on_mouse_down(pos):
    global animation,selected_stars,level,actor_stars,gameOver
    for i in range(len(actor_stars)):
        if actor_stars[i].collidepoint(pos):
            if selected_stars[i] == "green-star.png":
                level+=1
                stop_animation()
                animation = []
                actor_stars = []
                selected_stars = []
                makestars()

            else:
                gameOver = True




            # stop_animation()
            # animation = [ ]
            # for i in range(len(actor_stars)):
            #     actor_stars[i].pos = gap*(i+1),20
            # animate_star()
            
        

def update():
    pass




pgzrun.go()