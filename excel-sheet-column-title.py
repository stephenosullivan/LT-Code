__author__ = 'stephenosullivan'

import string

class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        output = ""
        alphabet = string.ascii_uppercase
        div = n

        while True:
            div, remain = divmod(div-1, 26)
            output = alphabet[remain] + output
            if div == 0:
                return output

if __name__ == "__main__":
    sol = Solution()
    print(sol.convertToTitle(703))
