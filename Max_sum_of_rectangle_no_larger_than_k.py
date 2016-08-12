class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # self.dp = [[[0] for _ in range()]]

        # Allocate storage
        self.dp = [[[0 for i in range(len(matrix[0]) - j)] for j in range(len(matrix[0]))] for m in range(len(matrix))]

        output = 0

        for row_i, row in enumerate(matrix):
            # Initialize base layer
            for i in range(len(row)):
                self.dp[row_i][0][i] = row[i]
                if self.dp[row_i][0][i] == k:
                    # print('p1', k, self.dp[row_i][0], i)
                    return k
                elif self.dp[row_i][0][i] < k:
                    output = max(output, self.dp[row_i][0][i])

            # Calculate the higher layers and compare with k
            for j in range(1, len(row)):
                for i in range(len(row) - j):
                    self.dp[row_i][j][i] = self.dp[row_i][j - 1][i] + self.dp[row_i][0][i + j]
                    if self.dp[row_i][j][i] == k:
                        # print('p2')
                        return k
                    elif self.dp[row_i][j][i] < k:
                        output = max(output, self.dp[row_i][j][i])

        # Row by row aggregation
        self.dpRows = [[0 for i in range(len(matrix) - j)] for j in range(len(matrix))]

        for j in range(len(matrix[0])):
            for m in range(len(matrix[0]) - j):
                # initialize base layer
                for i in range(len(matrix)):
                    self.dpRows[0][i] = self.dp[i][j][m]

                # Hierarchy
                for a in range(1, len(matrix)):
                    for b in range(len(matrix) - a):
                        self.dpRows[a][b] = self.dpRows[a - 1][b] + self.dpRows[0][a + b]
                        if self.dpRows[a][b] == k:
                            return k
                        elif self.dpRows[a][b] < k:
                            output = max(output, self.dpRows[a][b])

        # print('final')
        return output


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSumSubmatrix([[2, 2, 1]], 2))
