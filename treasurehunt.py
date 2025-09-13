import random
treasure = []

tr_row = random.randint(0,3)
tr_coloum = random.randint(0,3)

def treause_place():
    for i in range(4):
        row = ["-"]*4
        treasure.append(row)

def draw_tr():
    for row in treasure:
        print(" ".join(row) )

treause_place()


while True:
    draw_tr()
    row_guess = int(input("enter a row number (0-3): "))
    coloum_guess = int(input("enter a coloum number (0-3): "))
    treasure[row_guess][coloum_guess] = "x"

    if tr_row < row_guess:
        print("hint: go up")

    elif tr_row > row_guess:
        print("hint: go down")


    if tr_coloum < coloum_guess:
        print("hint: go left")

    elif tr_coloum > coloum_guess: 
        print("hint: go right ")

    if row_guess == tr_row and coloum_guess == tr_coloum:
        print("Congratulations you have found the Treasure")
        draw_tr()
        break


