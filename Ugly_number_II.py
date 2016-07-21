class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * n
        p2, p3, p5 = 0, 0, 0
        dp[0] = 1

        for i in range(1, n):
            dp[i] = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
            if dp[p2] * 2 == dp[i]:
                p2 += 1
            if dp[p3] * 3 == dp[i]:
                p3 += 1
            if dp[p5] * 5 == dp[i]:
                p5 += 1

        return dp[-1]

    def nthUglyNumberNotDP(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Too Slow
        twos, threes, fives = 0, 2, 2
        cnt = 1
        current = 2

        dp = [0, 1]
        while cnt < n:
            ugly = False
            if twos == 0:
                if dp[current / 2]:
                    ugly = True

            if not ugly and threes == 0:
                if dp[current / 3]:
                    ugly = True

            if not ugly and fives == 0:
                if dp[current / 5]:
                    ugly = True

            if ugly:
                cnt += 1
            dp.append(ugly)
            current += 1
            twos = (twos + 1) % 2
            threes = (threes + 1) % 3
            fives = (fives + 1) % 5
        return current - 1
