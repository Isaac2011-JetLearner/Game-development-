import pgzrun
def read_questions():

    questions = []

    with open("lesson 6\questions.txt","r") as file:
        data = file.readlines()

        for line in data:
            line_split = line.split(",")

            question = {
                "question": line_split[0],
                "options" : line_split[1:5],
                "answer" : int(line_split[5])
            }

            questions.append(question)
    
    # print(questions)
    

WIDTH = 600
HEIGHT = 450


x = 300
y = 15


read_questions()






r_1 = Rect((20,50),(450,100))

r_2 = Rect((490,50),(100,100))

r_3 = Rect((20,180),(210,100))

r_4 = Rect((20,310),(210,100))

r_5 = Rect((260,310),(210,100))

r_6 = Rect((260,180),(210,100))

r_7 = Rect((490,180),(100,300))


def draw():
    screen.fill(color = "black")
    screen.draw.filled_rect(r_1, color = "blue")
    screen.draw.filled_rect(r_2, color = "orange")
    screen.draw.filled_rect(r_3, color = "orange")
    screen.draw.filled_rect(r_4, color = "orange")
    screen.draw.filled_rect(r_5, color = "orange")
    screen.draw.filled_rect(r_6, color = "orange")
    screen.draw.filled_rect(r_7, color = "darkgreen")



    screen.draw.text("Welcome To Quiz Master ",(x,y),fontsize = 50,color = "white")


def update():
    pass
    global x
    x-=3

    if x <= -400:
        x = 700

   





pgzrun.go()





# with open("lesson 6/questions.txt","r")as file:
#     data = file.readlines()
#     for line in data:
#         print(line)