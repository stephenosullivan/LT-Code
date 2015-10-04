__author__ = 'stephenosullivan'

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = 0
        sum2 = 0
        for i, num in enumerate(nums):
            sum1, sum2 = max(sum2 + num, sum1), sum1
        return max(sum1, sum2)

    def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        memo = [None] * len(nums)
        return self.recursivecheck(0, memo)


    def recursivecheck(self, index, memo):
        if index < len(self.nums):
            if memo[index] is None:
                memo[index] = max(self.nums[index] + self.recursivecheck(index + 2, memo),
                                  self.recursivecheck(index + 1, memo))
            return memo[index]
        else:
            return 0
