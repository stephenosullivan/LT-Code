__author__ = 'stephenosullivan'

"""
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes
the sum of all numbers along its path.
"""

class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        self.memo = [[None for i in row] for row in grid]
        self.memo[-1][-1] = grid[-1][-1]

        # Do the sides first
        for col in range(len(grid[0])-2,-1,-1):
            self.memo[-1][col] = grid[-1][col] + self.memo[-1][col+1]
        for row in range(len(grid)-2, -1, -1):
            self.memo[row][-1] = grid[row][-1] + self.memo[row+1][-1]

        # Then the middle
        # for indexrow, row in reversed(list(enumerate(grid[:-1]))):
        #     for indexcol, col in reversed(list(enumerate(row[:-1]))):
        if self.memo[0][0] is None:
            for row in range(len(grid)-2,-1,-1):
                for col in range(len(grid[0])-2,-1,-1):
                    self.memo[row][col] = grid[row][col] + min(self.memo[row + 1][col], self.memo[row][col + 1])


        return self.memo[0][0]

