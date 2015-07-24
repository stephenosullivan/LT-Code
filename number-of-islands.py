__author__ = 'stephenosullivan'

class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        if grid:
            cells_to_check = []
            count = 0
            jmax = len(grid)
            imax = len(grid[jmax-1])
            for j in range(jmax):
                for i in range(imax):
                    if grid[j][i] == '1':
                        cells_to_check.append((i,j))
                        while cells_to_check:
                            i0,j0 = cells_to_check.pop()
                            if grid[j0][i0] == '1':
                                grid[j0][i0] = '0'
                                if i0 + 1 < imax:
                                    cells_to_check.append((i0+1,j0))
                                if j0 + 1 < jmax:
                                    cells_to_check.append((i0,j0+1))
                                if i0 > 0:
                                    cells_to_check.append((i0-1,j0))
                                if j0 > 0:
                                    cells_to_check.append((i0,j0-1))
                        count += 1

            return count

        else:
            return 0
