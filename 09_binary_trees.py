from collections import deque

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
    
    # Recursive In Order Traversal (DFS) Time: O(n), Spa ce: O(n)
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
        
    # Iterative Pre Order Traversal (DFS) Time: O(n), Space: O(n)
    def pre_order_iterative(self, node):
        stack = [node]
        
        while stack:
            node = stack.pop()
            print(node)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
            
    # Level Order Traversal (BFS) Time: O(n), Space: O(n)
    def level_order(self, node):
        q = deque()
        q.append(node)
        
        while q:
            node = q.popleft()
            print(node)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
    
    # Check if Value Existes (DFS) Time: 0(n), Space O(n)
    def search(self, node, target):
        if not node:
            return False
        if node.val == target:
            return True
        
        return self.search(node.left, target) or self.search(node.right, target)
        
        
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

# Traversals
print("Pre-order Traversal:")
A.pre_order(A)

print("In-order Traversal:")
A.in_order(A)

print("Post-order Traversal:")
A.post_order(A)

print("Pre-order Traversal: Iterative")
A.pre_order_iterative(A)

print("Level-order Traversal: Queue")
A.level_order(A)

print(A.search(A, 6)) # False
print(A.search(A, 5)) #True
