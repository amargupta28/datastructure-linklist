
keyboard = [
	['Q', 'X', 'P', 'L', 'E'],

	['W', 'A', 'C', 'I', 'N'],
]
s={}
k=2
for i in range(len(keyboard)):
    for j in range(len(keyboard[0])):

        if keyboard[i][j] not in s:
            s[keyboard[i][j]] =[]
        
        l=0        
        while l <= k:
            if i-l < len()





# word = "PENCIL" 
# word="LENCIL"

# def search_keyboard(keyboard, word, k):
#   """ Returns True if word can be constructed from chars in keyboard."""
#   tempx=-1
#   tempy=-1
  
#   for i in range(len(keyboard)):
#     for j in range(len(keyboard[0])):
#         if word[0] == keyboard[i][j]: # Position of first element --> P
#           tempx =i
#           tempy=j
#           break
          
#   if tempx == -1 and tempy ==-1:
#     return False
          
#   for ch in word[1:]:# Iterate over elements from 2nd positon to last element   PENCIL --> p [0][4] -->c[1][2] -- >L[0][3]
#     # ch = "C"
#     # tempX = 1
#     # tempY = 4
#     if tempx+1 < len(keyboard) and keyboard[tempx+1][tempy] == ch :
#       tempx+=1
#       continue
#     elif tempx+2 < len(keyboard) and keyboard[tempx+2][tempy] ==ch:
#       tempx+=2
#       continue
#     elif  tempx-1 < len(keyboard) and keyboard[tempx-1][tempy] ==ch:
#       tempx-=1
#       continue
#     elif tempx-2 < len(keyboard) and keyboard[tempx-2][tempy] == ch:
#       tempx-=2
#       continue
#     elif tempy+1 < len(keyboard[0]) and keyboard[tempx][tempy+1] == ch:
#       tempy+=1
#       continue
#     elif  tempy+2 < len(keyboard[0]) and keyboard[tempx][tempy+2] == ch:
#       tempy+=2
#       continue
#     elif tempy-1 < len(keyboard[0]) and keyboard[tempx][tempy-1] ==ch:
#       tempy-=1
#       continue
#     elif tempy-2 < len(keyboard[0]) and keyboard[tempx][tempy-2] ==ch:
#       tempy-=2
#       continue
#     else:
#       return False
    
#   return True


# print(search_keyboard(keyboard,word,2))
      