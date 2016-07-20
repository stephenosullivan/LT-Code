# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        while True:
            myguess = (right + left) // 2
            response = guess(myguess)

            if response == 0:
                return myguess
            elif response == -1:
                right = myguess - 1
            else:
                left = myguess + 1
