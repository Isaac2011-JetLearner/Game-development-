import pgzrun

WIDTH = 600
HEIGHT = 450


r_1 = Rect((20,50),(450,100))

r_2 = Rect((490,50),(100,100))

r_3 = Rect((20,180),(210,100))

r_4 = Rect((20,310),(210,100))

r_5 = Rect((260,310),(210,100))

r_6 = Rect((260,180),(210,100))

r_7 = Rect((490,180),(100,300))


def draw():
    screen.draw.filled_rect(r_1, color = "blue")
    screen.draw.filled_rect(r_2, color = "orange")
    screen.draw.filled_rect(r_3, color = "orange")
    screen.draw.filled_rect(r_4, color = "orange")
    screen.draw.filled_rect(r_5, color = "orange")
    screen.draw.filled_rect(r_6, color = "orange")
    screen.draw.filled_rect(r_7, color = "darkgreen")

    screen.draw.text("hello",(225,90),fontsize = 50,color = "white")




pgzrun.go()





# with open("lesson 6/questions.txt","r")as file:
#     data = file.readlines()
#     for line in data:
#         print(line)