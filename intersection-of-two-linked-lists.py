__author__ = 'stephenosullivan'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        lengthA = self.lengthList(headA)
        lengthB = self.lengthList(headB)
        lengthdiff = abs(lengthA - lengthB)
        if lengthA >= lengthB:
            while lengthdiff:
                headA = headA.next
                lengthdiff -= 1
        else:
            while lengthdiff:
                headB = headB.next
                lengthdiff -= 1

        while headA!=headB:
            headA = headA.next
            headB = headB.next
        return headA

    def lengthList(self,head):
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        return length

