__author__ = 'stephenosullivan'

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        filterlist = [1]*n
        i = 2
        while i*i < n:
            j = 2
            while i*j < n:
                filterlist[i*j] = 0
                j += 1
            i += 1

            while filterlist[i] == 0 and i * i < n:
                i += 1
        return sum(filterlist[2:])


