"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def insert(r,val):
    if not r:
        return Node(data=val)

    if r.left and r.right:
        if val < r.data:
            insert(r.left, val)
        else:
            insert(r.right, val)

    elif r.left and not r.right:
        if val > r.data:
            r.right = Node(data=val)
        else:
            insert(r.left, val)

    elif not r.left and r.right:
        if val < r.data:
            r.left = Node(data=val)
        else:
            insert(r.right, val)

    else:
        if val < r.data:
            r.left = Node(data=val)
        else:
            r.right = Node(data=val)
    return r
