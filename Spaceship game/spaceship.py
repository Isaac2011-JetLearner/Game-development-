import pgzrun
import random
WIDTH = 650
HIGTH = 500

score = 0
Lives = 3

game_over = False

spaceship = Actor("spaceship") 

spaceship.pos = (325,475)

wasp = Actor("wasp")

wasp.pos = random.randint(0,600),25

laser = Actor("laser")

laser.pos = spaceship.pos


def draw():
 if not game_over:
    screen.blit("spacebackground",(0,0))
    spaceship.draw()
    wasp.draw()
    laser.draw()

    screen.draw.text("Score: " + str(score),(10,10), fontsize = 30 , color = "white")
    screen.draw.text("Lives: " + str(Lives),(560,10), fontsize = 30 , color = "white")

 elif game_over:
  screen.blit("greenspace",(0,0))
  screen.draw.text("Score: " + str(score),(325,250), fontsize = 30 , color = "white")
  screen.draw.text("Gameover",(325,200), fontsize = 30 , color = "white")
  screen.draw.text("Lives: " + str(Lives),(325,300), fontsize = 30 , color = "white")
  



def update():
 global wasp,spaceship,laser,score,game_over,Lives
 
 wasp.y+=2.5
 if wasp.y > 475:
  wasp.y = 25

 if keyboard.left:
   spaceship.x-=5

 if spaceship.x >=625:
   spaceship.x = 625

 if spaceship.x <=20:
    spaceship.x = 20

 if keyboard.right:
    spaceship.x+=5

 laser.y-=4

 if laser.y <= 30:
  laser.x = spaceship.x
  laser.y = spaceship.y
  

 if laser.colliderect(wasp):
  wasp.pos = random.randint(0,600),25
  laser.pos = spaceship.pos
  score+=1

 if wasp.colliderect(spaceship):
  Lives-=1
 
 if Lives == 0:
  game_over = True




 pass








pgzrun.go()