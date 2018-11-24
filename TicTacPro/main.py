from p5 import *
from board import Board
from board import Check

#--------------------------------VARIABLES--------------------------------------
#board array stores objects and show_board shows the state of the board
board = []
show_board = [["E" for j in range(10)] for i in range(10)]

#number of squares
count = 10
#scale of squares in pixels
scale = 61

column = 0

#check is used to check status of each player's turn
#it is also used to check how many pieces are in the board
check = Check()

#declare values for x and y
x = 0
y = 0

#array to track pieces
circle_array = []
cross_array = []
circle_object = []
cross_object = []

#---------------------------------MAIN CODE-------------------------------------

#point and click featuer
def mouse_pressed() :
    #every time the user places a new piece
    #run a check for all pieces with their positions
    #check if there is a winning move
    #if there is draw a line in the direction of that winning move
    #or just change the fill to signify the winning spaces
    for i in range(len(board)) :
        for j in range(len(board[0])) :
            if(board[i][j].contains(mouse_x,mouse_y)) :
                if(check.counter == 0) :
                    #create a new piece circle and put it in circle array
                    #to keep track of how many circles
                    #and their positions for checking
                    #circle_array.append(board[i][j])
                    circle_array.append([board[i][j].x,board[i][j].y])
                    board[i][j].place("circle")
                    board[i][j].clicked = True
                    board[i][j].colour = 200
                    check.update(1)
                elif(check.counter == 1) :
                    #the same goes for cross pieces
                    #cross_array.append(board[i][j])
                    cross_array.append([board[i][j].x,board[i][j].y])
                    board[i][j].place("cross")
                    board[i][j].colour = 200
                    check.update(0)
    print("circle array : ",circle_array)
    print("cross array : ",cross_array)
    # print(board)

def setup():
    row = 0
    array = []
    size(int(601),int(601))
    background(255)
    x = 0
    y = 0

    #create board
    while row <= 10 :
        x = 0
        column = 0
        array = []
        while column <= 10 :
            cell = Board(x,y)
            cell.size = scale
            array.append(cell)
            column += 1
            x += scale - 1
        board.append(array)
        y += scale - 1
        row += 1

    return board
                    
def draw():
    fill(0)
    if check.counter == 0 :
        x = int(input("Its CIRCLE's turn. Enter x value to place piece : "))
        y = int(input("Enter y value : "))
        board[y][x].circle = True
        #put coordinates of the piece in the array 
        circle_array.append([y,x])
        circle_object.append(board[y][x])
        show_board[x][y] = "O"
        #change turn to cross's turn
        check.update(1)

    elif check.counter == 1 :
        x = int(input("Its CROSS's turn. Enter x value to place piece : "))
        y = int(input("Enter y value : "))
        board[y][x].cross = True
        show_board[x][y] = "X"
        cross_array.append([y,x])
        cross_object.append(board[y][x])
        check.update(0)

    for i in range(len(board)) :
        for j in range(len(board[i])) :
            board[i][j].show()
    print(show_board)

run()

