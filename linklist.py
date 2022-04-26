class Node:
    def __init__(self,value):
        self.value= value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node= Node(value)
        self.head=new_node
        self.tail = new_node
        self.length =1

    def printList(self):
        if self.head is None:
            print("Link List is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.value)
                temp =temp.next

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next = new_node
            self.tail=new_node
        self.length+=1
    
    def pop(self):

        if self.length == 1:
            self.head= None
            self.tail=None
            self.length =0
        elif self.length ==0 :
            print("No element to pop out")
        else:
            temp = self.head
            pre =self.head
            while temp is not None:
                pre =temp
                temp=temp.next
            self.tail =pre
            self.tail.next =None
            self.length-=1







link= LinkedList(1)
link.append(2)
link.append(3)
link.printList()
link.pop()
link.printList()
link.pop()
link.printList()
link.pop()
link.printList()