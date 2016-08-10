import operator


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        opdict = {'*': operator.mul, '+': operator.add, '-': operator.sub}
        self.ops = []
        self.values = []

        lastindex = 0
        for index, c in enumerate(input):
            if c in opdict:
                self.ops.append(opdict[c])
                self.values.append(int(input[lastindex:index]))
                lastindex = index + 1
        self.values.append(int(input[lastindex:]))
        self.dp = [[None for _ in range(len(self.ops) + 1)] for _ in range(len(self.ops) + 1)]
        for i in range(len(self.ops) + 1):
            self.dp[i][i] = [self.values[i]]
        return self.recursiveCompute(0, len(self.ops))

    def recursiveCompute(self, i, j):
        if self.dp[i][j] == None:
            self.dp[i][j] = []
            for opindex in range(i, j):
                for leftside in self.recursiveCompute(i, opindex):
                    for rightside in self.recursiveCompute(opindex + 1, j):
                        self.dp[i][j].append(self.ops[opindex](leftside, rightside))
        return self.dp[i][j]


if __name__ == '__main__':
    sol = Solution()
    print(sol.diffWaysToCompute('2-1-1'))
    print(sol.dp)
