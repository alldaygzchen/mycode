# class Node:
#     # constructor to create tree node
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# class Solution:
#     def listAllNode(self,root):
#         self.allPaths = []
#         self.helper(root,[])
#         return self.allPaths


#     def helper(self,root,path):


#         if not root:
#             return

#         path.append(root.data)

#         if not root.left and not root.right:
#             self.allPaths.append(path)
#             return 

#         self.helper(root.left,path.copy())
#         self.helper(root.right,path.copy())

class Node:
    # constructor to create tree node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def listAllNode(self,root):
        self.allPaths = []
        self.helper(root,[])
        return self.allPaths


    def helper(self,root,path):


        if not root:
            return

        path.append(root.data)

        if not root.left and not root.right:
            self.allPaths.append(path)
            return 

        self.helper(root.left,path.copy())
        self.helper(root.right,path)


root = Node(4)
root.left = Node(0)
# root.left.left = Node(None)
root.right = Node(1)
root.left.right = Node(7)
root.right.left = Node(2)
root.right.right = Node(2)
s= Solution()
print(s.listAllNode(root))