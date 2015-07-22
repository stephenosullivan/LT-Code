__author__ = 'stephenosullivan'

class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.front = []
        self.back = []


    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.front.append(x)


    # @return nothing
    def pop(self):
        if self.front:
            while self.front:
                self.back.append(self.front.pop())
            self.back.pop(0)
            while self.back:
                self.front.append(self.back.pop())


    # @return an integer
    def top(self):
        if self.front:
            while self.front:
                self.back.append(self.front.pop())

            tmp = self.back[0]
            while self.back:
                self.front.append(self.back.pop())
            return tmp


    # @return an boolean
    def empty(self):
        return not bool(self.front)

