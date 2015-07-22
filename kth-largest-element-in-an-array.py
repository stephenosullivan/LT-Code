__author__ = 'stephenosullivan'

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        return self.recursiveFind(nums,0,len(nums)-1,len(nums)-k)

    def recursiveFind(self,nums,left,right,k):
        if left == right:
            return nums[left]
        pivotIndex = int((left+right+1)/2)
        pivotIndex = self.partition(nums,left,right,pivotIndex)

        if k==pivotIndex:
            return nums[k]

        elif k<pivotIndex:
            return self.recursiveFind(nums,left,pivotIndex-1,k)

        else:
            return self.recursiveFind(nums,pivotIndex+1,right,k)

    def partition(self,nums,left,right,pivot):
        pivotVal = nums[pivot]
        index = left
        outindex = left
        nums[pivot],nums[right] = nums[right],nums[pivot]
        for index in range(left,right):
            if nums[index] < pivotVal:
                nums[index],nums[outindex] = nums[outindex],nums[index]
                outindex += 1

        nums[outindex],nums[right] = nums[right],nums[outindex]
        return outindex