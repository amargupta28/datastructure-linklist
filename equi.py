def reverseInGroups( arr, N, K):
    # code here
    firs = arr[:K][::-1]
    print(firs)
    second=arr[K:][::-1]
    print(second)
    print(firs+second)
    return (firs+second)

print(reverseInGroups([1,2,3,4,5],5,3))