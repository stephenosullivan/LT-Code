# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        carry = 0
        sumNode = ListNode(0)
        sumNodeHead = sumNode
        ptr1 = l1
        ptr2 = l2
        while ptr1 or ptr2 or carry:
            if ptr1 == None:
                val1 = 0
            else:
                val1 = ptr1.val
            if ptr2 == None:
                val2 = 0
            else:
                val2 = ptr2.val

            total = val1 + val2 + carry

            if total>9:
                sumNode.val = total%10
                carry = 1
            else:
                sumNode.val = total
                carry = 0

            if ptr1 is not None:
                ptr1 = ptr1.next
            if ptr2 is not None:
                ptr2 = ptr2.next

            if ptr1 or ptr2 or carry:
                sumNode.next = ListNode(0)
                sumNode = sumNode.next

        return sumNodeHead
