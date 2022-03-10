class Counter:
    def __init__(self,low,high):
        self.low =low
        self.high =high
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.low >self.high:
            raise StopIteration
        else:
            self.low+=1
        return self.low -1

for c in Counter(3,8):
    print(c)
