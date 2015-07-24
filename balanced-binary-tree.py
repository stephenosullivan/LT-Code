__author__ = 'stephenosullivan'

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        if root:
            return self.recursive(root) != False
        else:
            return True

    def recursive(self, node):
        if node is None:
            return 1
        leftmax = self.recursive(node.left)
        rightmax = self.recursive(node.right)
        if not leftmax or not rightmax:
            return False
        elif abs(leftmax - rightmax) > 1:
            return False
        else:
            return max(leftmax, rightmax) + 1