__author__ = 'stephenosullivan'

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        i = 0; j = len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False


    #     height = len(matrix)
    #     width = len(matrix[0])
    #     print(width, height)
    #     if width > 1 and height > 1:
    #         row = len(matrix)//2
    #         col = len(matrix[0])//2
    #         if target == matrix[row][col]:
    #             return True
    #         elif target < matrix[row][col]:
    #             return self.searchMatrix(matrix[:row][:col], target)
    #         else:
    #             if row >= col:
    #                 index = self.binarySearch1D([matrix[i][col] for i in range(height)], 0, target)
    #                 return self.searchMatrix(matrix[0:index][col+1:], target) or self.searchMatrix(matrix[index:][0:col], target)
    #
    #             else:
    #                 index = self.binarySearch1D([matrix[row][j] for j in range(width)], 0, target)
    #                 return self.searchMatrix(matrix[0:row][index:], target) or self.searchMatrix(matrix[row+1:][0:index], target)
    #
    #     elif width > 1:
    #         index = self.binarySearch1D(matrix[0][:], 0, target)
    #         return False
    #     elif height > 1:
    #         index = self.binarySearch1D(matrix[:][0], 0, target)
    #         return False
    #     else:
    #         return target == matrix[0][0]
    #
    # def binarySearch1D(self, vector, index, target):
    #     if vector[0]==target:
    #         return True
    #     elif len(vector)==1:
    #         return index
    #     else:
    #         mid = len(vector)//2
    #         left = vector[:mid]
    #         right = vector[mid:]
    #
    #
    #         if target <= vector[mid]:
    #             self.binarySearch1D(left, index, target)
    #         else:
    #             self.binarySearch1D(right, index + mid, target)

if __name__ == '__main__':
    a = [[1,4], [2,5]]
    target = 6
    sol = Solution()
    print(sol.searchMatrix(a,target))