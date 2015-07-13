__author__ = 'stephenosullivan'

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        output = [[]]
        outputList = []
        for i in candidates:
            if i < target:
                output.append([i])
            if i == target:
                outputList.append([i])

        while output:
            for sums in output:
                hit = False
                for i in candidates:
                    if sums and i >= sums[-1]:
                        if sum(sums) + i < target:
                            output.append(sums.append(i))
                            hit = True
                        if sum(sums) + i == target:
                            outputList.append(sums.append(i))
                output.pop(0)

        return outputList


sol = Solution()
cand = [1]
target = 2
print(sol.combinationSum(cand, target))
