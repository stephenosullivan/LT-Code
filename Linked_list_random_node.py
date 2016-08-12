# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import random


class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head. Note that the head is guanranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.len = self.length(head)

    def length(self, head):
        current = head
        cnt = 0
        while current:
            current = current.next
            cnt += 1
        return cnt

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        current = self.head
        index = 0

        while random.random() > self.prob_q(index):
            # print(index)
            index += 1
            current = current.next

        return current.val

    def prob_q(self, index):
        return 1. / (self.len - index)


        # Your Solution object will be instantiated and called as such:
        # obj = Solution(head)
        # param_1 = obj.getRandom()
