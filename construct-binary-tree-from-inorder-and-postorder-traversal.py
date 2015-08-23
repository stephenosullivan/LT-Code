__author__ = 'stephenosullivan'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        def _buildTree(inorder, postorder):
            if postorder:
                if len(postorder) == 1:
                    return TreeNode(postorder[0])

                # check equality (long left branch)
                if inorder == postorder:
                    node = TreeNode(inorder[-1])
                    head = node
                    for i in inorder[-2::-1]:
                        node.left = TreeNode(i)
                        node = node.left
                    return head

                # check reverse (long right branch)
                if inorder == reversed(postorder):
                    node = TreeNode(postorder[-1])
                    head = node
                    for i in postorder[-2::-1]:
                        node.right = TreeNode(i)
                        node = node.right
                    return head

                # Partition into left and right branches
                node = TreeNode(postorder[-1])
                indexright = len(postorder) - 1
                # Find partition point
                while postorder[-1] != inorder[indexright]:
                    indexright -= 1
                node.right = _buildTree(inorder[indexright + 1:], postorder[indexright:-1])
                node.left = _buildTree(inorder[:indexright], postorder[:indexright])
                return node

        return _buildTree(inorder, postorder)
