class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxPal = 0, (0, 0)
        for i in range(len(s)):
            cnt = -1
            for j in range(min(len(s) - i, i + 1)):
                if s[i - j] == s[i + j]:
                    cnt += 2
                    if cnt > maxPal[0]:
                        maxPal = cnt, (i - j, i + j)
                else:
                    break

            cnt = 0
            for j in range(min(len(s) - i - 1, i + 1)):
                if s[i - j] == s[i + j + 1]:
                    cnt += 2
                    if cnt > maxPal[0]:
                        maxPal = cnt, (i - j, i + j + 1)
                else:
                    break

        return s[maxPal[1][0]:maxPal[1][1] + 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome('bccb'))
