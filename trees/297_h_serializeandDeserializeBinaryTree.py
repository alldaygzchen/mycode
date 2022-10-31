
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec():
    def serialize(self,root):
        self.res = []
        self.helper1(root)
        return ",".join(self.res)


    def deserialize(self,data):
        self.vals = data.split(",")
        self.i = 0 
        return self.helper2()


    def helper1(self,root):

        if not root:
            self.res.append("N")
            return

        self.res.append(str(root.val))
        self.helper1(root.left)
        self.helper1(root.right)

    def helper2(self):

        if self.vals[self.i]=="N":
            self.i+=1 #right
            return None

        node = TreeNode(int(self.vals[self.i]))
        self.i+=1

        node.left = self.helper2()
        node.right= self.helper2()

        return node
