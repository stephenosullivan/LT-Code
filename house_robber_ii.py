__author__ = 'stephenosullivan'


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        sum1 = [0, nums[-1]]
        sum2 = [0, 0]

        for i, num in enumerate(nums[:-2]):
            print(sum1[0], sum1[1], sum2[0], sum2[1])
            sum1[1], sum1[0] = max(num + sum1[0], sum1[1]), sum1[0]
            print(sum1[0], sum1[1], sum2[0], sum2[1])
            sum2[0], sum2[1] = max(num + sum2[0], sum2[1]), sum2[0]
        print(sum1[0], sum1[1], sum2[0], sum2[1])
        sum2[0] = max(nums[-2] + sum2[1], sum2[0])
        print(sum1[0], sum1[1], sum2[0], sum2[1])

        return max(sum1[0], sum1[1], sum2[0], sum2[1])

    def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        output1 = self.robwith(nums[:-1])
        output2 = self.robwith(nums[1:])

        return max(output1, output2)

    def robwith(self, nums):
        memo = [None] * len(nums)
        return self.roblinear(0, memo, nums)

    def roblinear(self, index, memo, nums):
        if index < len(nums):
            if memo[index] is None:
                memo[index] = max(nums[index] + self.roblinear(index + 2, memo, nums),
                                  self.roblinear(index + 1, memo, nums))
            return memo[index]
        else:
            return 0


if __name__ == '__main__':
    print(Solution().rob([1, 2, 1, 0]))
