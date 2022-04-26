class Hash:
    def __init__(self,size=7):
        self.map=[None] *size

    def __hash(self,key):
        my_hash =0
        for letter in key:
            my_hash=(my_hash+ord(letter)*23)%len(self.map)
        
        return my_hash

    def printHash(self):
        for i,item in enumerate(self.map):
            print(i," : ",item)

    def set_item(self,key,value):
        hashVal = self.__hash(key)
        if self.map[hashVal] is None:
            self.map[hashVal] = []
        self.map[hashVal].append([key,value])

    def get_item(self,key):
        hashVal = self.__hash(key)

        if self.map[hashVal] is not None:
            for item in range(len(self.map[hashVal])):
                if key == self.map[hashVal][item][0]:
                    return self.map[hashVal][item][1]
            return None
        return None

    def keys(self):
        all_key=[]

        for i in range(len(self.map)):
            if self.map[i] is not None:
                for j in range(len(self.map[i])):
                    all_key.append(self.map[i][j][0])
        return all_key


    
hash = Hash()

hash.set_item('bolts',50000)
hash.set_item('washers',50)
hash.set_item('lumber',80)
hash.printHash()
print(hash.get_item('bolts'))
print(hash.keys())
