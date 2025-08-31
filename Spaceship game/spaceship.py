import pgzrun
import random
WIDTH = 650
HEIGTH = 500

score = 0
Lives = 3

x = 20

lasers = []
wasps = []

for i in range(6):
  wasp = Actor("wasp")
  wasp.pos = x,25
  x+=60
  wasps.append(wasp)

game_over = False

spaceship = Actor("spaceship") 

spaceship.pos = (325,475)





def draw():
 if not game_over:
    screen.blit("spacebackground",(0,0))
    spaceship.draw()
    
    for wasp in wasps:
      wasp.draw()
    for laser in lasers:
      laser.draw()

    screen.draw.text("Score: " + str(score),(10,10), fontsize = 30 , color = "white")
    screen.draw.text("Lives: " + str(Lives),(560,10), fontsize = 30 , color = "white")

 elif game_over:
  screen.blit("greenspace",(0,0))
  screen.draw.text("Score: " + str(score),(325,250), fontsize = 30 , color = "white")
  screen.draw.text("GAME OVER",(325,200), fontsize = 30 , color = "white")
  screen.draw.text("Lives: " + str(Lives),(325,300), fontsize = 30 , color = "white")
  



def update():
 global spaceship,score,game_over,Lives
 if game_over:
   return
 for wasp in wasps:
   wasp.y+=2.5
   if wasp.y > 475:
      wasp.y = 25
      wasp.x = random.randint(0,600)

 if keyboard.left:
   spaceship.x-=5

 if spaceship.x >=625:
   spaceship.x = 625

 if spaceship.x <=20:
    spaceship.x = 20

 if keyboard.right:
    spaceship.x+=5

 for laser in lasers:
   laser.y-=4

   if laser.y <= 0:
      lasers.remove(laser)
   
 for laser in lasers:
   for wasp in wasps:
      if laser.colliderect(wasp):
            wasps.remove(wasp)
            lasers.remove(laser)
            score+=1
            break
 for wasp in wasps:
   if wasp.colliderect(spaceship):
      wasps.remove(wasp)
      if wasp.y == 500:
        Lives-=1
        break
   if Lives == 0:
      game_over = True





def on_key_down():
  if keyboard.space:
   laser = Actor("laser")

   laser.pos = spaceship.pos

   lasers.append(laser)





pgzrun.go()