class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        output = []
        worddict = {word: index for index, word in enumerate(words)}
        for word, index in worddict.items():
            if reversed(word) in worddict and reversed(word) != word:
                output.append([index, worddict[reversed(word)][1]])

    def isPalindrome(self, word):
        for i in range(len(word) // 2):
            if word[i] != word[len(word) - i - 1]:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome('worddrow'))
