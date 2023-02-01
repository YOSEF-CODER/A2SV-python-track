class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None
        

class MyLinkedList:

    def __init__(self):
        self.head = None
        
    def printAll(self)-> None:
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next
        print('done')
        
    def get(self, index: int) -> int:
        cur = self.head
        for i in range(index):    
            cur = cur.next
            if cur == None:
                return -1
        if cur == None:
            return -1
        return cur.val 
        

    def addAtHead(self, val: int) -> None:
        #if no recorded element just add the new val as a head else move the head to the next element and make the new node the head
        if not self.head:
            self.head = Node(val)
        else:
            newNode = Node(val)
            cur = self.head
            self.head = newNode
            self.head.next = cur
            newNode = None
        

    def addAtTail(self, val: int) -> None:
        #fist reach the end of the node and then the last node next will be the new node
        if self.head == None:
            self.head = Node(val)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(val)
            
            
    def addAtIndex(self, index: int, val: int) -> None:
        #if index 0 just add as a first element
        if index == 0:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
            return
        #if no head then
        if self.head == None:
            return
        cur = self.head
        for i in range(index-1):
            if  cur == None:
                return
            cur = cur.next
        if cur == None:
            return
        before = cur.next
        cur.next = Node(val)
        cur.next.next = before
                
                

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head:
                self.head = self.head.next
                return
        cur = self.head
        for i in range(index-1):
            if cur == None:
                return
            cur = cur.next
        if cur == None:
            return
        toDelete = cur.next
        if toDelete:
            cur.next = cur.next.next
        toDelete = None

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)