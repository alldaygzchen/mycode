

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def removeNthFromEnd(self, head, n): #n=3

        dummy = ListNode(0,head)
        left = dummy
        right  = head
        
        while n>0:# 3,2,1
            right = right.next
            n-=1 # explode
        
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
        
