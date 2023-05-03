# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        ans=ListNode()
        head=ans


        for index,sortedList in enumerate(lists):
            if sortedList:
              heap.append((sortedList.val,index,sortedList))

        heapify(heap)
        
        while heap:
            val,index,node=heappop(heap)
            head.next=node
            head=head.next
            node=node.next

            if node:
                heappush(heap,(node.val,index,node))

        return ans.next