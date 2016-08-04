# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # choose to steal from current house and skip the next or skip current and see if its worthwhile to steal from the next
        self.memo = dict()
        return self.rob_recursive(root)

    def rob_recursive(self, current):
        if current not in self.memo:
            if current:
                if self.children(current):
                    self.memo[current] = max(current.val + sum(map(self.rob_recursive, self.grandchildren(current))),
                                             sum(map(self.rob_recursive, self.children(current))))
                else:
                    self.memo[current] = current.val
            else:
                self.memo[current] = 0
        return self.memo[current]

    def children(self, current):
        if current.left:
            yield current.left
        if current.right:
            yield current.right

    def grandchildren(self, current):
        for child in self.children(current):
            for grandchild in self.children(child):
                yield grandchild
