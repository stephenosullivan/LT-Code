__author__ = 'stephenosullivan'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            _, depth, basecnt = self.dfsTraverse(root, 0, 0, 0)
            print(depth, basecnt)
            return 2 ** depth + basecnt - 1
        else:
            return 0

    def dfsTraverse(self, node, cnt, depth, basecnt):
        # leaf node
        if node.left is None and node.right is None:
            if cnt < depth:
                return False, depth, basecnt
            else:
                depth = cnt
                return True, depth, basecnt + 1
        else:
            lefttest, newdepth, newbasecnt = self.dfsTraverse(node.left, cnt + 1, depth, basecnt)
            if lefttest:
                if node.right:
                    return self.dfsTraverse(node.right, cnt + 1, newdepth, newbasecnt)
            return lefttest, newdepth, newbasecnt
