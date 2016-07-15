class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        dp = [i for i in range(n + 1)]

        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = max(dp[i - j] * dp[j] for j in range(i // 2 + 1))

        print(dp)
        return max(dp[n - i] * dp[i] for i in range(1, n // 2 + 1))


if __name__ == '__main__':
    sol = Solution()
    print(sol.integerBreak(58))
