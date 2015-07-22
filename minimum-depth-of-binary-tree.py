__author__ = 'stephenosullivan'

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        # Breadth first search --- level traversal
        if root:
            nodes_to_traverse_next = [root]
            cnt = 0
            while nodes_to_traverse_next:
                nodes_to_traverse = nodes_to_traverse_next
                nodes_to_traverse_next = []
                cnt += 1
                while nodes_to_traverse:
                    node = nodes_to_traverse.pop()
                    if node.left is None and node.right is None:
                        return cnt
                    if node.left:
                        nodes_to_traverse_next.append(node.left)
                    if node.right:
                        nodes_to_traverse_next.append(node.right)

        else:
            return 0
