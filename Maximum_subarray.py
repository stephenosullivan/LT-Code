class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        best = nums[0]
        current = max(0, nums[0])

        for item in nums[1:]:
            current += item

            if current > best:
                best = current

            current = max(0, current)
                
        return best

    def maxSubArrayDPTopDown(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def helper(left, right):
            if left == right:
                return nums[left], nums[left]

            leftside = helper(left, right - 1)
            rightside = helper(left + 1, right)
            currentmax = max(nums[left] + rightside[0], leftside[0] + nums[right])
            best = max(currentmax, leftside[1], rightside[1])
            return currentmax, best

        return helper(0, len(nums) - 1)[1]

    def maxSubArrayBestIncludingArrayIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        val, (i, j) = self.helper(0, len(nums) - 1)[1]
        return val

    def helper(self, left, right):
        if right == left:
            return self.nums[left], (self.nums[left], (left, right))

        currentmax = max(self.nums[right] + self.helper(left, right - 1)[0],
                         self.nums[left] + self.helper(left + 1, right)[0])
        best = max((currentmax, (left, right)), self.helper(left, right - 1)[1], self.helper(left + 1, right)[1],
                   lambda x: x[0])

        return currentmax, best
