__author__ = 'stephenosullivan'

# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
from collections import deque


class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """

        if root:
            queue = deque()
            queue.append('$')
            queue.append(root)
            while len(queue) > 1:
                node = queue.popleft()
                if node == '$':
                    for i, ptr in enumerate(queue):
                        try:
                            ptr.next = queue[i + 1]
                        except:
                            ptr.next = None
                    queue.append(node)
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
