def merge(list1,list2):
    combined=[]
    i=0
    j=0

    while i<len(list1) and j< len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i+=1
        else:
            combined.append(list2[j])
            j+=1
    
    while i < len(list1):
        combined.append(list1[i])
        i+=1
    
    while j<len(list2):
        combined.append(list2[j])
        j+=1
    
    return combined




def mergeArray(mylist):
    if len(mylist) == 1:
        return mylist
    else:
        mid_pt = int(len(mylist)/2)
        left_array = mylist[:mid_pt]
        right_array = mylist[mid_pt:]

        return merge(mergeArray(left_array),mergeArray(right_array))


print(mergeArray([2,5,3,1,6,8,4]))
