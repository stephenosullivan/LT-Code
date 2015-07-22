__author__ = 'stephenosullivan'

"""Given an array and a value, remove all instances of that value in place and return the new length."""

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        cnt = 0
        for i in range(len(nums)):
            if cnt > 0:
                nums[i-cnt] = nums[i]
            if nums[i] == val:
                cnt += 1
        return len(nums) - cnt


   #Slower method
    # def removeElement(self, nums, val):
    #     if nums is None:
    #         return 0
    #     else:
    #         i = 0
    #         length = len(nums)
    #         while True:
    #             if i < length:
    #                 if nums[i] == val:
    #                     del nums[i]
    #                     length -= 1
    #                 else:
    #                     i += 1
    #             else:
    #                 return length