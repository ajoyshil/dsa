class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def insert_at_last(self,x):
        new_node = Node(x)
        current = self.head
        if current is None:
            self.head = new_node
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after_node(self, x, target_node):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current:
            if current.data == target_node:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def search(self, data):
        current = self.head
        if not current:
            print("list is empty")
            return
        while current:
            if current.data == data:
                print("node is found")
                return
            current = current.next

    def sorting(self):
        current = self.head
        if not current:
            return
        while current:
            pass

    def delete_node(self,target_node):
        current = self.head
        if not current:
            return
        if self.head.data == target_node:
            self.head = self.head.next
            return
        while current:
            if current.next.data == target_node:
                current.next = current.next.next
                return
            current = current.next


node = Node(4)
node1 = Node(5)
node2 = Node(9)
ll = LinkedList()
ll.head = node
ll.head.next = node1
node1.next = node2
ll.insert_at_beginning(6)
ll.insert_at_last(11)
ll.insert_after_node(-2,5)
ll.traverse()
ll.delete_node(-2)
ll.traverse()
ll.reverse()
ll.traverse()
ll.rev()
ll.traverse()



# x = ll.head

# while x:
#     print(x.data)
#     x = x.next




