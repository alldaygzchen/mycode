class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root):
        return self.helper(root,float("-infinity"))


    def helper(self,node,maxValue):

        if not node:
            return 0

        if node.val>=maxValue:
            res =1
        else:
            res = 0
        maxValue = max(maxValue,node.val)
        res+=self.helper(node.left,maxValue)
        res+=self.helper(node.right,maxValue)

        return res

