add_library('controlP5')

#----------------------------GLOBAL VARIABLES------------------------------------
class Board() :
    def __init__(self,x,y) :
        self.size = 61
        self.x = x * self.size
        self.y = y * self.size
        self.r = 200
        self.g = 200
        self.b = 200
        self.circle = False
        self.cross = False
        self.sequence = False
        
    def show(self) :
        strokeWeight(8)
        stroke(235,242,40)
        fill(self.r,self.g,self.b)
        rect(self.x,self.y,self.size,self.size)
        if self.circle == True :
            fill(self.r,self.g,self.b)
            rect(self.x,self.y,self.size,self.size)
            image(imgCircle,self.x+11,self.y+11)             
        elif self.cross == True :
            fill(self.r,self.g,self.b)
            rect(self.x,self.y,self.size,self.size)
            image(imgCross,self.x+13,self.y+13)

    def contains(self,x,y) :
        return ((x > self.x and x < self.x + self.size) and (y > self.y and y < self.y + self.size))
    

def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)

class Check() :
    def __init__(self) :
        self.counter = 0
        self.xCircle,self.yCircle = 0,0
        self.xCross,self.yCross = 0,0
        self.circleS,self.crossS = 0,0
        self.circleScore = "Circle player has %d score " %self.circleS
        self.crossScore = "Cross player has %d score " %self.crossS
        self.circlePosition = "No circle placed on board"
        self.crossPosition = "No cross placed on board"
        self.circleStatus = ""
        self.crossStatus = ""
        self.message = ""
        self.mode = "idle"
        self.circleSPUsed = False
        self.crossSPUsed = False

    def checkSPUsed(self,counter):
        if counter == 0:
            return self.circleSPUsed
        else:
            return self.crossSPUsed

    def update(self,num) :
        self.counter = num
        
    def getCircleCoor(self,x,y) :
        self.xCircle = x
        self.yCircle = y
    
    def getCrossCoor(self,x,y) :
        self.xCross = x
        self.yCross = y
    
    def sequenceFound(self,board,sequence,player,sequenceType):
        for i in range(len(sequence)):
            board[sequence[i][0]][sequence[i][1]].r = 150
            board[sequence[i][0]][sequence[i][1]].g = 150
            board[sequence[i][0]][sequence[i][1]].b = 150
            board[sequence[i][0]][sequence[i][1]].sequence = True
        if player == "O":
            self.circleS += 1
            self.circleScore = "Circle player has %d score " %self.circleS
        else:
            self.crossS += 1
            self.circleScore = "Cross player has %d score " %self.crossS
    
    def buttonContains(self,x,y) :
        return ((x >= 1153 and x <= 1300) and (y >= 685 and y <= 732))
    
    def showMessage(self,counter,x,y,mode):
        if mode == "errorInput":
            self.message = "Invalid input!\nEnter numbers only!"
        elif mode == "errorRange":
            self.message = "Invalid range!\nEnter numbers between 0-9 "
        elif mode == "winMessage":
            if counter == 0:
                self.message = "Circle wins the round!"
            else:
                self.message = "Cross wins the round!"
        elif mode == "idle":
            if counter == 0:
                self.message = "Its circle player's turn\nEnter row and column"
            else:
                self.message = "Its cross player's turn\nEnter row and column"
        elif mode == "superpowerPosition":
            if counter == 0:
                self.message = "Enter row OR column value\nto change position of cross"
            else:
                self.message = "Enter row OR column value\nto change position of circle"
        elif mode == "superpowerNoPosition":
            self.message = "No position to change!"
        elif mode == "SPUsed":
            self.message = "Superpower has been used!\nCannot use superpower!"
        elif mode == "sequenceFound":
            self.message = "Invalid row and column values!\nCannot change piece in a sequence!"
        elif mode == "pieceFound":
            self.message = "Cannot place piece at there!\nRow and column occupied!"
        elif mode == "reverseMode":
            self.message = "Reverse superpower used!\nEnter row and column to reverse"
        elif mode == "errorReverseInput":
            self.message = "Error input!\nEnter either row or column to reverse"
        elif mode == "reverseSuccessful":
            self.message = "Reverse successful!\nEnter next player's row and column"
        
    def showInterface(self,board) :
        image(imgTitle,450,10)
        image(imgCredits,900,40)
        image(imgMenu,710,110)
        image(imgButton,1150,680)
        fill(0)
        textSize(25)
        textFont(font2)
        fill(255,0,0)
        #==============================SCORE TEXT=============================
        text(self.circleScore,960,145)
        fill(82,218,221)
        text(self.crossScore,960,175)
        #==============================STATUS TEXT=============================
        fill(0)
        text(self.circlePosition,960,220)
        text(self.crossPosition,960,245)
        textSize(25)
        text("ROW",740,720)
        text("COLUMN",910,720)
        textSize(25)
        text(self.message,740,585)
        
        #===============================ARRAY NUMBERS==========================
        #horizontal number lines
        textSize(25);
        fill(0)
        text("0",79,102)
        text("1",140,102)
        text("2",201,102)
        text("3",262,102)
        text("4",323,102)
        text("5",384,102)
        text("6",445,102)
        text("7",506,102)
        text("8",567,102)
        text("9",628,102)
        #vertical number lines
        text("0",15,163)
        text("1",15,224)
        text("2",15,285)
        text("3",15,346)
        text("4",15,407)
        text("5",15,468)
        text("6",15,529)
        text("7",15,590)
        text("8",15,651)
        text("9",15,712)
        textSize(18)
        
        #==================ARRAY BOARD========================
        fill(232,252,45)
        textSize(24)
        text("ARRAY LIST",730,295)
        fill(0)
        textSize(18)
        text(str(board[0]),730,320)
        text(str(board[1]),730,340)
        text(str(board[2]),730,360)
        text(str(board[3]),730,380)
        text(str(board[4]),730,400)
        text(str(board[5]),730,420)
        text(str(board[6]),730,440)
        text(str(board[7]),730,460)
        text(str(board[8]),730,480)
        text(str(board[9]),730,500)
        
        #==============================SUPERPOWERS===============================
        image(imgPosition,1140,330)
        image(imgReverse,1140,440)
        fill(0)
        textSize(24)
        fill(255,0,0)
        text("SUPERPOWERS",1150,295)
        fill(0)
        textSize(18)
        text("Change Position",1130,325)
        text("Reverse",1130,430)
        
