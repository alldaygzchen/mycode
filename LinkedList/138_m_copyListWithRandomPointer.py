
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):

        copy_dict ={None:None} #oldNode=>copyNode


        curr = head
        while curr:
            copy =Node(curr.val)
            copy_dict[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = copy_dict[curr]
            copy.next = copy_dict[curr.next] #copy_dict
            copy.random = copy_dict[curr.random]

            curr = curr.next

        return copy_dict[head]






