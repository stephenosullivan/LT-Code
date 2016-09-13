import random


class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.cnt = dict()
        for index, num in enumerate(nums):
            if num in self.cnt:
                self.cnt[num].add(index)
            else:
                self.cnt[num] = set([index])

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(list(self.cnt[target]))


if __name__ == '__main__':
    sol = Solution([1, 2, 3, 3, 3])
    for _ in range(10):
        print(sol.pick(3))

    print(sol.cnt)
