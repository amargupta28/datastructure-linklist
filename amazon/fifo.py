class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class stack:
    def __init__(self,val):
        node = Node(val)
        self.head=node
        # self.tail=node
    
    def insert(self,val):
        node= Node(val)
        if self.head is None:
            self.head = node
            # self.tail = node
            return True
        
        temp=self.head
        self.head = node
        node.next =temp
        # temp.next=None

    
    def print_node(self):
        temp=self.head
        if self.head is None:
            print("Empty List")
            return -1
        s=""
        while temp:
            s+=str(temp.val) +" --> " 
            temp=temp.next
        print (s)
    
    def pop_item(self):
        if self.head is None:
            print("Empty List")
            return -1
        
        temp=self.head
        self.head = self.head.next
        temp.next=None
    


lifo=stack(5)
lifo.print_node()
lifo.insert(4)
lifo.print_node()
lifo.insert(3)
lifo.print_node()
lifo.insert(2)
lifo.print_node()
lifo.insert(1)


lifo.print_node()
lifo.pop_item()

lifo.print_node()
lifo.pop_item()

lifo.print_node()

lifo.pop_item()

lifo.print_node()
lifo.pop_item()

lifo.print_node()
lifo.pop_item()
lifo.pop_item()

# lifo.print_node()
# lifo.pop_item()

# lifo.print_node()
# lifo.pop_item()

# lifo.print_node()