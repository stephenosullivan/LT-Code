__author__ = 'stephenosullivan'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        realhead = head
        # Reverse the later half of the list
        if head and head.next and head.next.next:
            # Find the midway
            slow = head
            fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            headreversed = self.reverseList(slow.next)

            # Reattach the nodes
            while head.next and headreversed:
                headnext = head.next
                head.next = headreversed
                headreversednext = headreversed.next
                headreversed.next = headnext
                head = headnext
                headreversed = headreversednext

            if headreversed:
                headreversed.next = None
            else:
                head.next = None

    def reverseList(self, head):
        if head.next:
            previous = head
            current = head.next
            while current != None:
                nextnode = current.next
                current.next = previous
                previous = current
                current = nextnode
            head.next = None
            return previous
        else:
            return head

    # O(n^2) in time
    # def reorderList(self, head):
    #     if head and head.next and head.next.next:
    #         node = head
    #         cnt = 0
    #         while node:
    #             node = node.next
    #             cnt += 1
    #         start = head
    #         while cnt>1:
    #             skip = cnt - 1
    #             end = start
    #             while skip:
    #                 end = end.next
    #                 skip -= 1
    #             nextstart = start.next
    #             start.next = end
    #             end.next = nextstart
    #             start = nextstart
    #             cnt -= 2
    #         if cnt == 1:
    #             start.next.next = None
    #         else:
    #             start.next = None


