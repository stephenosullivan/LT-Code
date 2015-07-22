__author__ = 'stephenosullivan'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        path = [root]
        branches = []
        lastbranch = root
        found = False
        node = path.pop()

        # Find First Node
        while not found:
            if node == p:
                r = q
                found = True
                node2 = node
            elif node == q:
                r = p
                found = True
                node2 = node
            else:
                if node.right:
                    branches.append(node)
                if node.left:
                    node = node.left
                else:
                    node = (branches.pop()).right

        # Get nodes inorder
        if not branches:
            return node2
        if node2.right:
            branches.append(node2)
        if node2.left:
            lastbranch = node2
            node = node2.left
        else:
            lastbranch = branches.pop()
            if not branches:
                return lastbranch
            node = lastbranch.right

        # Find second node
        while True:
            if r == node:
                return lastbranch
            if node.right:
                path.append(node)
            if node.left:
                node = node.left
            elif path:
                node = (path.pop()).right
            else:
                lastbranch = branches.pop()
                if not branches:
                    return lastbranch
                path = [lastbranch.right]
                node = path.pop()
