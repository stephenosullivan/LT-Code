__author__ = 'stephenosullivan'


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root:
            storedpaths = []
            queue = [[root]]
            while queue:
                path = queue.pop()
                if path[-1].left or path[-1].right:
                    if path[-1].left:
                        queue.append(path + [path[-1].left])
                    if path[-1].right:
                        queue.append(path + [path[-1].right])
                else:
                    storedpaths.append(path)

            return [self.stringify(path) for path in storedpaths]
        return []

    def stringify(self, path):
        strpath = ""
        if path:
            for node in path:
                strpath += str(node.val) + "->"
            return strpath[:-2]
        else:
            return ""
