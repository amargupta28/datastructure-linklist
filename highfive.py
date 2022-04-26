def highfive(items):
    idDict={}
    finalAns=[]

    for [id,marks] in items:
        if id not in idDict:
            idDict[id]=[]
        idDict[id].append(marks)

    for id in idDict.keys():
        idDict[id].sort(reverse=True)
        # print(idDict[id])
        # print(idDict[id][:5])
        tempAverage = int(sum(idDict[id][:5])/5)
        finalAns.append([id,tempAverage])
    
    return finalAns

print(highfive([[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]))
