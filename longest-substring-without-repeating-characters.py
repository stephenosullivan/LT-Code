__author__ = 'stephenosullivan'


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = 0
        sub = dict()
        index = dict()
        start = 0
        for i, char in enumerate(s, start=0):
            if char not in sub:
                sub[char] = i
                index[i] = char
            else:
                newstart = sub[char] + 1
                for j in range(start, sub[char] + 1):
                    del sub[index[j]]
                    del index[j]

                sub[char] = i
                index[i] = char
                start = newstart
            output = max(output, i - start + 1)

        return output


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring('abba'))
