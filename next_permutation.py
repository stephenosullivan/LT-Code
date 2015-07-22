__author__ = 'stephenosullivan'

"""Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers."""

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        left = None
        right = len(nums) - 1
        n = right
        cnt = 0
        while n > 0:
            if nums[n] > nums[n-1]:
                left = n - 1
                break
            n -= 1
        if left is None:
            nums.reverse()
            return
        n = right
        while n > 0:
            if nums[n] > nums[left]:
                nums[n], nums[left] = nums[left], nums[n]
                break
            n -= 1

        nums[left+1:] = reversed(nums[left+1:])

