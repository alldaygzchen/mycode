class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root):

        self.res = float("-infinity")
        self.helper(root)
        return self.res

    def helper(self,root):

        if not root:
            return 0

        leftMax = self.helper(root.left)
        rightMax = self.helper(root.right)
        
        leftMax = max(leftMax,0)
        rightMax= max(rightMax,0)



        self.res = max(self.res,root.val + leftMax + rightMax)

        return root.val + max(leftMax,rightMax)




