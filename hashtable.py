class HashTable:
    def __init__(self):
        self.MAX=100
        self.arr = [None for i in range(self.MAX)]
    
    def createHash(self,key):
        h=0
        for ch in key:
            h += ord(ch)
        
        return h % self.MAX
    
    def __setitem__(self,key,val):
        item = self.createHash(key)
        self.arr[item]=val
    
    def __getitem__(self,key):
        item=self.createHash(key)
        return self.arr[item]

    def __delitem__(self,key):
        item = self.createHash(key)
        self.arr[item] = None



t=HashTable()

t['amar'] = 56
t['radhe'] =90
t['march 1'] = 89
print(t.arr)
print(t['amar'])