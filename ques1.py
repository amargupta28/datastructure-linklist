def balancedSum(arr):
    print(arr)
    tempLeft = 0
    index=0
    size=len(arr)

    tempRight= sum(arr) -arr[0]
    while index< size:
        if tempLeft == tempRight:
            return item
        tempLeft +=  arr[index]
        index +=1
        if index < size:
            tempRight -= arr[index]
    return -1




print(balancedSum([4, 1, 3, 2, 4, 6]))