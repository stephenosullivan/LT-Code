class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = len(nums) - 1

        while p2 >= 0 and nums[p2] == 2:
            p2 -= 1
        while p1 <= p2 and nums[p1] == 0:
            p1 += 1

        i = p1

        while i <= p2:
            if nums[i] == 0:
                nums[p1], nums[i] = nums[i], nums[p1]
            elif nums[i] == 2:
                nums[p2], nums[i] = nums[i], nums[p2]
            else:
                i += 1

            while p2 >= p1 and nums[p2] == 2:
                p2 -= 1
            while p1 <= p2 and nums[p1] == 0:
                p1 += 1
            if i < p1:
                i = p1
