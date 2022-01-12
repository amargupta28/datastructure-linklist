class Node:

    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class linkedList:

    def __init__(self):
        self.head=None

    def insert_at_last(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr=self.head
        while itr.next:
            itr = itr.next
        
        itr.next=Node(data,None)

    def print(self):
        if self.head is None:
            print("No Linked LIST")
            return 
        
        itr =self.head
        llstr=''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr =itr.next
        
        print(llstr)


if __name__ == '__main__':
    l1=linkedList()
    l1.insert_at_last(5)
    l1.insert_at_last(10)
    l1.print()
    