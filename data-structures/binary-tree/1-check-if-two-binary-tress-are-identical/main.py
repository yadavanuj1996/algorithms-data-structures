# Importing required functions
from binary_tree import BinaryTree 
from binary_tree import *
from binary_tree_node import *

def are_identical(root1, root2):
    result = check_binary_tree_identical(root1, root2)
    print(result)
    return result

def check_binary_tree_identical(node_a, node_b):
    if not node_a and not node_b:
        return True
    
    if (not node_a and node_b) or (node_a and not node_b) or node_a.data != node_b.data:
        return False
    
    is_left_subtree_identical = check_binary_tree_identical(node_a.left, node_b.left)
    is_right_subtree_identical = check_binary_tree_identical(node_a.right, node_b.right)

    if not is_left_subtree_identical or not is_right_subtree_identical:
        return False
    
    return True


first_binary_tree = BinaryTree(8)
first_binary_tree.insert(5)
first_binary_tree.insert(3)
first_binary_tree.insert(7)
first_binary_tree.insert(11)
first_binary_tree.insert(10)
first_binary_tree.insert(14)

second_binary_tree = BinaryTree(8)
second_binary_tree.insert(5)
second_binary_tree.insert(3)
second_binary_tree.insert(7)
second_binary_tree.insert(11)
second_binary_tree.insert(10)
second_binary_tree.insert(14)
second_binary_tree.insert(12)

are_identical(first_binary_tree.root, second_binary_tree.root)