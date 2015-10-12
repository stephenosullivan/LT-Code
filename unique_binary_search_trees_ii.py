__author__ = 'stephenosullivan'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __iter__(self):
        queue = [self, '$']
        level = []
        while len(queue) > 1:
            node = queue.pop(0)
            if node == '$':
                yield level
                level = []
                queue.append('$')
            else:
                if node is None:
                    level.append(node)
                else:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

                    # if self.left:
                    #     for i in self.left.__iter__():
                    #         yield i
                    # else:
                    #     yield None
                    # yield self.val
                    #
                    # if self.right:
                    #     for i in self.right.__iter__():
                    #         yield i
                    # else:
                    #     yield None

    def __repr__(self):
        return 'Tree(' + repr(list([i for i in self])) + ')'


class Solution(object):
    def __init__(self):
        self.memo = dict()

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        for i in range(n + 1):
            self.memo[i] = []

        output = [node for node in self.blankTree(n)]
        # for node in output:
        #     self.fillTree(node)
        return output

    def fillTree(self, node, val=0):
        if node is None:
            return val
        else:
            node.val = self.fillTree(node.left, val) + 1
            return self.fillTree(node.right, node.val)

    def blankTree(self, n):
        if n == 0:
            yield None
        if not self.memo[n]:
            for i in range(n):
                for left in self.blankTree(i):
                    for right in self.blankTree(n - i - 1):
                        root = TreeNode(None)
                        root.left = left
                        root.right = right
                        self.memo[n].append(root)

        for node in self.memo[n]:
            yield node


if __name__ == '__main__':
    a = TreeNode(None)
    a.left = TreeNode(None)

    b = TreeNode(None)
    b.right = TreeNode(None)
    # b.left = TreeNode(None)

    Solution().fillTree(a)
    print(a.val)
    print(a.left.val)

    # Solution().fillTree(b)
    print(b.val)
    print(b.right.val)

    print(a)
    print(b)

    for node in Solution().generateTrees(2):
        print(node)
