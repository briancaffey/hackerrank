
def topView(root):
  #Write your code here
    l_roots, r_roots = [], []
    l_root, r_root = root.left, root.right
    while l_root:
        l_roots.append(l_root.data)
        l_root = l_root.left

    while r_root:
        r_roots.append(r_root.data)
        r_root = r_root.right

    for top_node in l_roots[::-1] + [root.data] + r_roots: print top_node,
