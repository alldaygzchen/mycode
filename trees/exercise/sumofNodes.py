class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def sum(self,root):

        if not root:
            return 0

        return root.val + self.sum(root.left)+ self.sum(root.right)
