from p5 import *
import random

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
        fill(self.colour)
        rect((self.x,self.y),self.size,self.size)
        if self.circle == True :
            fill(255,0,0)
            ellipse((self.x + self.size/2,self.y + self.size/2),30,30)             
        elif self.cross == True :
            fill(0,0,255)
            ellipse((self.x + self.size/2,self.y + self.size/2),30,30)

        # if self.displayPosition == True :
        #     text("%d,%d" %(self.x/60,self.y/60),(self.x,self.y))


    def contains(self,x,y) :
        return ((x > self.x and x < self.x + self.size) and (y > self.y and y < self.y + self.size))

    def place(self,symbol) :
        if(symbol == "circle") :
            self.circle= True
        else :
            self.cross = True


    # def placeByCoordinate(self) :
    #     self.circle = True


class Check() :
    def __init__(self) :
        self.counter = 0
        self.x = 0
        self.y = 0

    def update(self,num) :
        self.counter = num

    def botMode(self,board,piece_array,piece_object,piece) :
        self.x = abs(random.randint(0,9))
        self.y = abs(random.randint(0,9))
        if piece == "cross" :
            board[self.y][self.x].cross = True
        piece_array.append([self.y,self.x])
        piece_object.append(board[self.y][self.x])



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