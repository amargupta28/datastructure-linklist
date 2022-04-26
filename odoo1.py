def amountinCents(amount,taxpercent):
    arr=[]
    taxAmount= (amount*taxpercent)/100
    # print(taxAmount)
    arr.append(int(100*taxAmount))
    return arr
print(amountinCents(100,10))