__author__ = 'stephenosullivan'

import string
from collections import deque
import copy


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """

        self.visited = set()
        self.links = {(-1, beginWord): False, (1, endWord): False}
        while True:
            matched = self.nextLayer(wordList)
            if matched:
                front = []
                word = (-1, matched)
                while True:
                    if word in self.links and self.links[word] is not False:
                        front.append(word[1])
                        word = self.links[word]
                    else:
                        front.append(word[1])
                        break

                back = []
                word = (1, matched)
                while True:
                    if word in self.links and self.links[word] is not False:
                        back.append(word[1])
                        word = self.links[word]
                    else:
                        back.append(word[1])
                        break

                return front[:0:-1] + back

    def nextLayer(self, wordList):
        source = copy.deepcopy(self.links)
        for side, currentWord in source.keys():
            for i, replacement in enumerate(currentWord):
                for letter in string.ascii_lowercase:
                    if letter != replacement:
                        newWord = currentWord[:i] + letter + currentWord[i + 1:]

                        if newWord in wordList:
                            print(newWord, side, self.visited, self.links)
                            if (side, newWord) not in self.visited:
                                self.links[(side, newWord)] = (side, currentWord)
                                if (-side, newWord) in self.links:
                                    return newWord

                                self.visited.add((side, newWord))

    def ladderLength2(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        queue = deque()
        queue.append([beginWord])
        while queue:
            path = queue.popleft()
            currentWord = path[-1]
            for i, replacement in enumerate(currentWord):
                for letter in string.ascii_lowercase:
                    newWord = currentWord[:i] + letter + currentWord[i + 1:]
                    if newWord == endWord:
                        return len(path) + 1
                    if newWord in wordList and newWord not in path:
                        print(newWord)
                        if endWord[i] == letter:
                            queue.appendleft(path + [newWord])
                        else:
                            queue.append(path + [newWord])


if __name__ == '__main__':
    sol = Solution()
    wordList = ["hot", "cog", "dot", "dog", "hit", "lot", "log"]
    print("Answer: ", sol.ladderLength('hit', 'cog', wordList))
