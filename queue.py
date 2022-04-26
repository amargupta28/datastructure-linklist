class Node:
    def __init__(self.v):
        self.val=v
        self.next = None

class Queue:
    def __init__(self,v):
        newNode = Node(v)
        self.first = newNode
        self.last=newNode
        self.height = 1

    def printQueue(self):
        temp = self.first
        while temp:
            print(temp.val)
            temp = temp.next

    def addQueue(self,v):
        newNode = Node(v)
        if self.height == 0:
            self.first =newNode
            self.last=newNode
        else:
            self.last.next = newNode
            self.last =newNode
        self.height+=1

    def removeQueue(self):
        if self.height == 0:
            print("Empty Queue")
            return False
        elif self.height == 1:
            temp =self.first
            self.first =None
            self.last = None
            return temp.val
        else:
            temp = self.first
            self.first = self.first.next
            temp.next =None
            self.height -=1
            return temp