class Superpower():
    def __init__(self):
        self.superpowerMode = False
        self.reverseMode = False
    def changePosition(self,counter,board,boardObject):
        if(checkPieces(counter,board)):
            check.mode = "superpowerPosition"
            highlightSquares(counter,board,boardObject)
            self.superpowerMode = True
        else:
            check.mode = "superpowerNoPosition"
        
    def containsPosition(self,x,y):
        return ((x >= 1143 and x <= 1319) and (y >= 335 and y <= 388))
    
    def containsReverse(self,x,y):
        return ((x >= 1146 and x <= 1319) and (y >= 443 and y <= 500)) 
    
    
    def restoreSquares(self,boardObject):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if boardObject[i][j].sequence == False:
                    boardObject[i][j].r = 200
                    boardObject[i][j].g = 200
                    boardObject[i][j].b = 200
                

def checkPieces(counter,board):
    check = "X" if counter == 0 else "O"
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == check:
                return True
    return False
        
def highlightSquares(counter,board,boardObject):
    if counter == 0:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "X" and boardObject[i][j].sequence == False:
                    boardObject[i][j].r = 102
                    boardObject[i][j].g = 45
                    boardObject[i][j].b = 145
    elif counter == 1:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O" and boardObject[i][j].sequence == False:
                    boardObject[i][j].r = 102
                    boardObject[i][j].g = 45
                    boardObject[i][j].b = 145

