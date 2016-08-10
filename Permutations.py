class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.recursivebuild(nums)

    def recursivebuild(self, numbers):
        if len(numbers) == 1:
            return [[numbers[0]]]
        output = []
        for index, number in enumerate(numbers):
            for suffix in self.recursivebuild(numbers[:index] + numbers[index + 1:]):
                output.append([number] + suffix)
        return output


if __name__ == '__main__':
    sol = Solution()
    print(sol.permute([1, 2, 3]))
