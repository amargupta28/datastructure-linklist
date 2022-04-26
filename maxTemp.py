def getMaxTemp(arr):
    su = sum(arr)
    i=0
    max_temp=0

    while i < len(arr):
        t1=arr[:i+1]
        t2=arr[i:len(arr)]

        if max(sum(t1),sum(t2)) > max_temp:
            max_temp =max(sum(t1),sum(t2))
        i+=1
    return max_temp

arr=[-1,2,3]
print(getMaxTemp(arr))
