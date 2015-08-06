__author__ = 'stephenosullivan'


class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        overflow = 2 ** 31 - 1
        minus = x < 0
        if minus:
            output = - int(''.join(i for i in list(str(x))[-1:0:-1]))
            if output < - overflow:
                return 0
            else:
                return output
        else:
            output = int(''.join(i for i in list(str(x))[-1::-1]))
            if output > overflow:
                return 0
            else:
                return output
