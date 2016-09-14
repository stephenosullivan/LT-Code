# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head:
            length = 0
            current = head
            while current:
                length += 1
                current = current.next

            if length == 1:
                return TreeNode(head.val)

            half = length // 2
            current = head
            while half:
                half -= 1
                current = current.next

            center = TreeNode(current.val)
            right = current.next

            last = head
            while last.next != current:
                last = last.next
            last.next = None

            if head != current:
                center.left = self.sortedListToBST(head)
            center.right = self.sortedListToBST(right)

            return center
        return None
