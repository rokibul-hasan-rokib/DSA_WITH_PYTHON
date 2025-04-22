class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_before(self, next_node, data):
        if next_node is None:
            return
        new_node = Node(data)
        new_node.next = next_node
        prev_node = self.head
        while prev_node.next is not next_node:
            prev_node = prev_node.next
        prev_node.next = new_node
   

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def delete_node(self, key):
        current = self.head
        if current is not None:
            if current.data == key:
                self.head = current.next
                current = None
                return
        while current is not None:
            if current.data == key:
                break
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None


llist = DoublyLinkedList()
llist.insert_at_beginning(1)
llist.insert_at_beginning(2)
llist.insert_at_beginning(3)
llist.insert_at_end(4)
llist.insert_after(llist.head.next, 5)
llist.insert_before(llist.head.next.next, 6)
llist.delete_node(3)
llist.print_list()

# Output: