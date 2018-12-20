class Board() :
    def __init__(self,x,y) :
        self.x = x
        self.y = y
        self.size = 61
        #self.clicked = False
        self.colour = 255
        self.circle = False
        self.cross = False


    def show(self) :
        stroke(1)
        fill(self.colour)
        rect(self.x,self.y,self.size,self.size)
        if self.circle == True :
            fill(255,0,0)
            ellipse(self.x + self.size/2,self.y + self.size/2,30,30)             
        elif self.cross == True :
            fill(0,0,255)
            ellipse(self.x + self.size/2,self.y + self.size/2,30,30)



    def contains(self,x,y) :
        return ((x > self.x and x < self.x + self.size) and (y > self.y and y < self.y + self.size))

    def place(self,symbol) :
        if(symbol == "circle") :
            self.circle= True
        else :
            self.cross = True


    # def placeByCoordinate(self) :
    #     self.circle = True

def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)

class Check() :
    def __init__(self) :
        self.counter = 0
        self.xCircle = 0
        self.yCircle = 0
        self.xCross = 0
        self.yCross = 0

    def update(self,num) :
        self.counter = num
        
    def getCircleCoor(self,x,y) :
        self.xCircle = x
        self.yCircle = y
    
    def getCrossCoor(self,x,y) :
        self.xCross = x
        self.yCross = y
    
    def showInterface(self,board) :
        noStroke()
        fill(255)
        rect(670,200,350,150)
        stroke(0)
        fill(255)
        rect(680,260,510,250)
        fill(0)
        textSize(28)
        text("Board Array",860,250)
        textSize(18)
        text(str(board[0]),700,300)
        text(str(board[1]),700,320)
        text(str(board[2]),700,340)
        text(str(board[3]),700,360)
        text(str(board[4]),700,380)
        text(str(board[5]),700,400)
        text(str(board[6]),700,420)
        text(str(board[7]),700,440)
        text(str(board[8]),700,460)
        text(str(board[9]),700,480)
        
        fill(255)
        rect(680,80,510,70)
        fill(0)
        textSize(18)
        text("Circle piece placed at board[%d][%d]" %(self.yCircle,self.xCircle),700,110)
        text("Cross piece placed at board[%d][%d]" %(self.yCross,self.xCross),700,130)
        fill(255)
        noStroke()
        rect(680,30,510,40)
        fill(0)
        stroke(1)
        textSize(28)
        text("Locations",860,60)
        

    #check if there is a winning move
    #the question is :
    #how do we develop an algorithm that determines the winning move
    #PUT ALGORITHM HERE
    def check(self,circle_array,cross_array) :
        #Check if the pieces are in the same row
        #sort the array according to x values (sorting introduced)
        #after sorting then find 5 pieces that are in the same row
        #then check if each pieces are adjacent to each other
        #if they are then its a winning move

        #Do the same for column,check if the pieces are in the same columns
        #sort the array according to y values
        #after sorting then find 5 pieces that are in the same column
        #then check if each pieces are adjacent to each other
        #if they are then its a winning move
        pass
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

def checkSequence(tic_tac_toe) :
    for i in tic_tac_toe:
        print(i)
    row_counter=0#row increment
    column_counter=0#column increment
    sequence_counter=0
    x_counter=0
    o_counter=0
    board_size=len(tic_tac_toe)
    for row in range(len(tic_tac_toe)):
        while row_counter<len(tic_tac_toe):
            if tic_tac_toe[row][row_counter]=='x':
                x_counter+=1
            if tic_tac_toe[row][row_counter]=='o':
                o_counter+=1
            if x_counter==3:
                print("Cross win")
            elif o_counter==3:
                print("Circle win")
            row_counter+=1
        row_counter=0
        x_counter=0#reinitialize sequence counter
        o_counter=0

    for column in range(len(tic_tac_toe)):
        while column_counter<len(tic_tac_toe):
            if tic_tac_toe[column_counter][column]=='x':
                x_counter+=1
            if tic_tac_toe[column_counter][column]=='o':
                o_counter+=1
            if x_counter==3:
                print("You Win by 3o in column")
                exit(0)
            elif o_counter==3:
                print("You Win by 3o in column")
                exit(0)
            column_counter+=1
        column_counter=0
        x_counter=0#reinitialize sequence counter
        o_counter=0


    for diagonal in range(board_size):#count_diagonal from left
        if tic_tac_toe[diagonal][diagonal]=='x':
            x_counter+=1
        if tic_tac_toe[diagonal][diagonal]=='o':
            o_counter+=1
        if x_counter==3:
                print("You Win by 3X in left diagonal")
                exit(0)
        elif o_counter==3:
                print("You Win by 3o in right diagonal")
                exit(0)
    x_counter=0#reinitialize sequence counter
    o_counter=0

    for diagonal in range(board_size):#count_diagonal from right
        if tic_tac_toe[diagonal][board_size-1-diagonal]=='x':
            x_counter+=1
        if tic_tac_toe[diagonal][board_size-1-diagonal]=='o':
            o_counter+=1
        if x_counter==3:
                print("You Win by 3X in right diagonal")
                exit(0)
        elif o_counter==3:
                print("You Win by 3o in right diagonal")
                exit(0)

    

#---------------------------------MAIN CODE-------------------------------------

def setup():
    font = createFont("CMUTypewriter-Regular",24)
    textFont(font)
    row = 0
    array = []
    size(1202,602)
    background(255)
    x = 0
    y = 0
    #font = loadFont("CMUSerif-Roman-28.vlw")

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
        x = int(input("Enter circle's row value : "))
        y = int(input("Enter circle's column value : "))
        if x > 10 or y > 10 :
            print("Out of range! Enter again!")
            x = int(input("Enter circle's row value : "))
            y = int(input("Enter circle's column value : "))
        else :
            board[y][x].circle = True
            check.getCircleCoor(x,y)
            #put coordinates of the piece in the array 
            circle_array.append([y,x])
            circle_object.append(board[y][x])
            show_board[x][y] = "o"
            #change turn to cross's turn
            checkSequence(show_board)
            check.update(1)

    elif check.counter == 1 :
        x = int(input("Enter cross's row value : "))
        y = int(input("Enter cross's column value : "))
        if x > 10 or y > 10 :
            print("Out of range! Enter again!")
            x = int(input("Enter cross's row value : "))
            y = int(input("Enter cross's column value : "))
        else :
            board[y][x].cross = True
            check.getCrossCoor(x,y)
            show_board[x][y] = "x"
            checkSequence(show_board)
            cross_array.append([y,x])
            cross_object.append(board[y][x])
            check.update(0)

    for i in range(len(board)) :
        for j in range(len(board[i])) :
            board[i][j].show()
    check.showInterface(show_board)
