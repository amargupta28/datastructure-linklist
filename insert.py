class Node:

    def __init__(self,data=None,next=None):
        self.data= data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_last(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
    
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,None)
        
    def print_linked_list(self):

        if self.head is None:
            print("No Linked List")
            return


        itr=self.head
        llstr=''
        while itr:
            llstr += str(itr.data) + " --> "
            itr =itr.next
        print (llstr)


    def insert_list(self,items):
        # self.head = None
        for item in items:
            self.insert_at_last(item)

    def count_linkList(self):

        count= 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        print(count)
        return count

    
    def remove_at(self,pos):

        if pos == 0:
            self.head = self.head.next
        
        if pos < 0 and pos >= count_linkList():
            print("Invalid Index")

        count= 0
        itr = self.head
        while itr:
            if count == pos -1:
                itr.next =itr.next.next
                break
            itr = itr.next
            count += 1


    def insert_at(self,data,pos):

        if pos <= 0 :
            print("element is getting inserted at 1st position")
            self.insert_at_begining(data)
        
        elif pos >= self.count_linkList():
            print("Element is getting inserted at last !!!!!")
            self.insert_at_last(data)

        else:
            count =0
            itr =self.head

            while itr:
                if count == pos -1:
                    temp = Node(data,itr.next)
                    itr.next = temp
                    break
                
                itr= itr.next
                count+=1

    def insert_after_value(self,data,afterValue):

        count= 0

        itr= self.head
        while itr:
            if itr.data == afterValue:
                count+=1
                node=Node(data,itr.next)
                itr.next =node
                break
            itr= itr.next
        
        if count == 0:
            print("Value not found")



if __name__ == "__main__":


    l1 = LinkedList()
    l1.insert_at_begining(222)
    l1.insert_at_begining(3333)
    l1.insert_at_last(11111)
    l1.insert_list([1,2,3,4,5,6])
    l1.print_linked_list()
    l1.count_linkList()
    l1.remove_at(2)
    l1.print_linked_list()
    l1.insert_at(23,5)
    l1.print_linked_list()
    l1.count_linkList()
    l1.insert_at(67,-1)
    l1.print_linked_list()
    l1.count_linkList()
    l1.insert_at(56,14)
    l1.print_linked_list()
    l1.count_linkList()
    l1.insert_after_value(78,1)
    l1.print_linked_list()
    l1.count_linkList()
