"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root , s):
    current = root
    secret = ""
    for x in list(s):
        if int(x) == 0:
            current = current.left
            if current.data != '\0':
                secret += current.data
                current = root
            else:
                continue
        if int(x) == 1:
            current = current.right
            if current.data != '\0':
                secret += current.data
                current = root
            else:
                continue
    print secret
            
