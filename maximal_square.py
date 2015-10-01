__author__ = 'stephenosullivan'


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        savedlength = 0

        if matrix:
            self.matrix = matrix
            self.width = len(matrix[0])
            self.height = len(matrix)

            for i, row in enumerate(matrix):
                for j, elem in enumerate(row):
                    if elem == '1':
                        savedlength = self.squarecheck(i, j, savedlength + 1) or savedlength
        return savedlength ** 2

    def squarecheck(self, i, j, minlength):
        k = minlength
        if i + k - 1 < self.height and j + k - 1 < self.width:
            m = 0
            while m < k and all([int(elem) for elem in self.matrix[i + m][j:j + k]]):
                m += 1
            if m == k:
                return self.squarecheck(i, j, minlength + 1) or minlength

        return False
