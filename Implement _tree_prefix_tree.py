class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.next = None
        self.follows = None


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def __insert(self, current, word):
        if word:
            if current.val == word[0]:
                if current.next is None:
                    current.next = TrieNode()
                self.__insert(current.next, word[1:])

            elif current.val is None:
                current.val = word[0]
                current.next = TrieNode()
                self.__insert(current.next, word[1:])

            else:
                if not current.follows:
                    current.follows = TrieNode()
                self.__insert(current.follows, word)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        self.__insert(self.root, word + '$')

    def __search(self, current, word):
        if word:
            if current.val == word[0]:
                return self.__search(current.next, word[1:])
            else:
                if current.follows:
                    return self.__search(current.follows, word)
                else:
                    return False
        else:
            return True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return self.__search(self.root, word + '$')

    def __startsWith(self, current, prefix):
        if prefix:
            if current.val == prefix[0]:
                return self.__startsWith(current.next, prefix[1:])
            else:
                if current.follows:
                    return self.__startsWith(current.follows, prefix)
                else:
                    return False
        else:
            return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.__startsWith(self.root, prefix)


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("a")
print("trie search", trie.search("ab"))
print(trie.root.next.val)
print(trie.startsWith('ab'))
