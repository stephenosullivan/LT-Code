__author__ = 'stephenosullivan'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        extrahead = ListNode(None)
        extrahead.next = head
        ptr = head
        while ptr and ptr.next:
            if ptr.next.val < ptr.val:
                selectptr = extrahead
                while ptr.next.val > selectptr.next.val:
                    selectptr = selectptr.next

                # Take out ptr
                tmp = ptr.next
                ptr.next = ptr.next.next

                # Place it in the sorted list
                tmp2 = selectptr.next
                selectptr.next = tmp
                tmp.next = tmp2
            else:
                ptr = ptr.next
        return extrahead.next
