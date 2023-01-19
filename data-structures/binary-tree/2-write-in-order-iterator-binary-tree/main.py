from binary_tree import *
from binary_tree_node import *

class InorderIterator:
    def __init__(self, root):
        # TODO: Write - Your - Code
        self.result = []
        self.root = root
        self.in_order_traversal(root)
        self.result.reverse()

    def hasNext(self):
        return len(self.result) > 0
    # getNext returns null if there are no more elements in tree

    def getNext(self):
        return self.result.pop()
    
    def in_order_traversal(self, root):
        if not root:
            return 

        self.in_order_traversal(root.left)
        self.result.append(root)
        self.in_order_traversal(root.right)


# Iterator helper function (Don't modify it)
# This function returns the in-order list of nodes using the hasNext() and
# getNext() methods

def inorder_using_iterator(root):
    iter = InorderIterator(root)
    result = ""
    while iter.hasNext():
        ptr = iter.getNext()
        if iter.hasNext():
            result += str(ptr.data) + ", "
        else:
            result += str(ptr.data)
    if result == "":
        result = "None"
    print(result)
    return result

first_binary_tree = BinaryTree([100, 50, 200, 25, 75, 125, 300, 12, 35, 60])



in_order_iterator = InorderIterator(first_binary_tree.root)
inorder_using_iterator(first_binary_tree.root)


"""
Approach 1
class InorderIterator:
    def __init__(self, root):
        # TODO: Write - Your - Code
        self.result = []
        self.root = root
        self.in_order_traversal(root)
        self.result.reverse()

    def hasNext(self):
        return len(self.result) > 0
    # getNext returns null if there are no more elements in tree

    def getNext(self):
        return self.result.pop()
    
    def in_order_traversal(self, root):
        if not root:
            return 

        self.in_order_traversal(root.left)
        self.result.append(root)
        self.in_order_traversal(root.right)

"""