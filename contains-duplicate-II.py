__author__ = 'stephenosullivan'

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        indexmap = dict()
        for i in range(len(nums)):
            if nums[i] in indexmap:
                if i - indexmap[nums[i]] <= k:
                    return True
                else:
                    indexmap[nums[i]] = i
            else:
                indexmap[nums[i]] = i
        return False
