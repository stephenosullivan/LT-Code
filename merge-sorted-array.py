__author__ = 'stephenosullivan'

class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        count = m + n
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            count -= 1
            if nums1[m] > nums2[n]:
                nums1[count] = nums1[m]
                m -= 1

            else:
                nums1[count] = nums2[n]
                n -= 1


        while n>=0:
            count -= 1
            nums1[count] = nums2[n]
            n -= 1

