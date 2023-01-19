# Import required functions
from collections import deque
from binary_tree import *
from binary_tree_node import *

def level_order_traversal(root):
    result = ""
    # TODO: Write - Your - Code
    current_queue = deque()
    if not root:
        print(None)
        return None

    current_queue.append(root)
    result = get_level_order_traversal(current_queue, deque(), result)
    print(result)
    
    
def get_level_order_traversal(current_queue, next_queue, result):
    if not current_queue:
        return result

    result = result + " : " if len(result) > 0 else result
    while len(current_queue) > 0:
        node = current_queue.popleft()
        result += str(node.data) + ", " if len(current_queue) > 0 else str(node.data)
        if node.left:
            next_queue.append(node.left)
        if node.right:
            next_queue.append(node.right)
    return get_level_order_traversal(current_queue=next_queue, next_queue=deque(), result=result)
        

first_binary_tree = BinaryTree([100, 50, 200, 25, 75, 350])
level_order_traversal(first_binary_tree.root)

"""
Iteration 1 of solution using 2 queues

def level_order_traversal(root):
    result = ""
    # TODO: Write - Your - Code
    current_queue = deque()
    if not root:
        print(None)
        return None

    current_queue.append(root)
    result = get_level_order_traversal(current_queue, deque(), result)
    print(result[1:len(result)-1].replace(",", ", ").replace(":", " : "))
    
    
def get_level_order_traversal(current_queue, next_queue, result):
    if not current_queue:
        return result
    result = result[:len(result)-1] + ":"
    while len(current_queue) > 0:
        node = current_queue.popleft()
        result += str(node.data) + ","
        if node.left:
            next_queue.append(node.left)
        if node.right:
            next_queue.append(node.right)
    return get_level_order_traversal(current_queue=next_queue, next_queue=deque(), result=result)
        
"""