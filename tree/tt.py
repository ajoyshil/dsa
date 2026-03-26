class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if not self.val:
            self.val = val
        else:
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

    def delete(self, val):
        if val == self.val:
            self.right.left = self.left
            self.val = self.right

    def traverse(self):
        s = []
        s.append(t)
        while s:
            nn = s.pop(0)
            print(nn.val)
            if nn.left:
                s.append(nn.left)
            if nn.right:
                s.append(nn.right)



t = Tree(5)
t.insert(4)
t.insert(6)
t.insert(3)
t.insert(2)
t.insert(1)
t.insert(7)


# t.traverse()
t.delete(5)
t.traverse()