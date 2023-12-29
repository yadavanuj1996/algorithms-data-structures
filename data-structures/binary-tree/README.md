# Binary Tree

A binary tree is a tree in which each node has between 0-2 children. They’re called the left and right children of the node. 
The figure below shows what a Binary Tree looks like.

### Types of Binary Trees
#### Complete Binary Trees
- A complete binary tree is a binary tree in which all the levels of the tree are fully filled, except for perhaps the last level which can be filled from left to right.

![Screenshot 2022-11-09 at 7 53 36 PM](https://user-images.githubusercontent.com/22169012/200855308-b78ac671-8323-4e2c-819a-444af9aff56b.png)

#### Full Binary Trees
- In a full or ‘proper’ binary tree, every node has 0 or 2 children. No node can have 1 child.
- The total number of nodes in a full binary tree of height ‘h’ can be expressed as: 2h+1 <= total no of node <= 2^(h+1) - 1

![Screenshot 2022-11-09 at 8 00 25 PM](https://user-images.githubusercontent.com/22169012/200856981-42d37cfb-1a50-4fe2-a79d-988df3e30cca.png)


#### Perfect Binary Trees
A Binary tree is said to be Perfect if all its internal nodes have two children and all leaves are at the same level. 
- the total number of nodes in a perfect binary tree of height ‘h’ are given as: 2^(h+1) - 1
- total number of leaf nodes are given as 2^h or (n+1)/2

![Screenshot 2022-11-09 at 7 59 17 PM](https://user-images.githubusercontent.com/22169012/200856737-bcc182bd-da27-4dc2-8c21-e3f0ff26db34.png)


## Binary Tree Node Implementation
```
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        # below data members used only for some of the problems
        self.next = None
        self.parent = None
        self.count = 0
```

## Binary Tree Class Implementation
```
from binary_tree_node import *

class BinaryTree:

    # def __init__(self, *args) is a constructor that initializes 
    # the data members of BinaryTree
    def __init__(self, *args):
        if len(args) < 1:
            self.root = None
        elif isinstance(args[0], int):
            self.root = BinaryTreeNode(args[0])
        else:
            self.root = None
            for x in args[0]:
                self.insert(x)

    # insert_bt inserts a given key into the binary tree
    # insert_bt is used for normal binary tree level by level insertion
    def insert_bt(self, key):
        temp_queue = []
        temp = self.root

        temp_queue.append(temp)

        while temp_queue:
            temp = temp_queue[0]
            temp_queue.pop(0)

            if not temp.left:
                temp.left = BinaryTreeNode(key)
                break
            else:
                temp_queue.append(temp.left)

            if not temp.right:
                temp.right = BinaryTreeNode(key)
                break
            else:
                temp_queue.append(temp.right)

    # insert inserts an integer into the binary search tree
    def insert(self, node_data):
        new_node = BinaryTreeNode(node_data)
        if not self.root:
            self.root = new_node
        else:
            parent = None
            temp_pointer = self.root
            while temp_pointer:
                parent = temp_pointer
                if node_data <= temp_pointer.data:
                    temp_pointer = temp_pointer.left
                else:
                    temp_pointer = temp_pointer.right
            if node_data <= parent.data:
                parent.left = new_node
            else:
                parent.right = new_node

    # find_in_bst_rec is a helper function used by find_in_bst to 
    # find the given data in the binary search tree
    def find_in_bst_rec(self, node, node_data):
        if not node:
            return None
        if node.data == node_data:
            return node
        elif node.data > node_data:
            return self.find_in_bst_rec(node.left, node_data)
        else:
            return self.find_in_bst_rec(node.right, node_data)

    # find_in_bst is used to find the given data in the binary search tree
    def find_in_bst(self, node_data):
        return self.find_in_bst_rec(self.root, node_data)

    # populate_parents_rec is a helper function that is used by populate_parents
    def populate_parents_rec(self, node, parent):
        if node:
            node.parent = parent
            self.populate_parents_rec(node.left, node)
            self.populate_parents_rec(node.right, node)

    # populate_parents is used to populate the parent pointers 
    # of the nodes in the BinaryTree
    def populate_parents(self):
        self.populate_parents_rec(self.root, None)

    # get_sub_tree_node_count returns the count of the nodes in 
    # the sub-tree rooted at the given node
    def get_sub_tree_node_count(self, node):
        if not node:
            return 0
        else:
            return 1 + self.get_sub_tree_node_count(node.left) + self.get_sub_tree_node_count(node.right)

    # populate_count is a helper function used by populate_count 
    def populate_count_rec(self, node):
        if node:
            node.count = self.get_sub_tree_node_count(node)
            self.populate_count_rec(node.left)
            self.populate_count_rec(node.right)

    # populate_count is used to calculate the number of 
    # nodes present in the BinaryTree
    def populate_count(self):
        self.populate_count_rec(self.root)

    # get_tree_deep_copy_rec is a helper function used by get_tree_deep_copy
    def get_tree_deep_copy_rec(self, node):
        if node:
            new_node = BinaryTreeNode(node.data)
            new_node.left = self.get_tree_deep_copy_rec(node.left)
            new_node.right = self.get_tree_deep_copy_rec(node.right)
            return new_node
        else:
            return None

    # get_tree_deep_copy is used to make a deep copy of the BinaryTree
    def get_tree_deep_copy(self):
        if not self.root:
            return None
        else:
            tree_copy = BinaryTree()
            tree_copy.root = self.get_tree_deep_copy_rec(self.root)
            return tree_copy

    # find_in_BT_rec is a helper function used by find_in_BT to
    # find the given data in the binary tree 
    def find_in_BT_rec(self, node, node_data):
        if not node:
            return None

        if node.data == node_data:
            return node

        left_node = self.find_in_BT_rec(node.left, node_data)
        if left_node:
            return left_node

        right_node = self.find_in_BT_rec(node.right, node_data)
        return right_node
    
    # find_in_BT is used to find the given data in the binary tree
    def find_in_BT(self, node_data):
        return self.find_in_BT_rec(self.root, node_data)
```


#### Difference between Binary Tree and Binary Search Tree

##### Binary Tree
- A tree whose elements have at most 2 children is called a binary tree. Since each element in a binary tree can have only 2 children, we typically name them the left and right children. 

![Screenshot 2022-11-15 at 6 28 53 PM](https://user-images.githubusercontent.com/22169012/201925503-63b42764-bc7d-4453-99b5-c381fd901679.png)


##### Binary Search Tree
A binary Search Tree is a node-based binary tree data structure that has the following properties:  

- The left subtree of a node contains only nodes with keys lesser than the node’s key.
- The right subtree of a node contains only nodes with keys greater than the node’s key.
- The left and right subtree each must also be a binary search tree.
- There must be no duplicate nodes.

![Screenshot 2022-11-15 at 6 29 08 PM](https://user-images.githubusercontent.com/22169012/201925563-92af8e52-be36-4068-97c2-e855b7abda0d.png)



#### Links
https://takeuforward.org/binary-tree/introduction-to-trees/
