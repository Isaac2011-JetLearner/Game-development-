import pgzrun
import random

WIDTH = 800
HEIGHT = 500

score = 0

game_over = False  

blue_slab = Actor("blue-slab")
blue_slab.pos = (400,350)

green_ball = Actor("green-ball")
green_ball.pos = (0,0)

change_x = 2
change_y = 2



def draw():
    if not game_over:
        screen.blit("grassland.png", (0,0))
        blue_slab.draw()
        green_ball.draw()
        screen.draw.text(str(score),(10, 10), fontsize=30, color="white")
    
    else:
        screen.fill("green")
        screen.draw.text("game over", center=(WIDTH // 2, HEIGHT // 2), fontsize=50, color="white")

def update():
    global change_y, change_x, score, game_over
    
    if keyboard.left:
         blue_slab.x -= 5
    elif keyboard.right:
        blue_slab.x += 5

    if blue_slab.x >= WIDTH:
        blue_slab.pos = (600, 300)
    elif blue_slab.x <= 0:
        blue_slab.pos = (100, 300)
    
    green_ball.x+= change_x
    green_ball.y+= change_y

    if green_ball.x <= 0 or green_ball.x >= WIDTH:
        change_x*=-1
    if green_ball.y <= 0:
        change_y*=-1

    
    if green_ball.colliderect(blue_slab):
        change_y*=-1 
        score += 1

    if green_ball.y > HEIGHT:
        game_over = True

pgzrun.go()
