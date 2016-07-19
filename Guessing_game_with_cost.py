class GuessingGame:
    def __init__(self, nums):
        # Matrix containing (worst cost, choice which produces minimum worst cost)
        self.dp = [[(0, 0) for _ in range(len(nums) + 1)] for _ in range(len(nums) + 1)]

        # for i in range(len(nums)-1):
        #     self.dp[i][i+1] = nums[i]

        for diff in range(1, len(nums) + 1):
            for left in range(len(nums) - diff + 1):
                right = left + diff
                self.dp[left][right] = min((
                                               nums[index] + max(self.dp[left][index][0], self.dp[index + 1][right][0]),
                                               index) for index in range(left, right))

        self.averageDP = [[(0, 0) for _ in range(len(nums) + 1)] for _ in range(len(nums) + 1)]

        for left in range(len(nums)):
            right = left + 1
            self.averageDP[left][right] = (nums[left], left)

        # print(self.averageDP)

        for diff in range(2, len(nums) + 1):
            for left in range(len(nums) - diff + 1):
                right = left + diff
                self.averageDP[left][right] = min([(nums[index] + ((
                                                                       (index - left) * self.averageDP[left][index][
                                                                           0] + (right - index - 1) *
                                                                       self.averageDP[index + 1][right][0]) / (
                                                                   diff - 1)), index) for index in range(left, right)])
                # print(self.averageDP[left][right])

    def guessPattern(self, nums):
        if len(nums) == 0:
            return 0, 0
        if len(nums) == 1:
            return nums[0], 0
        return min(
            (i + max(self.guessPattern(nums[:i])[0], self.guessPattern(nums[i + 1:])[0]), i) for i in range(len(nums)))

    def guessPattern_v2(self, target):
        left = 0
        right = len(self.dp) - 1
        choices = []
        while True:
            choice = self.dp[left][right][1]
            choices.append(choice)
            if choice == target:
                break
            elif target < choice:
                right = choice
            else:
                left = choice + 1

        return choices

    def guessPatternAverage(self, target):
        left = 0
        right = len(self.averageDP) - 1
        choices = []
        while True:
            choice = self.averageDP[left][right][1]
            # print(left, right, choice)
            choices.append(choice)
            if choice == target:
                break
            elif target < choice:
                right = choice
            else:
                left = choice + 1

        return choices

    def printDP(self):
        print(self.dp)

    def worstChoices(self):
        left = 0
        right = len(self.dp) - 1

        choices = []

        while left < right:
            choice = self.dp[left][right][1]
            choices.append(choice)
            if self.dp[choice + 1][right] > self.dp[left][choice]:
                left = choice + 1
            else:
                right = choice

        return choices

    def performance(self):
        sumMinWorst = 0
        sumAverage = 0
        for target in nums:
            sumMinWorst += sum(self.guessPattern_v2(target))
            sumAverage += sum(self.guessPatternAverage(target))

        return sumMinWorst, sumAverage


if __name__ == '__main__':
    nums = [i for i in range(10)]
    target = 3
    sol = GuessingGame(nums)
    print(sol.guessPattern_v2(target), sum(sol.guessPattern_v2(target)))
    sol.printDP()
    print(sol.averageDP)
    print(sol.worstChoices(), sum(sol.worstChoices()))
    print(sol.guessPatternAverage(target), sum(sol.guessPatternAverage(target)))

    print(sol.performance())
