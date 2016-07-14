class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.accumulator = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.accumulator[i] = self.accumulator[i - 1] + nums[i - 1]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """

        return self.accumulator[j + 1] - self.accumulator[i]


class NumArray_v1(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.store = dict()

        for i in range(len(nums)):
            self.store[(i, i)] = nums[i]
            for j in range(i + 1, len(nums)):
                self.store[(i, j)] = self.store[(i, j - 1)] + nums[j]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """

        return self.store[(i, j)]



        # Your NumArray object will be instantiated and called as such:
        # numArray = NumArray(nums)
        # numArray.sumRange(0, 1)
        # numArray.sumRange(1, 2)
