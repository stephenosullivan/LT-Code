__author__ = 'stephenosullivan'

import math


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = dict()
        if len(nums) % 3 == 0:
            threshold = (len(nums) / 3) + 1
        else:
            threshold = math.ceil(len(nums) / 3.)
        store = set()
        ignore = set()
        for index, num in enumerate(nums):
            if num not in store and num not in ignore:
                if num in counter:
                    counter[num] += 1
                else:
                    counter[num] = 1
                if counter[num] == threshold:
                    store.add(num)
                    # Freeing up space costs time!
                    # del counter[num]
                elif counter[num] + (len(nums) - index) < threshold:
                    ignore.add(num)
        return list(store)
