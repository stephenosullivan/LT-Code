__author__ = 'stephenosullivan'


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        output1 = self.robwith(nums[:-1])
        output2 = self.robwith(nums[1:])

        return max(output1, output2)

    def robwith(self, nums):
        memo = [None] * len(nums)
        return self.roblinear(0, memo, nums)

    def roblinear(self, index, memo, nums):
        if index < len(nums):
            if memo[index] is None:
                memo[index] = max(nums[index] + self.roblinear(index + 2, memo, nums),
                                  self.roblinear(index + 1, memo, nums))
            return memo[index]
        else:
            return 0
