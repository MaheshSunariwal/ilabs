# Q-1 reverse a doubly linked list



# driver code
class node :
    def __init__(self,data) :
        self.data = data
        self.prev = None
        self.next = None

class Doubly_link :
    def __init__(self) :
        self.head = None
    def add_begin(self,data) :
        new_node = node(data)
        if self.head is None :
            self.head = new_node
            #print(self.head.data)
        else :
            new_node.prev = None
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        #print(new_node.data,end = '<-->')

    def reverse(self):
        pointer = self.head
        if pointer is None:
            return pointer.data
        if pointer.prev is None and pointer.next is None:
            return pointer.data
        curr=pointer
        while curr.next is not None:
            curr.prev,curr.next=curr.next,curr.prev
            curr=curr.prev
        curr.prev,curr.next=curr.next,curr.prev
        return curr

    def print_ll_reverse(self) :
        pointer = self.head
        if self.head is None :
            print('ll is empty')
        else :
            while pointer.next is not None :
                pointer = pointer.next

            while pointer is not None:
                print(pointer.data,end = '--')
                pointer = pointer.prev

l = Doubly_link()
l.add_begin(10)
l.add_begin(20)
l.add_begin(40)
l.print_ll_reverse()
l.reverse()
l.print_ll_reverse()


# Q2


