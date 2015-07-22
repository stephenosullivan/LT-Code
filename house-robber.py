__author__ = 'stephenosullivan'

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums)>1:
            self.memo = [None]*len(nums)
            self.memo[0] = nums[0]
            self.memo[1] = max(nums[0],nums[1])
            return self.robRecursive(len(nums)-1,nums)
        elif len(nums)==1:
            return nums[0]
        else:
            return 0

    def robRecursive(self,n,nums):
        if self.memo[n] is None:
            self.memo[n] = max(self.robRecursive(n-1,nums),self.robRecursive(n-2,nums) + nums[n])
        return self.memo[n]