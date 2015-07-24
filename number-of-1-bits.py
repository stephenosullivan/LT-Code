__author__ = 'stephenosullivan'

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        return sum(list(map(int, bin(n)[2:])))
