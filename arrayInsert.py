# arr=[1,2,3,5,6]
# arr.append(7)
# print(arr)
# temp=0
# arr.append(-1)
# for i in range(len(arr)):
#     # print(i)
#     temp,arr[i]= arr[i],temp

# print(arr)

# def posInsert(arr,pos,itm):
#     arr.append(-1)
#     temp=itm
#     for i in range(pos,len(arr)):
#         temp,arr[i] =arr[i],temp
#     print(arr)

# posInsert(arr,4,4)

# def rototateArray(arr):
#     i=0
#     j=len(arr)-1
#     while i <j:
#         arr[j],arr[i] =arr[i],arr[j]
#         i+=1
#         j-=1
#     print(arr)

# def rotateArrayPos(arr,pos):
#     i=pos
#     j=len(arr)-1
#     while i <j:
#         arr[i],arr[j] = arr[j],arr[i]
#         i+=1
#         j-=1
#     print(arr)

# def deleteElem(arr,pos):
#     arr[pos]=-1
#     # temp=-1
#     i=pos
#     j=len(arr)-1
#     for i in range(pos,len(arr)-1):
#         arr[i]=arr[i+1]
#     arr.pop()
#     print(arr)


# def rottateArrayPivot(arr,pos):
#     i=0
#     j=pos-1
#     while i <j:
#         arr[i],arr[j] =arr[j],arr[i]
#         i+=1
#         j-=1
#     i=pos+1
#     j=len(arr)-1
#     while i <j:
#         arr[i],arr[j] =arr[j],arr[i]
#         i+=1
#         j-=1
#     print(arr)



    

# rototateArray(arr)
# rotateArrayPos(arr,4)
# deleteElem(arr,0)
# deleteElem(arr,3)
# rottateArrayPivot(arr,3)



nums = [1,2,3,4,5,6,7]
k = 3
 #o/p [5,6,7,1,2,3,4]

def rot(arr,k):


    for i in range(k):
        temp=arr[-1]
        i=0
        while i <len(arr):
            temp,arr[i] =arr[i],temp
            i+=1
    print(arr)

    # i=0
    # j=k
    # while i <j:
    #     arr[i],arr[j] =arr[j],arr[i]
    #     i+=1
    #     j-=1
    # print(arr)
    # i=k+1
    # j=len(arr)-1
    # while i <j:
    #     arr[i],arr[j]=arr[j],arr[i]
    #     i+=1
    #     j-=1
    # print(arr)
    # i=0
    # j=len(arr)-1
    # while i<j:
    #     arr[i],arr[j] =arr[j],arr[i]
    #     i+=1
    #     j-=1
    # print("Final ARR: ", arr)
rot([-1,-100,3,99],2)
