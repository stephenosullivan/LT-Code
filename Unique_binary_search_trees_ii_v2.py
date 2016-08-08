# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        self.dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            self.dp[i][i] = [None]
        return self.recurse(0, n)

    def recurse(self, i, j):
        if self.dp[i][j] == 0:
            self.dp[i][j] = []
            for k in range(i, j):
                for leftnode in self.recurse(i, k)[:]:
                    for rightnode in self.recurse(k + 1, j)[:]:
                        head = TreeNode(k + 1)
                        head.left = leftnode
                        head.right = rightnode
                        self.dp[i][j].append(head)

        return self.dp[i][j]


if __name__ == '__main__':
    sol = Solution()
    print(sol.generateTrees(2))
    print(sol.dp)
