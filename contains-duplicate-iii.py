__author__ = 'stephenosullivan'

import collections


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 1 or t < 0:
            return False
        numDict = collections.OrderedDict()
        for index, val in enumerate(nums):
            key = val / (t + 1)
            for m in (key, key - 1, key + 1):
                if m in numDict and abs(val - numDict[m]) <= t:
                    return True
            numDict[key] = val
            if index >= k:
                numDict.popitem(last=False)
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.containsNearbyAlmostDuplicate([4, 1, 6, 3, 1], 100, 1))
