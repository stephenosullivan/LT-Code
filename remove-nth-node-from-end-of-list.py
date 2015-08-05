__author__ = 'stephenosullivan'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        prehead = ListNode(None)
        prehead.next = head

        endfinder = head

        n -= 1
        while n:
            endfinder = endfinder.next
            n -= 1

        remover = prehead
        while endfinder.next:
            endfinder = endfinder.next
            remover = remover.next

        remover.next = remover.next.next

        return prehead.next
