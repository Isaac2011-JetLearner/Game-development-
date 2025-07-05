import pgzrun
import random
WIDHT = 500
HEIGHT = 500
satalites = []
start_cords = [ ]
end_cords = []
next_index = 1

def create_satalites():
    for i in range(8):
        sat = Actor("satalite")
        satalites.append(sat)
        sat.pos = random.randint(50,450),random.randint(50,450)


create_satalites()

def draw():
    screen.blit("background",(0,0))
    # screen.draw.line((10,34),(90,64),(255,255,255))
    for i in range(8):
        satalites[i].draw()
        screen.draw.text(str(i+1),(satalites[i].x,satalites[i].y+15),fontsize = 20, color = (255,255,255),)
    
    for i in range(len(start_cords)):
        screen.draw.line(start_cords[i],end_cords[i],(255,255,255))

def on_mouse_down(pos):
    global next_index
    if satalites[next_index].collidepoint(pos):
        start = satalites[next_index-1].pos
        end = satalites[next_index].pos
        start_cords.append(start)
        end_cords.append(end)
        next_index+=1
       

    



def update():
    pass  



pgzrun.go() 