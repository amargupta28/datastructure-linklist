board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

def print_board(boo):
    for i in range(len(boo)):
        if i%3 == 0 and i !=0:
            print("------------------")
        
        for j in range(len(boo[0])):

            if j%3 == 0 and j!=0:
                print("|",end =" ")
            if j == 8:
                print(boo[i][j])
            else:
                print(boo[i][j],end=" ")


def isEmpty(boo):
    for i in range(len(boo)):
        for j in range(len(boo[0])):
            if boo[i][j]== '.':
                return (i,j)
    return None

def isValid(boo,itm,pos):
    #check ROw
    for i in range(len(boo[0])):
        if boo[pos[0]][i] == itm and pos[1]!= i:
            return False
    
    #check Column
    for i in range(len(boo)):
        if boo[i][pos[1]] == itm and pos[0] !=i:
            return False
    #check in box
    # box_x= pos[1] //3
    # box_y=pos[0] //3

    # print(box_x,box_y)

    # for i in range(box_y*3,box_y*3 +3):
    #     for y in range(box_x*3,box_x*3 +3):
            
    #         print(boo[i][y] == itm , itm)
    #         if boo[i][y] == itm and (i,y) != pos:
    #             return False
    # return True
    row=pos[0]
    column=pos[1]

    for i in range(3):
        for j in range(3):
            if boo[(row - row % 3) + i][(column - column % 3) + j] == itm:
                return False

    return True


def solve(boo):
    find = isEmpty(boo)

    if  not find:
        return True
    
    for i in range(1,10):
        print(find,isValid(boo,i,find),i)
        if isValid(boo,i,find):
            boo[find[0]][find[1]] =i 
            if solve(boo):
                return True
            boo[find[0]][find[1]] = '.'
    return False






print_board(board)
print("**********************")
solve(board)
print("##################################")
print_board(board)