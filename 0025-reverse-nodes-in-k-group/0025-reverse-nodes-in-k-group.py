# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None or k < 2:
            return head
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        end = head
        count = 0
        while end:
            count += 1
            if count % k == 0:
                start = self.reverse(start, end.next)
                end = start.next
            else:
                end = end.next
        return dummy.next
    
    def reverse(self, start, end):
        prev, curr = start, start.next
        first = curr
        while curr != end:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        start.next = prev
        first.next = curr
        return first
                

                
           