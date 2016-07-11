__author__ = 'stephenosullivan'

"""
Solve a**b % 1337 where b is a large int represented as a list
"""


class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        prime = 1337
        single = a % prime
        residual = 1

        """
        Iterate through the exponent list starting from the least significant digit
        and add the contribution to the result
        """
        for index, exponent in enumerate(reversed(b)):
            if exponent:
                residual = (residual * single ** exponent) % prime
            single = single ** 10 % prime

        return residual


if __name__ == '__main__':
    sol = Solution()
    a = 9
    b = [4, 6, 1]
    print(sol.superPow(a, b))
