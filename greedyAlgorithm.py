denominations = [1, 2, 5, 10, 20, 50, 100]

def returnchange(change,denominations):
    toGiveback = [0]*len(denominations)
    for pos, coin in enumerate(reversed(denominations)):
        while coin <=change:
            change = change-coin
            toGiveback[pos] +=1
    return list(reversed(toGiveback))


print(returnchange(30,denominations))
