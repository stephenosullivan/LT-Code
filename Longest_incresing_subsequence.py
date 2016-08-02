import bisect


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sequence = []
        for num in nums:
            index = bisect.bisect_left(sequence, num)
            if index < len(sequence):
                sequence[index] = num
            else:
                sequence.append(num)

        return len(sequence)
