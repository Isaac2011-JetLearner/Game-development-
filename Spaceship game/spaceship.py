import pgzrun

WIDTH = 650
HEIGTH = 500

score = 0

game_over = False
x = 20

change = 5

lasers = []
wasps = []

for i in range(6):
  wasp = Actor("wasp")
  wasp.pos = x,25
  x+=60
  wasps.append(wasp)


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
    
    else:
       screen.blit("greenspace",(0,0))
       screen.draw.text("Score: " + str(score),(325,250), fontsize = 30 , color = "white")
       screen.draw.text("GAME OVER ",(325,200), fontsize = 30 , color = "white")
       
    

  



def update():
 global spaceship,score,change,game_over,x
 for wasp in wasps:
   wasp.x+=change
   wasp.y+=0.5
   
   if wasp.x>=600:
      change = -5

   if wasp.x <=0:
      change = +5
      
   if wasp.y > 500:
      wasp.y = 10
      

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
            score+=100
            break
 for wasp in wasps:
      if wasp.colliderect(spaceship):
         game_over = True

 if wasps == [ ]:
    for i in range(6):
        wasp = Actor("wasp")
        wasp.pos = x,25
        x+=70
        wasps.append(wasp)




def on_key_down():
  if keyboard.space:
   laser = Actor("laser")

   laser.pos = spaceship.pos

   lasers.append(laser)





pgzrun.go()