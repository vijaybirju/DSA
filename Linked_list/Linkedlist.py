# Linked list
# Every element of linked list has address of next element of it.



class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None 
    
    def insert_at_start(self,data):
        node=Node(data,self.head)
        self.head = node
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr=self.head
        while itr.next:
            itr=itr.next

        itr.next=Node(data,None)

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        llstr=''
        while self.head:
            llstr += str(self.head.data) + '-->'
            self.head=self.head.next
        print(llstr)



if __name__=='__main__':
    llst=LinkedList()
    print(llst.insert_at_start(4))
    llst.insert_at_start(43)
    llst.insert_at_end(34)
    llst.insert_at_start(11)
    llst.insert_at_end(22)
    llst.print()