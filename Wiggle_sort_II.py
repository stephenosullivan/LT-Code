class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2])

        nums[::2], nums[1::2] = reversed(nums[:half]), reversed(nums[half:])
