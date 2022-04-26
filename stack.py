class Node:
    def __init__(self,v,net=None):
        self.val = v
        self.next = net
    
class Stack:

    def __init__(self,v):
        newNode = Node(v)
        self.top = newNode
        self.height = 1

    def add(self,v):
        newNode = Node(v)

        if self.height < 0 :
            self.top = newNode
        else :
            newNode.next = self.top
            self.top = newNode
        self.height+=1
    
    def printStack(self):

        temp  =self.top

        while temp:
            print(temp.val)
            temp=temp.next

    def remove(self):
        if self.height == 0 :
            print("Stack is Empty")
            return False
        else:
            temp=self.top
            self.top = self.top.next
            temp.next=None
            self.height -=1
            return temp.val
        # temp=self.top
        # while temp:


    
stac = Stack(4)
stac.add(3)
stac.add(2)
stac.add(5)
stac.printStack()
print("----5------")
print(stac.remove())
print("-----------")
stac.printStack()
print("-----2-----")
print(stac.remove())
print("-----------")
stac.printStack()
print("------3----")
print(stac.remove())
print("-----------")
stac.printStack()
print("-----4-----")
print(stac.remove())
print("-----------")
stac.printStack()
print("-----None-----")
print(stac.remove())
print("-----------")
stac.printStack()