__author__ = 'stephenosullivan'

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        return self.inorder(root, k)

    def inorder(self, node, cnt):
        nodes_to_visit = []
        while node:
            nodes_to_visit.append(node)
            node = node.left

        node = nodes_to_visit.pop()

        while True:
            # Going down
            while node.left:
                nodes_to_visit.append(node)
                node = node.left

            cnt -= 1
            if cnt == 0:
                return node.val

            # Going up
            while node.right is None:
                node = nodes_to_visit.pop()
                cnt -= 1
                if cnt == 0:
                    return node.val

            if node.right:
                node = node.right
