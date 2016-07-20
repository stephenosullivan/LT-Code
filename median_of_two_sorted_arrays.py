__author__ = 'stephenosullivan'


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1_begin = 0
        nums1_end = (len(nums1) - 1)
        nums2_begin = 0
        nums2_end = (len(nums2) - 1)

        mid = (len(nums1) + len(nums2)) // 2
        print("Mid is: ", mid)
        length = (len(nums1) + len(nums2))
        odd = length % 2
        mid -= odd
        print(nums1_end - nums1_begin, nums2_end - nums2_begin)
        while (nums1_end - nums1_begin) > 1 and (nums2_end - nums2_begin) > 1:
            print("In while:", nums1[nums1_begin:nums1_end + 1], nums2[nums2_begin:nums2_end + 1])
            if (nums1_end - nums1_begin) > (nums2_end - nums2_begin):
                guess = (nums1_begin + nums1_end) // 2
                if nums2[mid - guess] > nums1[guess]:
                    nums1_begin = guess
                    nums2_end = mid - guess
                elif nums2[mid - guess] < nums1[guess]:
                    nums1_end = guess
                    nums2_end = mid - guess
                else:
                    return nums1[guess]
            else:
                guess = (nums2_begin + nums2_end) // 2
                print(guess, nums2_begin, nums2_end, nums1[mid - guess], nums2[guess])
                if nums1[mid - guess] > nums2[guess]:
                    nums2_begin = guess
                    nums1_end = mid - guess
                elif nums1[mid - guess] < nums2[guess]:
                    nums2_end = guess
                    nums1_end = mid - guess
                else:
                    return nums2[guess]

        return nums1[nums1_begin:nums1_end + 1], nums2[nums2_begin:nums2_end + 1]

        # mid = (len(nums1) + len(nums2))//2
        # if len(nums1) > len(nums2):
        #     initial_value = nums1[len(nums1)//2]
        #     if self.find_above_value(initial_value, nums2) + initial_value > mid:
        #         # aim for
        #         nums1_begin = len(nums1)//2
        #         nums2_end = len(nums2)//2
        #     elif self.find_above_value(initial_value, nums2) + initial_value < mid:
        #         pass
        # else:
        #     initial_value = nums2[len(nums2)//2]
        #     self.find_above_value(initial_value, nums1)


        # def findMedianSortedArrays(self, nums1, nums2):
        #     """
        #     :type nums1: List[int]
        #     :type nums2: List[int]
        #     :rtype: float
        #     """
        #
        #     mid = (len(nums1) + len(nums2))//2
        #     if len(nums1) > len(nums2):
        #         initial_value = nums1[len(nums1)//2]
        #         if self.find_above_value(initial_value, nums2) + initial_value > mid:
        #             # aim for
        #             pass
        #         elif self.find_above_value(initial_value, nums2) + initial_value < mid:
        #             pass
        #     else:
        #         initial_value = nums2[len(nums2)//2]
        #         self.find_above_value(initial_value, nums1)

        # def find_nearest_value(self, value, nums):
        #     front = 0
        #     back = len(nums)-1
        #     mid = (front + back)//2
        #     while front != back:
        #         mid = (front + back)//2
        #         if value <= nums[mid]:
        #             back = mid
        #             #return self.find_above_value(value,nums[:mid])
        #         else:
        #             front = mid
        #             #return self.find_above_value(value, nums[mid+1:])
        #     return mid


if __name__ == '__main__':
    a = Solution()
    print(a.findMedianSortedArrays([1, 5, 7], [2, 4, 5, 6, 8]))
