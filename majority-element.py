__author__ = 'stephenosullivan'

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        counter = dict()
        length = len(nums)
        if length == 1:
            return nums[0]
        for i in nums:
            if i in counter:
                counter[i] += 1
                if counter[i] > length/2:
                    return i
            else:
                counter[i] = 1

