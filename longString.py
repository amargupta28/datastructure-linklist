def getPassword(arr):
    k=1
    ar=[]

    if len(arr) ==2:
            return str(arr[0]%10)+str(arr[1]%10) 

    for i in range(len(arr)-k):
        ar.append(((arr[i]%10) + (arr[i+k]%10)) %10)
        i = i+k+1
    return getPassword(ar)

# def getPass(numbers):
#     t =numbers.copy()
#     while True:
#         if len(t) ==2:
#             return str(t[0]%10)+str(t[1]%10)
#         t2,n=[],len(t)

#         for i in range(len)





arr1=[4,5,6,7]
arr2=arr1.copy()
print(arr2)
arr1.pop()
print("!!",arr1)
print("---" , arr2)
arr=[4,5]
# print(getPassword(arr))



