__author__ = 'stephenosullivan'

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary_n = bin(n)[2:].zfill(32)
        bin_digits = map(int,list(binary_n))
        output = 0
        cnt = 0
        for digit in bin_digits:
            if digit:
                output += 2**cnt
            cnt += 1
        return output
