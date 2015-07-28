__author__ = 'stephenosullivan'

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        translate_dict = dict()
        used = set()
        for index, letter in enumerate(s):
            if letter in translate_dict:
                if translate_dict[letter] != t[index]:
                    return False
            elif t[index] in used:
                return False
            else:
                translate_dict[letter] = t[index]
                used.add(t[index])

        return True

