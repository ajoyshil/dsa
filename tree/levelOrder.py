from collections import deque

"""
    Tree declaration
    1 2 3 4 5 6 7 8 9
"""


class Tree:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def tree_print(self):
        if self.left:
            self.left.tree_print()
        print(self.val)
        if self.right:
            self.right.tree_print()

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Tree(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Tree(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

    def level_order(self, root):
        pass


# Invoke


root = Tree(5)
root.insert(3)
root.insert(2)
root.insert(4)
root.insert(7)
root.insert(6)
root.insert(8)
root.tree_print()
