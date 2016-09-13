import random


class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        :type size: int
        """
        self.original = nums[:]
        self.currentConfig = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.currentConfig = self.original[:]
        return self.currentConfig

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        random.shuffle(self.currentConfig)
        return self.currentConfig


        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.reset()
        # param_2 = obj.shuffle()
