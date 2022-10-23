class Solution:
    def isSameTree(self, p, q):

        if not p and not q:
            return True


        if p and q and p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
            return True

        else:
            return False