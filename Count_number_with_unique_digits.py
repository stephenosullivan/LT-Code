class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """

        def helper(num):
            if num == 0:
                return 1, 1
            perms, total = helper(num - 1)
            newperms = (10 - num + 1) * perms
            return newperms, total + (9 * newperms // 10)

        return helper(n)[1]
