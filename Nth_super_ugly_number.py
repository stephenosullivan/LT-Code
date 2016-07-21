class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        dp = [0] * n
        dp[0] = 1
        primeptrs = [0] * len(primes)

        for i in range(1, n):
            dp[i] = min(dp[ptr] * primes[index] for index, ptr in enumerate(primeptrs))
            for index, ptr in enumerate(primeptrs):
                if dp[ptr] * primes[index] == dp[i]:
                    primeptrs[index] += 1

        return dp[-1]
