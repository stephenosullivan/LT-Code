__author__ = 'stephenosullivan'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        ptr = node
        while ptr.next and ptr.next.next:
            ptr.val = ptr.next.val
            ptr = ptr.next
        ptr.val = ptr.next.val
        ptr.next = None

