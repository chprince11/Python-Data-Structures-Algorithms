class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right
        
    def __str__(self):
        return str(self.val)
    
    # Recursive Pre Order Traversal (DFS) Time: O(n), Space: O(n)
    def pre_order(self, node):
        if not node:
            return
        print(node)
        self.pre_order(node.left)
        self.pre_order(node.right)
    
      
    # Recursive In Order Traversal (DFS) Time: O(n), Space: O(n)
    def in_order(self, node):
        if not node:
            return
        self.in_order(node.left)
        print(node)
        self.in_order(node.right)
        
    # Recursive Post Order Traversal (DFS) Time: O(n), Space: O(n)
    def post_order(self, node):
        if not node:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node)

# Constructing the tree
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

print("Pre-order Traversal:")
A.pre_order(A)

print("In-order Traversal:")
A.in_order(A)

print("Post-order Traversal:")
A.post_order(A)
