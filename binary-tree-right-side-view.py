__author__ = 'stephenosullivan'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        output = []
        level = 1
        levelmax = 0

        # Store nodes as a tuple with a level indicator
        nodes_to_visit = [(root, level)]

        # Sweep through the tree; 'right' branches first
        while nodes_to_visit:
            node, level = nodes_to_visit.pop()
            while node:
                if node.left:
                    nodes_to_visit.append((node.left, level + 1))
                if level > levelmax:
                    output.append(node.val)
                    levelmax += 1
                level += 1
                node = node.right

        return output
