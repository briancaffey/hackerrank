'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    height = 0
    while True:
        if root.right == None and root.left == None:
            return height
        else:
            height += 1
            if root.right:
                root = root.right
            else:
                root = root.left
