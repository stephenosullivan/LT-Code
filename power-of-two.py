__author__ = 'stephenosullivan'

"""Given an integer, write a function to determine if it is a power of two."""


class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return not n == 0 and not (n & (n-1))
