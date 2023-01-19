# Importing required functions
from collections import deque
from binary_tree import *
from binary_tree_node import *
from Stack import MyStack

# Approach 2 using deque
def inorder_iterative(root):
  result = None
  stack = deque()
  if root:
    stack.append(root)
    
  while len(stack) > 0:
    if stack[-1].left:
      left_child = stack[-1].left
      stack[-1].left = None
      stack.append(left_child)
      
    else:
      node = stack.pop()
      result = result + ", " + str(node.data) if result else str(node.data)
      if node.right:
        stack.append(node.right)

  print(result)
  

first_binary_tree = BinaryTree([100, 50, 200, 25, 75, 35])
inorder_iterative(first_binary_tree.root)

"""
Approach 1 (Using MyStack class)
def inorder_iterative(root):
  result = None
  stack = MyStack()
  if root:
    stack.push(root)
    
  while not stack.is_empty():
    if stack.peek().left:
      left_child = stack.peek().left
      stack.peek().left = None
      stack.push(left_child)
      
    else:
      node = stack.pop()
      result = result + ", " + str(node.data) if result else str(node.data)
      if node.right:
        stack.push(node.right)

  print(result)

"""