def reverseRowColumn(show_board,row,column):
    if column == "":
        show_board[row][0],show_board[row][9] = show_board[row][9],show_board[row][0]
        show_board[row][1],show_board[row][8] = show_board[row][8],show_board[row][1]
        show_board[row][2],show_board[row][7] = show_board[row][7],show_board[row][2]
        show_board[row][3],show_board[row][6] = show_board[row][6],show_board[row][3]
        show_board[row][4],show_board[row][5] = show_board[row][5],show_board[row][4]
    elif row == "":
        show_board[0][column],show_board[9][column] = show_board[9][column],show_board[0][column]
        show_board[1][column],show_board[8][column] = show_board[8][column],show_board[1][column]
        show_board[2][column],show_board[7][column] = show_board[7][column],show_board[2][column]
        show_board[3][column],show_board[6][column] = show_board[6][column],show_board[3][column]
        show_board[4][column],show_board[5][column] = show_board[5][column],show_board[4][column]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if show_board[i][j] == "E":
                board[i][j].circle = False
                board[i][j].cross = False
            elif show_board[i][j] == "X":
                board[i][j].circle = False
                board[i][j].cross = True
            elif show_board[i][j] == "O":
                board[i][j].circle = True
                board[i][j].cross = False
    
    return show_board
        
        
        
#--------------------------------VARIABLES--------------------------------------
#board array stores objects and show_board shows the state of the board
board = []
show_board = [["E" for j in range(10)] for i in range(10)]

#scale of squares in pixels
scale = 61

#check is used to check status of each player's turn
#it is also used to check how many pieces are in the board
check = Check()

def checkSequence(board,array,player):
    horizontal,vertical,leftDiagonal,rightDiagonal = 0,0,0,0
    horizontalArray,verticalArray,leftDiagonalArray,rightDiagonalArray = [],[],[],[]
    for i in range(len(array)-1):
        for j in range(len(array[i])-1):
            if array[i][j] == player:
                if array[i+1][j] == player:
                    vertical += 1
                    if i+1 == len(array)-1:
                        verticalArray.append([i,j])
                        verticalArray.append([i+1,j])
                    else:
                        verticalArray.append([i,j])
                    if vertical == 4:
                        verticalArray.append([i+1,j])
                        check.sequenceFound(board,verticalArray,player,"Vertical")
                        vertical = 0
                if array[i][j+1] == player:
                    horizontal += 1
                    if j+1 == len(array)-1:
                        horizontalArray.append([i,j])
                        horizontalArray.append([i,j+1])
                    else:
                        horizontalArray.append([i,j])
                    if horizontal == 4:
                        horizontalArray.append([i,j+1])
                        check.sequenceFound(board,horizontalArray,player,"Horizontal")
                        horizontal = 0
                if array[i+1][j+1] == player:
                    rightDiagonal += 1
                    if i+1 == len(array)-1:
                        rightDiagonalArray.append([i,j])
                        rightDiagonalArray.append([i+1,j+1])
                    else:
                        rightDiagonalArray.append([i,j])
                    if rightDiagonal == 4:
                        rightDiagonalArray.append([i+1,j+1])
                        check.sequenceFound(board,rightDiagonalArray,player,"Diagonal")
                if array[i+1][j-1] == player:
                    leftDiagonal += 1
                    if i+1 == len(array)-1:
                        leftDiagonalArray.append([i,j])
                        leftDiagonalArray.append([i+1,j-1])
                    else:
                        leftDiagonalArray.append([i,j])
                    print(leftDiagonal,leftDiagonalArray)
                    if leftDiagonal == 3:
                        leftDiagonalArray.append([i+1,j-1])    
                        leftDiagonalArray.append([i-3,j+3])
                        check.sequenceFound(board,leftDiagonalArray,player,"Diagonal")
    
