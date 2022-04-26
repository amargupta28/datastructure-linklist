def findEarliestMonth(stock):
    # print(int((sum(stock[1:len(stock)])/(len(stock)-1))))
    minMonth=abs(stock[0] - int((sum(stock[1:len(stock)])/(len(stock)-1))))
    # print(minMonth)
    i=1
    while i < len(stock)-1:
        # print(stock[:i+1] , " @@@ ", len(stock[:i+1]))
        temp1 = int(sum(stock[:i+1])/len(stock[:i+1]))

        temp2 = int((sum(stock[i+1:len(stock)])/(len(stock[i+1:len(stock)]))))
        # print(temp1, " ",temp2)
        # print(int(abs(sum(stock[:i+1])/len(stock[:i+1]) - int((sum(stock[i+1:len(stock)])/(len(stock)-1))))))
        # print("Min", minMonth, " ", i)
        if abs(temp1-temp2) < minMonth:
            minMonth = i+1
        i+=1
    return minMonth





arr=[1,3,2,4,5]
print("final: ", findEarliestMonth(arr))