class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if matrix:
            rowsize = len(matrix)
            colsize = len(matrix[0])
            self.accumulator = [[0 for _ in range(colsize + 1)] for _ in range(rowsize + 1)]
            for i in range(1, rowsize + 1):
                for j in range(1, colsize + 1):
                    self.accumulator[i][j] = self.accumulator[i - 1][j] + self.accumulator[i][j - 1] + matrix[(i - 1)][
                        j - 1] - self.accumulator[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.accumulator[row2 + 1][col2 + 1] - self.accumulator[row2 + 1][col1] - (
        self.accumulator[row1][col2 + 1] - self.accumulator[row1][col1])


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)

if __name__ == '__main__':
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    test = [2, 1, 4, 3]
    sol = NumMatrix(matrix)
    print(sol.sumRegion(2, 1, 4, 3))
