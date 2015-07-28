__author__ = 'stephenosullivan'

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        cycle_test = set()
        return self.isHappyRecursive(n,cycle_test)

    def isHappyRecursive(self,n,cycle_test):
        if n == 1:
            return True
        # Test for cycles
        elif n in cycle_test and len(cycle_test) != 1:
            return False
        # separate the digits of n
        else:
            cycle_test.add(n)
            digitsum = 0
            digits = map(int,list(str(n)))
            for digit in digits:
                digitsum += digit*digit
            #digitsum = sum(x * x for x in map(int,list(str(n))))
            return self.isHappyRecursive(digitsum,cycle_test)

if __name__ == "__main__":
    sol = Solution()
    print(sol.isHappy(7))
