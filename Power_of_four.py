class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num > 0:
            binaryDigits = map(int, list(reversed(bin(num)[2:])))
            return not bool(sum(binaryDigits[1::2])) and (sum(binaryDigits[::2]) == 1)
        return False
