__author__ = 'stephenosullivan'

"""Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center)."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from operator import xor

class Solution:
    # @param {TreeNode} root
    # @return {boolean}

   def isSymmetric(self,root):
    if root is None:
        return True
    leftlist = [root]
    leftptr = root
    rightlist = [root]
    rightptr = root
    back = False
    while True:

        if leftptr.left and not back:
            if rightptr.right and leftptr.left.val == rightptr.right.val:
                leftlist.append(leftptr.left)
                leftptr = leftptr.left
                rightlist.append(rightptr.right)
                rightptr = rightptr.right
                #print ('left ', leftptr.val, rightptr.val)
            else:
                #print ('left')
                return False



        elif rightptr.right and not back:
            #print ('1')
            return False
        elif leftptr.right:
            back = False
            if rightptr.left and leftptr.right.val == rightptr.left.val:
                leftlist.append(leftptr.right)
                leftptr = leftptr.right
                rightlist.append(rightptr.left)
                rightptr = rightptr.left
                #print ('right ', leftptr.val, rightptr.val)
            else:
                #print ('right')
                return False
        elif rightptr.left:
            #print ('2')
            return False
        else:
            if leftptr == root:
                return True
            else:
                #print (leftptr.val,rightptr.val)
                leftptr = leftlist.pop()
                rightptr = rightlist.pop()
                back = True
                if leftptr == root:
                    return True











    # def isMirror(self,left,right):
    #     if not left and not right:
    #         return True
    #     if left.val == right.val:
    #         if not (bool(left.left) ^ bool(right.right)) and not(bool(left.right) ^ bool(right.left)):
    #             return self.isMirror(left.left,right.right) and self.isMirror(left.right,right.left)
    #         else:
    #             return False
    #     else:
    #         return False

    # def isSymmetric(self, root):
    #     if not root:
    #         return True
    #     if not root.left and not root.right:
    #         return True
    #     elif root.left and root.right:
    #         return self.isMirror(root.left,root.right)
    #     else:
    #         return False



