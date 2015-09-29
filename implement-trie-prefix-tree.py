__author__ = 'stephenosullivan'


class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follows = None
        self.next = None
        self.value = None


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """

        def _insert(node, word):
            if not word:
                yield None
            elif node is None:
                node = TrieNode()
                node.value = word[0]
                node.next = _insert(node.next, word[1:])
            elif node.value == word[0]:
                node.next = _insert(node.next, word[1:])
            else:
                node.follows = _insert(node.follows, word)
            return node

        wordin = word + '$'
        self.root = _insert(self.root, wordin)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        def _search(node, word):
            if not word:
                return True
            if node:
                if word[0] == node.value:
                    return _search(node.next, word[1:])
                elif node.follows:
                    return _search(node.follows, word)
                else:
                    return False
            else:
                return False

        wordtest = word + '$'
        return _search(self.root, wordtest)

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

        def _startsWith(node, word):
            if not word:
                if node:
                    return True
                else:
                    return False
            if node:
                if word[0] == node.value:
                    return _startsWith(node.next, word[1:])
                elif node.follows:
                    return _startsWith(node.follows, word)
                else:
                    return False
            else:
                return False

        return _startsWith(self.root, prefix)

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

if __name__ == '__main__':
    myTrie = Trie()
    myTrie.insert('apple')
    myTrie.insert('zebra')
    print(myTrie.search('apples'))
