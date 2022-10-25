# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# nice one !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def isValidBST(self, root):
        return self.helper(root,float("-infinity"),float("infinity"))


    def helper(self,root,left,right):

        if not root:
            return True
        if not (left<root.val and root.val<right):
            return False

        return self.helper(root.left,left,root.val) and self.helper(root.right,root.val,right)





        