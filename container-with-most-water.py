class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        maxArea = min(height[left],height[right])*(right-left)
        while right != left:
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
            maxArea = max(maxArea, (right-left)*min(height[left],height[right]))
        return maxArea
    
    # O(n^2) too slow!!        
    # def maxArea(self, height):
    #     ptr1 = height
    #     ptr2 = height
    #     maxArea = 0
    #     for ptr1 in range(len(height)-1):
    #         for ptr2 in range(ptr1+1,len(height)):
    #             maxArea = max(maxArea, (ptr2-ptr1)*min(height[ptr1],height[ptr2]))
    #     return maxArea