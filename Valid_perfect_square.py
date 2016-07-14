class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        test = 1
        while test ** 2 < num:
            test *= 2

        upper = test
        lower = test >> 1

        while upper > lower and upper ** 2 > num and lower ** 2 < num:
            mid = (upper + lower) >> 1
            if mid ** 2 < num:
                lower = mid + 1
            else:
                upper = mid

        return upper ** 2 == num or lower ** 2 == num


if __name__ == '__main__':
    sol = Solution()

    print(sol.isPerfectSquare(808201))
