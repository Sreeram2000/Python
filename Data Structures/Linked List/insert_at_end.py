class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node(None,None)
    def insert(self,value):
        if self.head.data == None:
            node = Node(value,None)
            self.head = node
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(value,None)
    def print(self):
        if self.head.data == None:
            return
        itr =  self.head
        while itr:
            print(itr.data + "-->",end = "")
            itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert('apple')
    ll.insert('pineapple')
    ll.insert('jackfruit')
    ll.insert('orange')
    ll.print()