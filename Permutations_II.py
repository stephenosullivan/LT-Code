from copy import deepcopy


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        counter = dict()
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        return self.recursiveUnique(counter)

    def recursiveUnique(self, counter):
        if len(counter.keys()) == 1:
            for ckey, cvalue in counter.items():
                return [[ckey] * cvalue]

        output = []
        for key in counter.keys():
            counter_copy = deepcopy(counter)
            if counter_copy[key] == 1:
                counter_copy.pop(key)
            else:
                counter_copy[key] -= 1

            for suffix in self.recursiveUnique(counter_copy):
                output.append([key] + suffix)

        return output
