"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def postOrder(root):
    #Write your code here

    if root.left:
        new_root = root.left
        postOrder(new_root)

    if root.right:
        new_root = root.right
        postOrder(new_root)

    print root.data,
