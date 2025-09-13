board = []

def make_board():
    for i in range(3):
        row = [" "]*3
        board.append(row)
def draw_row():
    for row in board:
        print("| ".join(row))
        print("-"*10)

make_board()
draw_row()

turn = "x"

while True:
    ask_row = int(input("enter a row number "))
    ask_coloum = int(input("enter a coloun number "))
    board[ask_row][ask_coloum] = turn

    if turn == "x":
        turn = "o"
    else:
        turn = "x"

    draw_row()

