import bisect


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = dict()
        ranking = []

        def insertionsort(cnt, num):
            ranking.insert(bisect.bisect(ranking, (cnt, num)), (cnt, num))

        for num in nums:
            if num in counter:
                ranking.remove((counter[num], num))
                counter[num] += 1
                insertionsort(counter[num], num)
            else:
                counter[num] = 1
                insertionsort(1, num)

        return [item[1] for item in ranking[:-(k + 1):-1]]


if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))
