class HashTable:
    def __init__(self):
        self.MAX=10
        self.arr = [[] for i in range(self.MAX)]
    
    def createHash(self,key):
        h=0
        for ch in key:
            h += ord(ch)
        
        return h % self.MAX
    
    def __setitem__(self,key,val):
        item = self.createHash(key)
        found =False
        # self.arr[item]=val
        for index,ele in enumerate(self.arr[item]):
            if len(ele) == 2 and ele[0] ==key :
                self.arr[item][idx] = (key,val)
                found =True
                break
        
        if not found:
            self.arr[item].append((key,val))

    
    def __getitem__(self,key):
        item=self.createHash(key)
        for idx,ele in enumerate(self.arr[item]):
            if ele[0] == key:
                return ele[1]
            

        return "Not Found"

    def __delitem__(self,key):
        item = self.createHash(key)

        for idx,ele in enumerate(self.arr[item]):
            if ele[0] == key:
                del self.arr[item][idx]
                break




if __name__ == '__main__':

    t=HashTable()
    t['amar'] = 56
    t['radhe'] =90
    t['march 6'] = 89
    t['march 17'] =54
    print(t.arr)

    print(t['march 6'])
    del t['march 6']
    print(t.arr)
