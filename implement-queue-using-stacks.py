__author__ = 'stephenosullivan'


class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.Stack = []
        self.reverseStack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.Stack.append(x)

    # @return nothing
    def pop(self):
        while bool(self.Stack):
            self.reverseStack.append(self.Stack.pop())
        output = self.reverseStack.pop()
        while bool(self.reverseStack):
            self.Stack.append(self.reverseStack.pop())


    # @return an integer
    def peek(self):
        while bool(self.Stack):
            self.reverseStack.append(self.Stack.pop())
        output = self.reverseStack[-1]
        while bool(self.reverseStack):
            self.Stack.append(self.reverseStack.pop())
        return output

    # @return an boolean
    def empty(self):
        return not bool(self.Stack)
