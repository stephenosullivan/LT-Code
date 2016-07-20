class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        pairs = [0] * len(nums1) * len(nums2)
        # Construct pairs
        for index1 in range(len(nums1)):
            for index2 in range(len(nums2)):
                pairs[index2 + len(nums2) * index1] = nums1[index1], nums2[index2]

        pairs.sort(key=lambda x: x[0] + x[1])

        if k <= len(pairs):
            return pairs[:k]
        return pairs
