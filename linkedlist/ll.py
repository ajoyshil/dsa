class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse_list(self): # 2 3 4 5
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

n = Node(2)
n2 = Node(3)
n3 = Node(4)
n4 = Node(5)

ll = LinkedList()
ll.head = n
n.next = n2
n2.next = n3
n3.next = n4
s = ll.head
while s:
    print(s.data)
    s = s.next

ll.reverse_list()
s = ll.head
while s:
    print(s.data)
    s =s.next


def tt(str):
    d = 0
    count = 0
    str = reversed(str)
    for c in str:
        if c == 'd':
            d +=1
        if c == 'g':
            count += d
    return count

s = "goodgdgggd"
print(tt(s))
