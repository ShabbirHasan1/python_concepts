# Linked List and Node Classes
class Node:
    '''
    Node Class use to construct Linked List
    '''
    def __init__(self, data):
        self.data = data
        self.next_element = None
        self.previous_element = None


class DoublyLinkedList:
    '''
    Implementation of Doubly Linked List
    '''
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get_head(self):
        if self.head is not None:
            return self.head.data
        return False

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def insert_tail(self, data):
        temp_node = Node(data)
        if self.is_empty():
            self.head = temp_node
            self.tail = temp_node
        else:
            self.tail.next_element = temp_node
            temp_node.previous_element = self.tail
            self.tail = temp_node
        self.length += 1
        return temp_node

    def remove_head(self):
        if self.is_empty():
            return False
        node_remove = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = node_remove.next_element
            self.head.previous_element = None
            node_remove.next_element = None
        self.length -= 1
        return node_remove.data

    def tail_node(self):
        if self.head is not None:
            return self.tail.data
        return False

    def __str__(self):
        if self.is_empty():
            return ''
        temp = self.head
        val = "[" + str(temp.data) + ", "
        temp = temp.next_element

        while temp.next_element:
            val = val + str(temp.data) + ", "
            temp = temp.next_element
        val = val + str(temp.data) + "]"
        return val
