# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# two pointer
# head ->None


# Replace the old one 
# iterative
# class Solution:
#     def reverseList(self, head):
#         prev , curr = None, head

#         while curr:
#             tmp = curr.next
#             curr.next = prev

#             prev = curr
#             curr = tmp
        
#         return prev

# recursive
class Solution:
    def reverseList(self, head):

        if not head:
            return None
        
        newHead = head

        if head.next:
            newHead =self.reverseList(head.next)
            head.next.next = head

        head.next =None

        return newHead

#e.g. A->B->C->D->E:


# recursive 1  None<-A<-B<-C<-D<-E
# recursive 2  None<-B<-C<-D<-E
# recursive 3  None<-C<-D<-E
# recursive 4  None <-D<-E
# recursive 5  None <-E