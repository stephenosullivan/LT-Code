class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        rawSum = sum(A)

        F = [None] * len(A)
        for i in range(len(A)):
            F[i] = i * A[i]

        maximum = sum(F)
        current = maximum
        for i in range(1, len(A)):
            diff = rawSum - len(A) * A[-i]

            current += diff
            print(maximum, current, rawSum, diff)
            maximum = max(maximum, current)

        return maximum


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxRotateFunction([4, 3, 2, 6]))
