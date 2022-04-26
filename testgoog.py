
keyboard = [
	['Q', 'X', 'P', 'L', 'E'],

	['W', 'A', 'C', 'I', 'N'],
]


def checkWord(keyboard,word,k,pos):
    print("h",pos,word)

    for i in range(len(keyboard)):
        for j in range(len(keyboard[0])):
            if keyboard[i][j] ==word:
                if pos[0] == -1 and pos[1] == -1:
                    return [i,j]
                distance = abs(pos[0] -i) + abs(pos[1]-j)
                print(distance)
                if 0<= distance <= k:
                    return [i,j]
                else:
                    return None
   
    return None

def searchBoard(keyboard,word,k):
    pos=[-1,-1]
    for i in word:
        res=checkWord(keyboard,i,k,pos)
        if res is None:
            return False
        else:
            pos[0]=res[0]
            pos[1] =res[1]
    return True

print(searchBoard(keyboard,"PIC",2))


# def isSafe(pos,visit):
#     if (0 <= pos[0] < len(visit)) and (0<= pos[1] < len(visit[0])):
#         return True

# def searchBoard(board,word,pos,visit,path=''):
#     visit[pos[0]][pos[1]] = True
#     path+=board[pos[0]][pos[1]]

#     if path == word:
#         return True





# def searchInBoard(board,word,k):
#     row=[i for i in range(-k,k+1)]
#     col= row[::-1]
    
#     visiting = [[False for i in range(len(board[0]))]for i in range (len(board))]
#     print(visiting)

#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             searchBoard(board,word,(i,j),visiting,'')