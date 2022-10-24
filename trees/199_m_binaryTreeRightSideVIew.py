# Definition for a binary tree node.
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root):
        
        res = []
        q = collections.deque()
        if root:
            q.append(root)

        while q:

            rightNode =None

            for _ in range(len(q)):

                node = q.popleft()

                if node:
                    rightNode = node
                    q.append(node.left)
                    q.append(node.right)

            res.append(rightNode.val)

        return res

