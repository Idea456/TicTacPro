circle_array = [[120, 240], [180, 240], [240, 240], [300, 240], [360, 240]]
cross_array =  [[60, 240], [60, 300], [60, 360], [60, 420], [60, 480]]


def checkWinningMove(circle_array,cross_array) :
    #check both piece array
    row_check = False
    #counter must be  5 for it to be True
    counter = 0
    column_check = False
    row = circle_array[0][0]
    column = circle_array[0][1]
    for i in range(1,len(circle_array)) :
        #check if the pieces are in the same rows or columns
        if circle_array[i][0] == row :
            row_check = True
        elif circle_array[i][1] == column :
            column_check = True

    for j in range(len(cross_array)) :
        pass

    if row_check == True :
        for rows in range(len(circle_array)) :
            if (circle_array[i+1][1] - circle_array[i][1] == 60) :
                counter += 1
            else :
                counter 

    print("circle pieces are in rows ? : ",row_check)
    print("circle pieces are in column ? : ",column_check)

#circle array are the red circles
#cross array are the blue circles
checkWinningMove(circle_array,cross_array)