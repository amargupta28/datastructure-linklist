def reverseList(arr,low,high):
    while low<high:
        A[low],A[high] = A[high], A[low]
        low+=1
        high-=1

def reverse(arr):
    arr[::-1]



A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)
reverse(A)
print(A)