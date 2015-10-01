__author__ = 'stephenosullivan'


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations:
            citations.sort()
            for cnt, numCitations in enumerate(citations):
                index = len(citations) - cnt
                if index <= numCitations:
                    return index
        return 0
