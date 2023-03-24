class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        sorted_head = ListNode(0)
        sorted_head.next = head
        sorted_tail = head
        
       
        curr = head.next
        
        while curr:
           

            if curr.val >= sorted_tail.val:
                sorted_tail = curr
                curr = curr.next
            else:
                
                sorted_tail.next = curr.next
                
               
                insert_pos = sorted_head
                while insert_pos.next.val < curr.val:
                    insert_pos = insert_pos.next
                
               
                curr.next = insert_pos.next
                insert_pos.next = curr
                
               
                curr = sorted_tail.next
        
        return sorted_head.next