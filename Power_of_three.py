class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            ndiv3 = n / 3
            if ndiv3 * 3 != n:
                return False
            return self.isPowerOfThree(ndiv3)
