from Queue import MyQueue
from Stack import MyStack


def reverseK(queue, k):
    # Write your code here
    if queue.is_empty():
        return None
    
    if queue.size() < k or k < 0:
        return 0

    stack=MyStack()
    result = MyQueue()
    for i in range(k):
        stack.push(queue.dequeue())
    
    while not stack.is_empty():
        result.enqueue(stack.pop())

    while not queue.is_empty():
        result.enqueue(queue.dequeue())
    print(result.display())
    return result

test_queue = MyQueue()
test_queue.enqueue(1)
test_queue.enqueue(2)
test_queue.enqueue(3)
test_queue.enqueue(4)
test_queue.enqueue(5)
test_queue.enqueue(6)
test_queue.enqueue(7)
test_queue.enqueue(8)
reverseK(test_queue, 5)