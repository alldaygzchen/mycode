class Solution:
    def isSubtree(self, root, subRoot):

        
        
        if not root:
            return False
        
        if not subRoot:
            return True

        if self.sameTree(root,subRoot):
            return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)



    def sameTree(self,p,q):

        if not p and not q:
            return True
        if p and q and p.val==q.val and self.sameTree(p.left,q.left) and self.sameTree(p.right,q.right):
            return True

        else:
            return False
        