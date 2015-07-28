__author__ = 'stephenosullivan'

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        while k:
            nums.insert(0,nums[-1])
            nums.pop()
            k -= 1

if __name__ == "__main__":
    sol = Solution()
    a = [1, 2, 3, 4, 5, 6, 7]
    print(sol.rotate(a, 3))
    print(a)
