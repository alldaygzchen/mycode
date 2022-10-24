# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):

        res = []

        q = collections.deque()
        if root:
            q.append(root)
        while q:
            level_res =[] 

            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level_res.append(node.val)

            res.append(level_res)

        return res


        