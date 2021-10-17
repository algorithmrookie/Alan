class Solution:
    def removeNthFromEnd(self, head, n):
        left = right = head
        count = 0 
        while count < n:
            right = right.next
            count += 1
        if not right:
            return head.next
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return head
