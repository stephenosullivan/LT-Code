class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        queue = [(0, 0)] * len(nums)
        divisors = dict()

        for i in range(len(nums)):
            for j, item in enumerate(queue[:i]):
                if nums[i] % item[1] == 0:
                    newCnt = item[0] + 1
                    left = 0
                    right = i - 1
                    while left < right:
                        mid = (left + right) // 2
                        if queue[mid][0] >= newCnt:
                            left = mid + 1
                        else:
                            right = mid

                    queue.insert(left, (newCnt, nums[i]))
                    divisors[nums[i]] = set(divisors[item[1]])
                    divisors[nums[i]].add(nums[i])
                    break
            else:
                queue.insert(i, (1, nums[i]))
                divisors[nums[i]] = {nums[i]}

        return list(divisors[queue[0][1]])


if __name__ == '__main__':
    sol = Solution()
    test = [1, 2, 3, 4, 8]
    print(sol.largestDivisibleSubset(test))
