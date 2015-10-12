__author__ = 'stephenosullivan'


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = [[None for i in range(m)] for j in range(n)]
        for i in range(m):
            grid[0][i] = 1
        for j in range(n):
            grid[j][0] = 1
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                if grid[i][j] is None:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

        return grid[len(grid) - 1][len(grid[0]) - 1] or 0
