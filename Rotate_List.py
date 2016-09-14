# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head:
            length = 0
            current = head

            while current:
                length += 1
                current = current.next

            extra = ListNode(None)
            extra.next = head

            current = extra
            if k >= length:
                k = k % length
            if k == 0:
                # print("K=0")
                return head
            cnt = length - k

            while cnt:
                cnt -= 1
                current = current.next

            extra.next = current.next
            current.next = None

            node = extra.next
            if node:
                while node.next:
                    node = node.next
                node.next = head

            return extra.next
        return None
