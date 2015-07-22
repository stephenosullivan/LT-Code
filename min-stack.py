__author__ = 'stephenosullivan'

"""Design a stack that supports push, pop, top, and retrieving the minimum element in constant time."""

class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stacklist = []
        self.minStack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stacklist.append(x)
        if not self.minStack or x<=self.minStack[-1]:
            self.minStack.append(x)


    # @return nothing
    def pop(self):
        x = self.stacklist.pop()
        if x<= self.minStack[-1]:
            self.minStack.pop()

    # @return an integer
    def top(self):
        return self.stacklist[-1]


    # @return an integer
    def getMin(self):
        return self.minStack[-1]

