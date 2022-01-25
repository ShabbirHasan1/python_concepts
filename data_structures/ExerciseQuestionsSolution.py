#Question1
#Reversing First k Elements of Queue
#Implement the function reverseK(queue, k)
#which takes a queue and a number “k” as input and reverses the first “k” elements of the queue.
from data_structures.StacksQueues import Stack
def reverse_k(queue, k):
    '''
    function takes a queue and a number k as input and reverses the first k elements of the queue.
    :param queue: Type: Queue
    :param k: Int
    :return: Type:Queue
    '''
    # Handling invalid input
    if queue.is_empty() is True or k > queue.size() or k < 0:
        return None
    # Creating stack for reversing the elements
    stack = Stack()
    for _ in range(k):
        stack.push(queue.dequeue())
    while stack.is_empty() is False:
        queue.enqueue(stack.pop())
    size = queue.size()
    for _ in range(size - k):
        queue.enqueue(queue.dequeue())
    return queue
