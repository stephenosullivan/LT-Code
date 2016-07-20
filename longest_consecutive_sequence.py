__author__ = 'stephenosullivan'


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxcnt = 0
        visited = set()
        lowerdict = dict()
        upperdict = dict()
        for num in nums:
            if num not in visited:
                visited.add(num)
                print(upperdict)
                print(lowerdict)
                if num + 1 in lowerdict:
                    if num - 1 in upperdict:
                        newupper = lowerdict[num + 1]
                        newlower = upperdict[num - 1]

                        del lowerdict[num + 1]
                        del upperdict[num - 1]

                        lowerdict[newlower] = newupper
                        upperdict[newupper] = newlower

                        maxcnt = max(maxcnt, newupper - newlower + 1)

                    else:
                        oldupper = lowerdict[num + 1]
                        del lowerdict[num + 1]
                        lowerdict[num] = oldupper
                        upperdict[oldupper] = num
                        maxcnt = max(maxcnt, oldupper - num + 1)

                elif num - 1 in upperdict:
                    oldlower = upperdict[num - 1]
                    del upperdict[num - 1]
                    upperdict[num] = oldlower
                    lowerdict[oldlower] = num

                    maxcnt = max(maxcnt, num - oldlower + 1)

                else:
                    lowerdict[num] = num
                    upperdict[num] = num
                    maxcnt = max(maxcnt, 1)

        print(upperdict)
        print(lowerdict)
        return maxcnt


if __name__ == '__main__':
    sol = Solution()
    array = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    array = [-7, -1, 3, -9, -4, 7, -3, 2, 4, 9, 4, -9, 8, -7, 5, -1, -7]
    # array = [0]

    print(sol.longestConsecutive(array))
