__author__ = 'stephenosullivan'

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if nums:
            length = len(nums)
            lennums = len(nums)
            i = 0
            j = 1
            while j < lennums:
                if nums[i] == nums[j]:
                    j += 1
                    length -= 1
                else:
                    i += 1
                    nums[i] = nums[j]
                    j += 1
            return length

        else:
            return 0

if __name__ == '__main__':
    a = [1, 2, 2]
    sol = Solution()
    print(sol.removeDuplicates(a))
