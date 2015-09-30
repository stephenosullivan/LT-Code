__author__ = 'stephenosullivan'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfsTraverse(root, 0, 0)

    def dfsTraverse(self, node, num, total):
        if node is None:
            return total

        num = num * 10 + node.val
        if node.left is None and node.right is None:
            total += num
            return total

        return self.dfsTraverse(node.left, num, total) + self.dfsTraverse(node.right, num, total)

    # Method with saved paths
    def sumNumbersSlow(self, root):

        self.paths = []
        self.maxdepth = 0
        self.recursiveTraverse(root, [])

        output = 0
        for path in self.paths:
            depth = self.maxdepth - 1
            for val in path:
                output += val * 10 ** depth
                depth -= 1

        return output

    def recursiveTraverse(self, root, path):
        if root:
            path.append(root.val)
            if root.left or root.right:
                if root.left:
                    self.recursiveTraverse(root.left, path)
                if root.right:
                    self.recursiveTraverse(root.right, path)
            else:
                self.paths.append(path)
                self.maxdepth = max(self.maxdepth, len(path))
