# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if head==None:
            return True
        elif head.next==None:
            return True
        else:
            cnt = 0
            node = head
            savehead = head
            while node!=None and node.next!=None:
                print(node.val,cnt)
                cnt += 1
                previous = node
                node = node.next

            if node.val == savehead.val:
                if cnt>2:
                    previous.next = None
                    return self.isPalindrome(savehead.next)
                else:
                    return True
            else:
                return False


sol = Solution()
one = ListNode(1)
two = ListNode(2)
three = ListNode(2)
four = ListNode(1)
one.next = two
two.next = three
three.next = four

print(sol.isPalindrome(one))