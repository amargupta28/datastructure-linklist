from random import randint

input_deck = ['A',1,2,3,4,5,6,7,8,9,10,'J','K','Q']

def shuffle(input_deck):
    temparr=[]
    outputDeck=[]
    i=0
    while i <len(input_deck):
        temp = randint(1, len(input_deck))
        if temp not in temparr:
            temparr.append(temp)
            i+=1
    for itm in temparr:
        outputDeck.append(input_deck[itm-1])
    return outputDeck

print(shuffle(input_deck))