def mousePressed():
    if(check.buttonContains(mouseX,mouseY) and superpower.reverseMode == True):
        x = cp5.getController("inputRow").getText()
        y = cp5.getController("inputColumn").getText()
        x,y = str(x),str(y)
        if (x.isdigit() and y == ""):
            x = int(x)
            reverseRowColumn(show_board,x,"")
            check.mode = "reverseSuccessful"
            superpower.reverseMode = False
        elif(y.isdigit() and x == ""):
            y = int(y)
            reverseRowColumn(show_board,"",y)
            check.mode = "reverseSuccessful"
            superpower.reverseMode = False
        else:
            check.mode = "errorReverseInput"
            superpower.reverseMode = True
    elif(check.buttonContains(mouseX,mouseY)):
        if superpower.superpowerMode == False:
            x = cp5.getController("inputRow").getText()
            y = cp5.getController("inputColumn").getText()
            x,y = str(x),str(y)
            if (x.isdigit() and y.isdigit()):
                x = int(x)
                y = int(y)
                if((x >= 0 and x <= 9) and (y >= 0 and y <= 9)):
                    if check.counter == 0 :
                        if board[x][y].circle == True or board[x][y].cross == True:
                            check.mode = "pieceFound"
                        else:
                            board[x][y].circle = True
                            check.getCircleCoor(x,y)
                            show_board[x][y] = "O"
                            checkSequence(board,show_board,"O")
                            #put message status here 
                            check.circlePosition = "Circle placed on board[%d][%d]" %(check.xCircle,check.yCircle)
                            check.update(1)
                            check.mode = "idle"
                    elif check.counter == 1 :
                        if board[x][y].circle == True or board[x][y].cross == True:
                            check.mode = "pieceFound"
                        else:
                            board[x][y].cross = True
                            check.getCrossCoor(x,y)
                            show_board[x][y] = "X"
                            checkSequence(board,show_board,"X")
                            check.crossPosition = "Cross placed on board[%d][%d]" %(check.xCross,check.yCross)  
                            check.update(0)
                            check.mode = "idle"
                else:
                    check.mode = "errorRange"
            else:
                check.mode = "errorInput"
        else:
            #SUPERPOWER MODE IS TRUE
            #use superpower to change position of piece
            x = cp5.getController("inputRow").getText()
            y = cp5.getController("inputColumn").getText()
            x,y = str(x),str(y)
            if (x.isdigit() and y.isdigit()):
                x,y = int(x),int(y)
                if board[x][y].sequence == True:
                    check.mode = "sequenceFound"
                else:
                    if check.counter == 0:
                        board[x][y].circle = True
                        show_board[x][y] = "O"
                        check.circleSPUsed = True
                        checkSequence(board,show_board,"O")
                    else:
                        board[x][y].circle = False
                        board[x][y].cross = True
                        show_board[x][y] = "X"
                        check.crossSPUsed = True
                        checkSequence(board,show_board,"O")
                    superpower.superpowerMode = False
                    check.update(1 if check.counter == 0 else 0)
                    superpower.restoreSquares(board)
                    check.mode = "idle"
    elif(superpower.containsPosition(mouseX,mouseY)):
        if check.checkSPUsed(check.counter):
            check.mode = "SPUsed"
        else:
            superpower.changePosition(check.counter,show_board,board)
    elif(superpower.containsReverse(mouseX,mouseY)):
        check.mode = "reverseMode"
        superpower.reverseMode = True
    

#---------------------------------MAIN CODE-------------------------------------
def setup():
    global cp5,imgCircle,imgCross,imgTitle,inputRow,inputColumn,font2,imgButton,imgMenu,superpower,imgReverse,imgCredits,imgPosition
    font2 = createFont("Type-Writer",20)
    cp5 = ControlP5(this)
    superpower = Superpower()
    cp5.addTextfield("inputRow").setPosition(800,690).setSize(100,40).setFont(font2).setColorBackground(0x00ffff).setAutoClear(True)
    cp5.addTextfield("inputColumn").setPosition(1030,690).setSize(100,40).setColorBackground(0x00ffff).setFont(font2)

    #===============================IMAGE==============================
    imgCircle = loadImage("circle2.png")
    imgCross = loadImage("cross2.png")
    imgTitle = loadImage("title2.png")
    imgButton = loadImage("button.png")
    imgMenu = loadImage("menu.png")
    imgReverse = loadImage("reverse.png")
    imgCredits = loadImage("credits.png")
    imgPosition = loadImage("position.png")
    #===============================FONTS==============================
    array = []
    size(1450,800)
    background(200)

    #create board
    for i in range(2,12):
        array = []
        for j in range(1,11):
            cell = Board(j,i)
            array.append(cell)
        board.append(array)
    return board
                    
def draw():
    fill(0)
    x,y = 0,0
    check.showMessage(check.counter,x,y,check.mode)
    for i in range(len(board)) :
        for j in range(len(board[i])) :
            board[i][j].show()
    check.showInterface(show_board)
