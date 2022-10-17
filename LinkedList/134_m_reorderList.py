class Solution:
    def reorderList(self, head):
        

        # find middle
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second =slow.next
        prev = None

        while second:

            tmp = second.next
            second.next = prev

            prev = second
            second = tmp


        