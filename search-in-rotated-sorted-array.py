__author__ = 'stephenosullivan'

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        pivot = self.binarySearchPivot(nums, 0)
        print('pivot', pivot)

        if target <= nums[-1]:
            x = self.binarySearch(nums[pivot:], 0 + pivot, target)
            return -1 if x is None else x[0]
        else:
            x = self.binarySearch(nums[:pivot], 0, target)
            return -1 if x is None else x[0]


    def binarySearchPivot(self, nums, index):
        length = len(nums)
        print(nums)
        if length > 1:
            mid = length//2
            left = nums[:mid]
            right = nums[mid:]
            if left[-1] > right[0]:
                return mid + index
            elif left[0] > right[-1]:
                if length > 2:
                    return self.binarySearchPivot(left, index) + self.binarySearchPivot(right, index + mid)
                else:
                    return index + 1
            else:
                return 0
        else:
            return 0

    def binarySearch(self, nums, index, target):
        print('nums', nums)
        length = len(nums)
        if length > 1:
            mid = length//2
            left = nums[:mid]
            right = nums[mid:]

            return self.binarySearch(left, index, target) or self.binarySearch(right, index + mid, target)
        elif len(nums) == 1 and nums[0] == target:
            return (index,)

if __name__ == '__main__':
    array = [5,1,3]
    target = 5
    sol = Solution()
    print(sol.search(array, target))
