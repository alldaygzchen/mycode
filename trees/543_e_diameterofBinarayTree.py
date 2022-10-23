# https://blog.csdn.net/fuxuemingzhu/article/details/70338312
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def diameterOfBinaryTree(self, root):

#         res = float('-infinity')

#         def height(root):

#             nonlocal res



#             if not root:
#                 return -1

#             left = height(root.left)
#             right = height(root.right)

#             res = max(res,left+right+2)

#             return 1+max(left,right)

#         height(root)
#         return res

class Solution:


    def diameterOfBinaryTree(self, root):

        self.res = float('-infinity')

        self.helper(root)
        return self.res


    def helper(self,root):

        if not root:
            return -1

        left = self.helper(root.left)
        right = self.helper(root.right)

        self.res = max(self.res,left+right+2)

        return 1+max(left,right)

