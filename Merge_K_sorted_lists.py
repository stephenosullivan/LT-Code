# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import bisect


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return []

        head = ListNode(0)
        last = head

        ranking = [node for node in lists if node is not None]
        ranking.sort(key=lambda x: x.val)
        keys = [node.val for node in ranking]

        while ranking:
            current = ranking.pop(0)
            keys.pop(0)
            last.next = current
            last = last.next

            if current.next:
                insert_pos = bisect.bisect_left(keys, current.next.val)
                ranking.insert(insert_pos, current.next)
                keys.insert(insert_pos, current.next.val)

        return head.next
