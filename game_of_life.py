__author__ = 'stephenosullivan'

import copy


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        newboard = copy.deepcopy(board)
        self.EMPTY = 0
        self.ALIVE = 1
        self.width = len(board[0])
        self.height = len(board)
        for i, row in enumerate(board):
            for j, elem in enumerate(row):
                newboard[i][j] = self.gameLogic(board[i][j], self.countNeighbors(board, self.neighbors(i, j)))
        for i, row in enumerate(board):
            for j, elem in enumerate(row):
                board[i][j] = newboard[i][j]

    def neighbors(self, i, j):
        surrounding = {(i + 1, j), (i + 1, j + 1), (i, j + 1), (i - 1, j + 1), (i - 1, j), (i - 1, j - 1), (i, j - 1),
                       (i + 1, j - 1)}
        return {(i, j) for (i, j) in surrounding if -1 < i < self.height and -1 < j < self.width}

    def countNeighbors(self, board, neighbors):
        return sum([int(board[i][j]) for (i, j) in neighbors])

    def gameLogic(self, state, neighbors):
        if state == self.ALIVE:
            if neighbors < 2:
                return self.EMPTY
            elif neighbors > 3:
                return self.EMPTY
        else:
            if neighbors == 3:
                return self.ALIVE
        return state
