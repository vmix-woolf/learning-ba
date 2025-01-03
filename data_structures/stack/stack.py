class Stack:
    def __init__(self):
        self.stack = []

    # Add element to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # delete element from the top of the stack and return it
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    # check if stack is empty and returns boolean
    def is_empty(self):
        return len(self.stack) == 0

    # return top element of the stack without its deletion
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
