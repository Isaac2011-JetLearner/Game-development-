import random
treasure = []

tr_row = random.randint(0,3)
tr_coloum = random.randint(0,3)

def treause_place():
    for i in range(4):
        row = ["-"]*4
        treasure.append(row)

    for row in treasure:
        print(" ".join(row) )

treause_place()

row_guess = int(input("enter a row number (0-3): "))
coloum_guess = int(input("enter a coloum number (0-3): "))


if tr_row < row_guess:
    print("hint: go up")

elif tr_row > row_guess:
    print("hint: go down")


if tr_coloum < coloum_guess:
    print("hint: go right")

elif tr_coloum > coloum_guess: 
    print("hint: go left")

if row_guess != tr_row and coloum_guess != tr_coloum:
    row_guess = int(input("enter a row number (0-3): "))
    coloum_guess = int(input("enter a coloum number (0-3): "))

elif row_guess != tr_row or coloum_guess != tr_coloum:
    row_guess = int(input("enter a row number (0-3): "))
    coloum_guess = int(input("enter a coloum number (0-3): "))

if row_guess == tr_row and coloum_guess == tr_coloum:
    print("Congratulations you have found the Treasure")



