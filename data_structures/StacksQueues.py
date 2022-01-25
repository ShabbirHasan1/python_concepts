#implementing a Stack from scratch
from data_structures.LinkedList import DoublyLinkedList
class Stack:
    """
    Class to implement Stacks and associated functions using List
    """
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0

    def is_empty(self):
        return self.stack_size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return self.stack_size

    def push(self, value):
        self.stack_size += 1
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        self.stack_size -= 1
        return self.stack_list.pop()


class Queue:
    '''
    Implement queue using doubly linked list
    '''
    def __init__(self):
        self.items = DoublyLinkedList()

    def is_empty(self):
        return self.items.length == 0

    def front(self):
        if self.is_empty():
            return None
        return self.items.get_head()

    def rear(self):
        if self.is_empty():
            return None
        return self.items.tail_node()

    def size(self):
        return self.items.length

    def enqueue(self, value):
        return self.items.insert_tail(value)

    def dequeue(self):
        return self.items.remove_head()

    def print_list(self):
        return self.items.__str__()

if __name__ == "__main__":
    stack_obj = Stack()
    queue_obj = Queue()
