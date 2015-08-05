__author__ = 'stephenosullivan'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        output = ListNode(0)
        node = output
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
                node = node.next
            else:
                node.next = l2
                l2 = l2.next
                node = node.next

        if l1:
            node.next = l1
        elif l2:
            node.next = l2

        return output.next
