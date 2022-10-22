class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):


        if not root:
            return None

        tmp_right = root.right
        tmp_left = root.left

        root.left =self.invertTree(tmp_right) 
        root.right =self.invertTree(tmp_left) 

        # tmp = root.left
        # root.left = root.right
        # root.right = tmp

        # self.invertTree(root.left)
        # self.invertTree(root.right)

        return root