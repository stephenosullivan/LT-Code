class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        output = 0
        base = 5
        while (n - n % base) / base:
            output += (n - n % base) / base
            base *= 5

        return output
