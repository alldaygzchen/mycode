# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k):

        dummy = ListNode(0,head)
        groupPrev = dummy

        while True:
            kth = self.getKth()




        return dummy.next