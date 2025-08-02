import pgzrun
import random

WIDTH = 850
HEIGHT = 600

score = 0
lives = 5

GameOver = False




ship = Actor("ship")
ship.pos = (425,500)

coin = Actor("goldcoin")
coin.pos = (random.randint(20,780),30)

skull = Actor("skull")
skull.pos = (random.randint(20,780),30)

bomb = Actor("bomb")
bomb.pos = (random.randint(20,780),30)




def draw():
    if GameOver == False:
        screen.blit("piratebackground.png",(0,0))
        ship.draw()
        coin.draw()
        bomb.draw()
        skull.draw()

    else:
        screen.fill("blue")
        screen.draw.text("Game Over",center = (WIDTH//2 ,HEIGHT//2),fontsize = 20,color = "white")


    screen.draw.text("Score = "+ str(score),(10,10),fontsize=30,color = "white")

    screen.draw.text("Lives = "+ str(lives),(750,10),fontsize=30,color = "white")



def update():
    global score,lives,GameOver

    pass

    if keyboard.left:
        ship.x-=5
    
    if keyboard.right:
        ship.x+=5

    if ship.x < 60:
        ship.x = 60

    if ship.x > 790:
        ship.x = 790

    coin.y+=3 + score/5
    if coin.y > 600:
        coin.pos = (random.randint(20,780),30)

    if ship.colliderect(coin):
        score+=1
        coin.pos = (random.randint(20,780),30)


    skull.y+=3
    if skull.y > 600:
        skull.pos = (random.randint(20,780),30)

    if ship.colliderect(skull):
        lives-=1
        score-=1
        skull.pos = (random.randint(20,780),30)


    bomb.y+=3
    if bomb.y > 600:
        bomb.pos = (random.randint(20,780),30)
    
    if ship.colliderect(bomb):
        score-=1
        lives-=1
        bomb.pos = (random.randint(20,780),30)

    if lives <= 0:
        GameOver = True


    

pgzrun.go()





