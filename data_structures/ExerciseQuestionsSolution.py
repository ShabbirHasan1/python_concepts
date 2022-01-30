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


#Question2
#Evaluate Postfix Expression Using a Stack
def evaluate_post_fix(exp):
    '''
    evaluate postfix expression
    :param exp: str exp = "694 * - 7 - 4 +"
    :return: integer
    '''
    stack = Stack()
    try:
        for char in exp:
            if char.isdigit():
                # Push numbers in stack
                stack.push(char)
            else:
                right = stack.pop()
                left = stack.pop()
                stack.push(str(eval(left + char + right)))
        return int(float(stack.pop()))
    except TypeError:
        return "Invalid Sequence"

if __name__ == "__main__" :
    print("Result of expression (694 * - 7 - 4 +) : " + str(evaluate_post_fix("694*+7-4+")))