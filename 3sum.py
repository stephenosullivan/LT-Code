__author__ = 'stephenosullivan'


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}



    #O(n^2)
    def threeSumSlow(self, nums):
        if len(nums) < 3:
            return
        else:
            counter = dict()
            for i in nums:
                if i not in counter:
                    counter[i] = 1
                else:
                    counter[i] += 1

            nums.sort()
            solution_set = set()
            first_prev = None
            second_prev = None

            for first in nums[:-2]:
                counter[first] -= 1
                if first != first_prev:
                    for second in nums[1:-1]:
                        if counter[second]:
                            counter[second] -= 1
                            if second != second_prev:
                                if -first-second in counter:
                                    solution_set.add((first,second,-first-second))
                                second_prev = second
                            counter[second] += 1
                    first_prev = first
                counter[first] += 1
            return list(solution_set)




if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-14,-10,-1,8,-8,-7,-3,-2,14,10,3,3,-1,-15,6,9,-1,6,-2,-6,-8,-15,8,-3,-14,5,-1,-12,-10,-5,-9,-8,1,-3,-15,0,-3,-11,6,-11,7,-6,7,-9,-6,-10,7,1,11,-10,10,-12,-10,3,-7,-9,-7,7,-14,-9,10,14,-2,-4,-4,-10,3,1,-14,-6,5,8,-4,-11,14,-3,-6,-2,13,13,3,0,-14,8,10,-14,6,11,1,7,-13,-4,6,0,-1,10,-3,-13,-4,-2,-11,8,-8]))

