class BinaryTreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    
    # below data members used only for some of the problems
    self.next = None
    self.parent = None
    self.count = None