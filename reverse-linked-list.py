__author__ = 'stephenosullivan'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        return self.reverseListRecursive(head, None)

    def reverseListRecursive(self,node, last):
        #finish = False
        if node is None:
            return None
        else:
            if node.next == None:
                node.next = last
                return node
            else:
                output = self.reverseListRecursive(node.next,node)
                node.next.next = node
                node.next = last
                return output
