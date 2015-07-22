__author__ = 'stephenosullivan'

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        singles = set()
        for i in nums:
            if i in singles:
                return True
            else:
                singles.add(i)
        return False
