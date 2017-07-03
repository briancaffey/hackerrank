"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def preOrder(root):
    #Write your code here
    print root.data,
    if root.left:
        preOrder(root.left)
    if root.right:
        preOrder(root.right)
