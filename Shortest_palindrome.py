class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s) - 1, -1, -1):
            print('new', i)
            for j in range(0, i // 2 + 1):
                print(i - j, j, s[i - j], s[j])
                if s[i - j] != s[j]:
                    break
            else:
                print(i, j)
                return s[-1:i:-1] + s[:]


if __name__ == '__main__':
    sol = Solution()
    print(sol.shortestPalindrome('aacacaaa'))
