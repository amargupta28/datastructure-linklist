'''
Problem 3:
Given a string s, return the sum of the vowels in the string if each vowel's weight increases by 1 according to the vowels order. 

Example:  
Input=  s: "Welcome to Indonesia", Vowels weight: a = 1, e = 2, i = 3, o = 4, u = 5  
Output = 22 (1 a's = 1*1 = 1 +  3 e's = 3*2 = 6 +  1 i's = 1*3 = 3 + 3 o's = 3*4 = 12)
'''

s="Welcome to Indonesia"

def checkVowel(w):
    v= {'a':1,'e':2,'i':3,'o':4,'u':5}
    return v[w] if w in v else 0
 
def wordCount(word, size):
    if (size == 1):
        return checkVowel(word[size - 1])
 
    return (wordCount(word, size - 1) + checkVowel(word[size - 1]))
 

 

print(wordCount(s, len(s)))

# def vowelWeight(s):
    
    



# print(vowelWeight(s,v))



# def vowelWeight(s):
#     vowels=['a','e','i','o','u']
#     arr={}
#     count=0
#     for i in s:
#         if i in vowels:
#             if i not in arr:
#                 arr[i] =0
#             arr[i]+=1
    
#     for idx,itm in enumerate(vowels):
#         if itm in arr:
#             count=count+((idx+1)*arr[itm])
    
#     return count

# print(vowelWeight(s))