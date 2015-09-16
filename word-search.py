__author__ = 'stephenosullivan'


class Solution(object):
    def exist(self, board, word):
        self.width = len(board[0])
        self.height = len(board)
        for j, row in enumerate(board):
            for i, letter in enumerate(row):
                if self.letter_check(board, i, j, word):
                    return True
        return False

    def letter_check(self, board, i, j, word):
        if board[j][i] == word[0]:
            board[j][i] = '.'
            if len(word) == 1:
                return True
            elif self._exist(board, word[1:], i, j):
                return True
            board[j][i] = word[0]

    def _exist(self, board, word, i0, j0):
        for i, j in self.adjacent(board, i0, j0):
            if self.letter_check(board, i, j, word):
                return True

    def adjacent(self, board, i, j):
        neighbors = {(i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)}
        return [neighbor for neighbor in neighbors if
                0 <= neighbor[0] < self.width and 0 <= neighbor[1] < self.height and board[neighbor[1]][
                    neighbor[0]] != '.']

# Little slow: Builds a dict of positions of each letter
# class Solution(object):
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """
#         letter_dict = dict()
#         self.load_dict(board, letter_dict)
#
#         height = len(board)
#         width = len(board[0])
#
#         if word[0] in letter_dict:
#             for position in letter_dict[word[0]]:
#                 tmp = copy.deepcopy(letter_dict)
#                 self._exists(word[1:], position, tmp[word[0]].remove(position), board, width, height)
#
#         return False
#
#     def load_dict(self, board, letter_dict):
#             for j, row in enumerate(board):
#                 for i, letter in enumerate(row):
#                     if letter not in letter_dict:
#                         letter_dict[letter]= set()
#                     letter_dict[letter].add((i,j))
#
#     def adjacent(self, i, j, width, height):
#         prelim = [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]
#         return {(i, j) for (i, j) in prelim if -1 < i < width and -1 < j < height}
#
#     def _exists(self, word, previous, letter_dict, board, width, height):
#         if not word:
#             return True
#         elif letter_dict and word[0] in letter_dict:
#             for (i, j) in self.adjacent(previous[0], previous[1], width, height):
#                 if (i, j) in letter_dict[word[0]]:
#                     self._exists(word[1:], (i,j), letter_dict[word[0]].remove((i, j)), board, width, height)

if __name__ == '__main__':
    sol = Solution()
