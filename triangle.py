__author__ = 'stephenosullivan'

"""Given a triangle, find the minimum path sum from top to bottom.
    Each step you may move to adjacent numbers on the row below."""

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    #def __init__(self):
    #    self.triangledepth = 0
    def minimumTotal(self, triangle):
        self.triangledepth = len(triangle)
        self.memo = [[None for i in range(j + 1)] for j in range(self.triangledepth)]
        return self.recursiveMinPath(triangle,0,0)

    def recursiveMinPath(self,triangle,i,j):
        if i < self.triangledepth-1:
            if not self.memo[i+1][j]:
                self.memo[i+1][j] = self.recursiveMinPath(triangle,i+1,j)
            if not self.memo[i+1][j+1]:
                self.memo[i+1][j+1] = self.recursiveMinPath(triangle,i+1,j+1)
            return min(self.memo[i+1][j],self.memo[i+1][j+1]) + triangle[i][j]
        else:
            return triangle[i][j]
