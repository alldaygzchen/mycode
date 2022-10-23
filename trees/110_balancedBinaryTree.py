# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def helper(self,root):

        if not root:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)

        if abs(left-right)>1:
            self.res =False

        return 1+max(left,right)

    def isBalanced(self, root):

        self.res = True
        self.helper(root)
        return self.res

# class Solution:

#     def helper(self,root):

#         if not root:
#             return [True,0]

#         left = self.helper(root.left)
#         right = self.helper(root.right)

#         if left[0] and right[0] and abs(left[1]-right[1])<=1:
#             self.res =True
#         else:
#             self.res =False

#         return [self.res,1+max(left[1],right[1])]

#     def isBalanced(self, root):

#         self.res = True
#         self.helper(root)

#         return self.res
        

