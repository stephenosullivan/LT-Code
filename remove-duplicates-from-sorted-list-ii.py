__author__ = 'stephenosullivan'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        headNone = ListNode(0)
        headNone.next = head

        previous = headNone
        current = head
        if current:
            post = current.next

            while current and post:
                if current.val != post.val:
                    previous.next = current
                    previous = previous.next
                else:
                    while post and current.val == post.val:
                        post = post.next
                current = post
                if post:
                    post = post.next
            previous.next = current
        return headNone.next


if __name__ == '__main__':
    sol = Solution()
    a = ListNode(1)
    b = ListNode(2)
    a.next = b
    sol.deleteDuplicates(a)
    while a:
        print(a.val)
        a = a.next
