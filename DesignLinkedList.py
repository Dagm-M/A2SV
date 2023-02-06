class Node: 
    def __init__(self, value): 
        self.value = value 
        self.next = None 



class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        temp = self.head
        ind = 0
        while temp != None:
            if ind == index:
                return temp.value
            temp = temp.next
            ind += 1
        return -1
        

    def addAtHead(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)
            self.head.next = None
            self.tail = self.head
        else:
            temp = Node(val)
            temp.next = self.head
            self.head = temp

    def addAtTail(self, val: int) -> None:
        if self.tail == None:
            self.head = Node(val)
            self.head.next = None
            self.tail = self.head
        else:
            temp = Node(val)
            self.tail.next = temp
            self.tail = temp
            self.tail.next = None

    def addAtIndex(self, index: int, val: int) -> None:
        temp = self.head
        if index == 0:
            self.addAtHead(val)
        else:
            for i in range(index):
                tempBefore = temp
                if temp == None:
                    return
                temp = temp.next
            temp2 = Node(val)
            tempBefore.next = temp2
            temp2.next = temp
            if(temp == None):
                self.tail = temp2

    def deleteAtIndex(self, index: int) -> None:
        temp = self.head

        if index == 0:
            self.head = self.head.next
        else:
            for i in range(index):
                temp2 = temp
                temp = temp.next
                if temp == None:
                    return
            temp2.next = temp.next
            if temp == self.tail:
                self.tail = temp2
                

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
