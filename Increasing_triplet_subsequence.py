import bisect


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seq = []
        for num in nums:
            index = bisect.bisect_left(seq, num)
            if index < len(seq):
                seq[index] = num
            elif index == 2:
                return True
            else:
                seq.append(num)

        return False
