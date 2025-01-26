class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count+=1
            itr = itr.next
        return count

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def remove_at_beginning(self):
        if self.head is None:
            print('Nothing in list to remove')
            return

        self.head = self.head.next
        
    def insert_at_end(self,data):
        if self.head is None:
            node = Node(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
            node = Node(data,None)
        itr.next = node

    def insert_at(self,index,data):
        if index < 0 or index>=ll.get_length():
            raise ValueError('Index should not be negative')

        if index == 0:
            node = Node(data)
            node.next = self.head
            self.head = node
            return 
            
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
            if count == index-1:
                node = Node(data)
                node.next = itr.next
                itr.next = node
                return


    def printll(self):
        if self.head is None:
            print('Linked list is empty')
            return 

        ll_str = ''
        itr = self.head
        while itr:
            ll_str += str(itr.data)+"--->"
            itr = itr.next
        print(ll_str+"None")
        
ll = LinkedList()
ll.insert_at_beginning(3)
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)
ll.insert_at_end(4)
ll.insert_at_end(5)
ll.insert_at(0,0)
ll.remove_at_beginning()
ll.printll()
print("Linked list length is",ll.get_length())
