class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def getMin(self):
        return self.min_stack[-1]
    
    def __str__(self):
        return str(self.stack)
    
    def __repr__(self):
        return str(self.stack)

    def __len__(self):
        return len(self.stack)
