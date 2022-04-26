def dictContains(word):
    dictionary = {"apple","pier","pie","pear"}
    return word in dictionary

def breakWord(word):
    breakwordhelp(word,len(word),"")

def breakwordhelp(word,n,result):
    
    for i in range(1,n+1):
        prefix=word[:i]
        print("--: ",prefix)

        if dictContains(word[:i]):
            print("i: ",i)
            if i==n:
                result+=prefix
                print ("res: ",result)
                return
            
            print(result+prefix+" ")
            
            breakwordhelp(word[i:],n-i,result+prefix+" ")
breakWord("applepie")