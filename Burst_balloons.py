class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums[left] * nums[i] * nums[right]
        # pad with unburstable balloons of value one

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0
        return self.helper([1] + nums + [1])

    def helper(self, nums):
        if len(nums) == 3:
            return nums[1]
        return max(
            self.helper(nums[:i] + nums[i + 1:]) + nums[i - 1] * nums[i] * nums[i + 1] for i in range(1, len(nums) - 1))


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxCoins([35, 16, 83, 87, 84, 59, 48, 41, 20, 54]))
