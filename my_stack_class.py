# stack first in last out

class Stack:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        self.data.pop(-1)

    def top(self):
        return self.peek()

    def peek(self):
        if not self.isEmpty():
            return self.data[-1]

    def isEmpty(self):
        return len(self.data) == 0

"""
stack_1 = Stack()
print(stack_1.peek())
stack_1.push(100)
stack_1.push(999)
stack_1.push(10000)
print(stack_1.peek())
print("my stack file")
"""
