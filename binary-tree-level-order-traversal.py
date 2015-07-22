__author__ = 'stephenosullivan'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        level = [root] if root else []
        nextlevel = []
        output = []
        while level:
            output.append([i.val for i in level])
            for node in level:
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            level = nextlevel
            nextlevel = []
        return output