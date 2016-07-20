class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = range(1, n + 1)
        self.dp = [[(0, 0) for _ in range(len(nums) + 1)] for _ in range(len(nums) + 1)]

        for diff in range(2, len(nums) + 1):
            for left in range(len(nums) - diff + 1):
                right = left + diff
                self.dp[left][right] = min((
                                               nums[index] + max(self.dp[left][index][0], self.dp[index + 1][right][0]),
                                               index) for index in range(left, right))

        return self.dp[0][-1][0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.getMoneyAmount(7))
