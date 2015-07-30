__author__ = 'stephenosullivan'

"""
Determine if a Sudoku is valid
"""


class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        for row in board:
            set_check = set()
            for elem in row:
                if elem != '.':
                    if elem not in set_check:
                        set_check.add(elem)
                    else:
                        return False

        for i in range(9):
            set_check = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] not in set_check:
                        set_check.add(board[j][i])
                    else:
                        return False

        for i in range(3):
            for j in range(3):
                set_check = set()
                for m in range(3):
                    for n in range(3):
                        if board[m+3*i][n+3*j] != '.':
                            if board[m+3*i][n+3*j] not in set_check:
                                set_check.add(board[m+3*i][n+3*j])
                            else:
                                return False
        return True
