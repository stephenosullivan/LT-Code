__author__ = 'stephenosullivan'

class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        if not a or not b:
            return a or b

        index = -1
        carry = 0
        result = []
        while -index <= max(len(a), len(b)):
            x = int(a[index]) if -index <= len(a) else 0
            y = int(b[index]) if -index <= len(b) else 0
            carry, remainder = divmod(x + y + carry, 2)
            result.append(remainder)
            index -= 1

        if carry:
            result.append(carry)

        return ''.join(map(str, reversed(result)))
