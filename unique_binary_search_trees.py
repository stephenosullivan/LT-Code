__author__ = 'stephenosullivan'


class Solution(object):
    def __init__(self):
        self.memo = dict()

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        for num in range(0, n + 1):
            self.memo[num] = None
        self.memo[0] = 1

        return self.partition(n)

    def partition(self, nums):
        if nums == 1:
            return 1
        else:
            if self.memo[nums] is None:
                self.memo[nums] = sum([self.partition(n) * self.partition(nums - n - 1) for n in range(nums)])

            return self.memo[nums]
