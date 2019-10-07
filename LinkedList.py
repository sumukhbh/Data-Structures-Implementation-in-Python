# Implementation of a singly linked list #

class Node(object):
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    # Returns the length of a linked list #
    def list_length(self):
        length = 0
        curr_node = self.head
        while curr_node is not None:
            length += 1
            curr_node = curr_node.next
        return length
    # checks whether a list is empty or not #
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    # Inserting a node at the end of the linked list #
    def insert_tail(self,Newnode):
        if self.head == None:
            self.head = Newnode
        else:
            last_node = self.head
            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next
            last_node.next = Newnode
    # Printing the contents of a linked list #
    def print_list(self):
        if self.head is None:
            print("Linked list is empty")
        current_node = self.head
        while True:
            if current_node is None:
                break
            print(current_node.data)
            current_node = current_node.next
    # Inserting a node at the head of the linked list #
    def insert_head(self,Newnode):
        temp_node = self.head
        self.head = Newnode
        Newnode.next = temp_node
        del temp_node
    # Inserting a node at a given index #
    def insert_index(self, Newnode, pos):
        if pos == 0:
            self.insert_head(Newnode)
            return
        if pos < 0 or pos > self.list_length():
            print("Invalid position")
            return
        curr_node = self.head
        curr_pos = 0
        while True:
            if curr_pos == pos:
                prev.next = Newnode
                Newnode.next = curr_node
                break
            prev = curr_node
            curr_node = curr_node.next
            curr_pos += 1
    # deleting head node #
    def delete_head(self):
        if self.isEmpty() == None:
            print("Linked list is already empty")
        else:
            prev = self.head
            self.head = self.head.next
            prev.next = None
    # deleting a node from the end of a linked list #
    def delete_tail(self):
        curr_node = self.head
        while curr_node.next is not None:
            prev = curr_node
            curr_node = curr_node.next
        prev.next = None
    # deleting a node at a given index #
    def delete_index(self,pos):
        if pos < 0 or pos >= self.list_length():
            print("Invalid position")
        if self.isEmpty() == False:
            if pos == 0:
                self.delete_head()
                return    
            curr_node = self.head
            curr_pos = 0
            while True:
                if curr_pos == pos:
                   prev.next = curr_node.next
                   curr_node.next = None
                   break
                prev = curr_node
                curr_node = curr_node.next
                curr_pos += 1
                        

first_node = Node(1)
linkedlist = LinkedList()
linkedlist.insert_tail(first_node)
second_node = Node(2)
linkedlist.insert_tail(second_node)
third_node = Node(3)
linkedlist.insert_tail(third_node)
linkedlist.print_list()
linkedlist.delete_index(1)
linkedlist.print_list()
