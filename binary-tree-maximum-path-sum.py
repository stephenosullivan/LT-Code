__author__ = 'stephenosullivan'

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxPathSum(self, root):
        return self.recursive(root)[1]

    def recursive(self, node):
        if node:
            leftmax = self.recursive(node.left)
            rightmax = self.recursive(node.right)
            if leftmax[0] < 0:
                leftmax[0] = 0
            if rightmax[0] < 0:
                rightmax[0] = 0

            if leftmax[1] or rightmax[1] is None:
                nonetest = [leftmax[0] + rightmax[0] + node.val, leftmax[1], rightmax[1]]
                maxnonetest = max([i for i in nonetest if i is not None])
                return [max(leftmax[0], rightmax[0]) + node.val, maxnonetest]
            else:
                return [max(leftmax[0], rightmax[0]) + node.val, max(leftmax[0] + rightmax[0] + node.val, max(leftmax[1], rightmax[1]))]
        else:
            return [0, None]

if __name__ == '__main__':
    a = TreeNode(-3)
    sol = Solution()
    print(sol.maxPathSum(a))