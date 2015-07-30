__author__ = 'stephenosullivan'

"""
Given a sorted linked list, delete all duplicates such that each element appear only once.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head:
            return head
        else:
            previous = head
            ptr = None

        if previous.next:
            ptr = previous.next

            while ptr.next:
                if previous.val == ptr.val:
                    ptr = ptr.next
                else:
                    previous.next = ptr
                    previous = ptr
                    ptr = ptr.next

            if previous.val == ptr.val:
                previous.next = None
            else:
                previous.next = ptr
                ptr.next = None

        return head
