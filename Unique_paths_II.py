class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        lenrows = len(obstacleGrid)
        lencols = len(obstacleGrid[0])

        numways = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]

        if obstacleGrid[0][0] == 0:
            numways[0][0] = 1
        else:
            return 0

        for col in range(1, lencols):
            if obstacleGrid[0][col] == 1:
                break
            numways[0][col] = 1

        for row in range(1, lenrows):
            if obstacleGrid[row][0] == 1:
                break
            numways[row][0] = 1

        for row in range(1, lenrows):
            for col in range(1, lencols):
                if obstacleGrid[row][col] == 0:
                    numways[row][col] = numways[row - 1][col] + numways[row][col - 1]
                else:
                    numways[row][col] = 0

        return numways[lenrows - 1][lencols - 1]
