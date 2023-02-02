# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        size = 0
        if not head:
            return head
        
        
        
        reverse = ListNode(head.val)
        dummyHead = reverse
        cur = head
        while cur.next:
            reverse.next = ListNode(cur.next.val)
            reverse = reverse.next
            cur = cur.next  
            
        prev,cur=None,head
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        # return prev
        # print(prev) 
#         print(dummyHead)
        
        cur=dummyHead
        curRev=prev
        
        while cur and curRev:
            if cur.val!=curRev.val:
                return False
            cur=cur.next
            curRev=curRev.next
        return True
        
        