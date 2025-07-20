class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def pop(self):
        if self.head is None:
            return None
        item = self.head.data
        self.head = self.head.next
        self.size -= 1
        return item
    
    def peek(self):
        if self.head is None:
            return None
        return self.head.data
    
    def stack_size(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
        print()
        
    def reverse(self):
        current = self.head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
            
            
myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("LinkedList: ", end="")
myStack.traverse()
print("Peek: ", myStack.peek())
print("Pop: ", myStack.pop())
print("LinkedList after Pop: ", end="")
myStack.traverse()
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stack_size())