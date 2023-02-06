# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        # 1 reach node at position LEFT
        leftPrev,cur=dummy,head
        for i in range(left-1):
            leftPrev,cur=cur,cur.next
        # now cur=LEFT , leftPrev=NODE BEFORE LEFT
        # reverse from left to right
        
        prev=None
        
        for i in range(right-left+1):
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
            
        # update pointers
        leftPrev.next.next=cur
        leftPrev.next=prev
        
        return dummy.next
        

                