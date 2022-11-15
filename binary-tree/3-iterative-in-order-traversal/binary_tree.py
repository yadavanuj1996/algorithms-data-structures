from binary_tree_node import *

class BinaryTree:
    def __init__(self, *args):
        if len(args) < 1:
            self.root = None
        elif isinstance(args[0], int):
            self.root = BinaryTreeNode(args[0])
        else:
            self.root = None
            for x in args[0]:
                self.insert(x)

    # for normal BT level by level insertion
    def insert_bt(self, key):
        temp_queue = []
        temp = self.root

        temp_queue.append(temp)

        while len(temp_queue):
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

    # for BST insertion
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

    def find_in_bst_rec(self, node, node_data):
        if not node:
            return None
        if node.data == node_data:
            return node
        elif node.data > node_data:
            return self.find_in_bst_rec(node.left, node_data)
        else:
            return self.find_in_bst_rec(node.right, node_data)

    def find_in_bst(self, node_data):
        return self.find_in_bst_rec(self.root, node_data)

    def populate_parents_rec(self, node, parent):
        if node:
            node.parent = parent
            self.populate_parents_rec(node.left, node)
            self.populate_parents_rec(node.right, node)

    def populate_parents(self):
        self.populate_parents_rec(self.root, None)

    def get_sub_tree_node_count(self, node):
        if not node:
            return 0
        else:
            return 1 + self.get_sub_tree_node_count(node.left) + self.get_sub_tree_node_count(node.right)

    def populate_count_rec(self, node):
        if node:
            node.count = self.get_sub_tree_node_count(node)
            self.populate_count_rec(node.left)
            self.populate_count_rec(node.right)

    def populate_count(self):
        self.populate_count_rec(self.root)

    def get_tree_deep_copy_rec(self, node):
        if node:
            new_node = BinaryTreeNode(node.data)
            # new_node = node.data
            new_node.left = self.get_tree_deep_copy_rec(node.left)
            new_node.right = self.get_tree_deep_copy_rec(node.right)
            return new_node
        else:
            return None

    def get_tree_deep_copy(self):
        if not self.root:
            return None
        else:
            tree_copy = BinaryTree()
            tree_copy.root = self.get_tree_deep_copy_rec(self.root)
            return tree_copy

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

    def find_in_BT(self, node_data):
        return self.findInBTRec(self.root, node_data)
