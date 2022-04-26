def getMinimumCost(parcels,k):
    win=1
    count=0
    arr=[]
    parcels.sort()
    print(parcels)
    if parcels[0] > 1 :
        for i in range(1,parcels[0]):
            arr.append(i)

    i=0
    while i < (len(parcels)-k):
        print(parcels[i+k] - parcels[i])

        if (parcels[i+k] - parcels[i]) > 1 and len(arr) != k:
            arr.append(parcels[i]+1)
        elif len(arr) ==k:
            break
        i+=k
    
    print(arr)


    # arr=[]
    # if len(parcels) == k:
    #     return 0
    # l={i:-1 for i in range(1,k+1)}
    # print(l)

    # for ele in l.keys():
        
    #     if ele not in parcels:
      
    #         arr.append(ele)
    # # print(arr[:(k-len(parcels))])
    # return sum(arr[:(k-len(parcels))])

print("ANS")
print(getMinimumCost([2,6,3,10,11],9))


    