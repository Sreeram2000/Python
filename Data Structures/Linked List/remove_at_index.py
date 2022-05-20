class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head = Node()
    def insert(self,value):
        itr = self.head
        if self.head.data == None:
            node = Node(value,None)
            self.head = node
        else:
            while itr.next:
                itr = itr.next
            itr.next = Node(value,None)
    def print(self):
        itr=self.head
        while itr:
            print(itr.data + '-->',end="")
            itr = itr.next
    def remove_at_index(self,index):
        itr = self.head
        if index == 0:
            self.head = self.head.next
        else:
            while index>1:
                itr = itr.next
                index -= 1
            itr.next = itr.next.next
if __name__== '__main__':
    ll = LinkedList()
    ll.insert('apple')
    ll.insert('orange')
    ll.insert('apple1')
    ll.insert('orange1')
    ll.insert('apple2')
    ll.insert('orange2')
    ll.insert('apple3')
    ll.insert('orange3')
    ll.print()
    ll.remove_at_index(int(input('\nchoose index: ')))
    ll.print()

