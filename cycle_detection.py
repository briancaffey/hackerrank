"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def advance(a, b):
    if a.next == None:
        return False
    elif a.data == b.data:
        return True
    else:
        a = a.next
        b = a.next
        return advance(a, b)

def has_cycle(head):
    if head.next == None:
        return False
    a = head.next
    b = a.next
    return advance(a, b)
