class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.memo = dict()
        return self.helper(n)

    def helper(self, n):
        if n == 1:
            return 0

        if n not in self.memo:
            # Even
            if not n % 2:
                self.memo[n] = 1 + self.helper(n // 2)

            # Odd
            else:
                self.memo[n] = 1 + min(self.helper(n - 1), self.helper(n + 1))
        return self.memo[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.integerReplacement(7))
    print(sol.memo)
