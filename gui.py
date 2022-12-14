import turtle
import time
from tkinter import *

scn = turtle.Screen()
scn.title(" ~ THE SUDOKU SOLVER ~ ")
scn.setup(600, 600)
scn.tracer(0)
colchange = 0
count = 0
canvas = scn.getcanvas()

test_pen = turtle.Turtle()
test_pen.speed(0)
done = False


pos_x, pos_y = -225, 225

board = [
    [1, 0, 0, 4, 8, 9, 0, 0, 6],
    [7, 3, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 0, 0, 0, 1, 2, 9, 5],
    [0, 0, 7, 1, 2, 0, 6, 0, 0],
    [5, 0, 0, 7, 0, 3, 0, 0, 8],
    [0, 0, 6, 0, 9, 5, 7, 0, 0],
    [9, 1, 4, 6, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 3, 7],
    [8, 0, 0, 5, 1, 2, 0, 0, 4]
]                                                   # Problem Statement

fixed = []
for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            temp = [i, j]
            fixed.append(temp)

turtles = [[0 for i in range(9)] for j in range(9)]

for i in range(9):
    for j in range(9):
        turtles[i][j] = turtle.Turtle()

def move(x, y, my_pen):
    my_pen.pu()
    my_pen.goto(x, y)
    my_pen.pd()


def change_theme(deff=None):

    global colchange

    if colchange % 2 == 0:

        scn.bgcolor('black')
        colchange += 1

    else:
        scn.bgcolor('white')
        colchange += 1

    if deff is None:
        run()

# To print the Grid Layout on the screen

def theme_button():

    button = Button(canvas.master, text="Theme", command=change_theme)
    button.pack()
    button.place(x=10, y=10)  # place the button anywhere on the screen

def start_button():

    button = Button(canvas.master, text="Start", command=run)
    button.pack()
    button.place(x=100, y=10)  # place the button anywhere on the screen

def layout(x, y,col):

    scn.tracer(0)
    my_pen = turtle.Turtle()

    if col % 2: my_pen.color('white')
    else: my_pen.color('black')

    move(x, y, my_pen)
    my_pen.right(90)

    for i in range(10):
        if i % 3 == 0:
            my_pen.pensize(5)
            my_pen.fd(450)
            x += 50
            move(x, y, my_pen)

        else:
            my_pen.pensize(2)
            my_pen.fd(450)
            x += 50
            move(x, y, my_pen)

    my_pen.left(90)
    x, y = -225, 225
    move(x, y, my_pen)

    for i in range(10):
        if i % 3 == 0:
            my_pen.pensize(5)
            my_pen.fd(450)
            y -= 50
            move(x, y, my_pen)

        else:
            my_pen.pensize(2)
            my_pen.fd(450)
            y -= 50
            move(x, y, my_pen)


# To Print the initial elements in the problem statement

def my_board(brd, x, y,col):

    x += 30
    y += 10
    for i in range(9):
        y -= 50
        x = -195
        for j in range(9):
            if [i, j] in fixed:

                if col % 2:
                    turtles[i][j].color("white")

                else:
                    turtles[i][j].color("black")

                scn.tracer(0)
            else:
                turtles[i][j].color("blue")
            move(x, y, turtles[i][j])
            x += 50
            if brd[i][j] != 0:
                turtles[i][j].write(brd[i][j], align="right", font=("Comic Sans MS", 15, "bold"))


# To Print a step by step solution of the Board

def Solution(brd, x, y, row, column):
    x += 30
    y += 10
    for i in range(9):
        y -= 50
        x = -195
        for j in range(9):
            if [i, j] in fixed:

                if colchange % 2 == 0:

                    turtles[i][j].color("black")

                else:
                    turtles[i][j].color('white')

                scn.tracer(0)
            else:

                turtles[i][j].color("blue")

            move(x, y, turtles[i][j])
            x += 50
            if brd[i][j] == 0:
                #time.sleep(.01)
                turtles[i][j].clear()
                return
            if i == row and j == column:
                #time.sleep(.01)
                turtles[i][j].write(brd[i][j], align="right", font=("Comic Sans MS", 15, "bold"))


# Function to check the valid entry of number

def check(brd, num_row, num_column, entry):

    # For checking in the small 3*3 matrix
    matrix_i = num_row // 3
    matrix_j = num_column // 3
    for i in range(matrix_i * 3, matrix_i * 3 + 3):
        for j in range(matrix_j * 3, matrix_j * 3 + 3):
            if brd[i][j] == entry and i != num_row and j != num_column:
                return False

    # For checking along the column
    for row in range(len(brd)):
        if brd[row][num_column] == entry and row != num_row:
            return False

    # For checking along the row
    for column in range(len(brd[num_row])):
        if brd[num_row][column] == entry and column != num_column:
            return False

    return True


# To Solve the board

def visualise(brd):
    global count
    count += 1
    row, column = -1, -1
    for i in range(len(brd)):
        for j in range(len(brd[i])):
            if brd[i][j] == 0:
                row, column = i, j
                break
        if row != -1:
            break

    if row == -1:                                               # Base Statement
        return True

    for i in range(9):
        if check(brd, row, column, i + 1):
            brd[row][column] = i + 1
            layout(pos_x, pos_y,colchange)
            Solution(brd, pos_x, pos_y, row, column)

            if visualise(brd):                                  # Recursive statement
                return True

            brd[row][column] = 0
            layout(pos_x, pos_y,colchange)
            Solution(brd, pos_x, pos_y, row, column)
    return False


# To Trigger the 'visualise' function on key press

def step():
    global done

    visualise(board)
    scn.clear()
    move(220, -280, test_pen)
    # test_pen.write("By Akshit", align="center", font=("Cooper Black", 11, "normal"))
    layout(pos_x, pos_y,colchange)
    if colchange:scn.bgcolor('black')
    my_board(board, pos_x, pos_y,colchange)
    test_pen.color("red")
    move(0, 260, test_pen)
    test_pen.write("Recursive Steps Taken = "+str(count), align="center", font=("Century", 15, "bold"))
    done = True
    #change_theme()

def run():

    #scn.clear()
    layout(pos_x, pos_y,colchange)
    my_board(board, pos_x, pos_y,colchange)
    move(220, -290, test_pen)
    # test_pen.write("By Akshit", align="center", font=("Cooper Black", 11, "normal"))
    move(0, 260, test_pen)
    test_pen.color("red")

    if not done:

        test_pen.write("Press 'SPACE BAR' to visualise the solution", align="center", font=("Century", 15, "bold"))

    test_pen.color("green")

    scn.onkeypress(step, "space")

theme_button()
run()

scn.listen()
turtle.done()
