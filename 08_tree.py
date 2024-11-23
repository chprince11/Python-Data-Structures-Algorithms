"""

- Tree (General tree)
- Tree is a recursive data structure.
- Each entities in the tree are called nodes, and the top node is called root node. 
- The node which doesn't have any children or subcategories they are called leaf nodes.

"""
class TreeNode:
    def __init__(self, data):
        self.data = data # data as an element
        self.children = [] # List, this list is an instance of the TreeNode class
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self): # counting the ancestors
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()
            

def build_product_tree():
    
    root = TreeNode("Electronics")
    
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))
  
    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("Apple"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))
    
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    
    return root
    
if __name__ == '__main__':
    root = build_product_tree()
    print("Root at level:",root.get_level())
    root.print_tree()
    pass
