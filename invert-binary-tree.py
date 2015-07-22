__author__ = 'stephenosullivan'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self,root):
        if root:
            nodes_to_visit = [root]
            while nodes_to_visit:
                ptr = nodes_to_visit.pop()
                if ptr.left:
                    nodes_to_visit.append(ptr.left)
                if ptr.right:
                    nodes_to_visit.append(ptr.right)
                ptr.left, ptr.right = ptr.right, ptr.left
        return root



    def invertTreeRecursive(self, root):
        if root:
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.left, root.right = root.right, root.left

        return root

