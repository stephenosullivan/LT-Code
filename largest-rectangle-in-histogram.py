__author__ = 'stephenosullivan'

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        height = [0] + height + [0]
        stack = [0]
        area = 0

        for i, x in enumerate(height):
            while x < height[stack[-1]]:
                y = height[stack.pop()]
                print('y',y, ' stack[-1]',height[stack[-1]], i-1-stack[-1])
                area = max(area, (i-1-stack[-1])*y)
            stack.append(i)
            print('i',height[i])
        return area

    # Too verbose
    def largestRectangleAreaLong(self, height):
        height = [0] + height
        indexStack = []
        maxArea = 0
        for i in range(len(height)):
            if not indexStack or height[i] > height[indexStack[-1]]:
                indexStack.append(i)
            elif height[i] < height[indexStack[-1]]:
                while indexStack and height[indexStack[-1]] > height[i]:
                    h = indexStack.pop()
                    area = (i - indexStack[-1] - 1)*height[h]
                    maxArea = max(maxArea, area)
                indexStack.append(i)
            else:
                indexStack[-1] = i
        i = len(height) - 1
        for j in indexStack:
            print('j',j)
        print('big',height[9])
        while len(indexStack)>1:
            h = indexStack.pop()
            area = (i - indexStack[-1]) * height[h]
            maxArea = max(maxArea, area)
        print(h)
        return maxArea

sol = Solution()
print(sol.largestRectangleArea([3,2,5,6,2,1]))
